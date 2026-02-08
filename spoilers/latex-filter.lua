-- latex-filter.lua
-- Pandoc Lua filter for LaTeX PDF of the spoiler guide
--
-- Transforms the markdown heading structure for book-class LaTeX:
--   # Title           → removed (template handles title page)
--   ## Table of Contents → removed (template generates LaTeX TOC)
--   ## Part X: Name   → \part{Name} on its own page
--   ## Appendices     → \part{Appendices}
--   ## Other          → \chapter (level 2, maps to chapter)
--   ### Chapter       → shifted to level 2 → \chapter
--   #### Section      → shifted to level 3 → \section
--   ##### Subsection  → shifted to level 4 → \subsection

-- Strip Emph inside BlockQuote so \itshape from the quote environment
-- isn't toggled back to upright by pandoc's \emph{}
function BlockQuote(bq)
  return bq:walk({
    Emph = function(emph)
      return emph.content
    end
  })
end

-- Check if a code block looks like a Sokoban map
local function is_sokoban_map(block)
  if block.tag ~= "CodeBlock" then return false end
  return block.text:match("%^") and block.text:match("[┌┐└┘├┤┬┴┼│─]")
end

-- Escape special LaTeX characters in a plain text string
local function escape_latex(s)
  s = s:gsub("\\", "\\textbackslash{}")
  s = s:gsub("([#$%%&_{}<>~^])", "\\%1")
  return s
end

-- Render an ordered list as plain LaTeX text for side-by-side layout
local function render_instructions(list_block)
  local items = {}
  for i, item in ipairs(list_block.content) do
    local text = pandoc.utils.stringify(pandoc.Pandoc(item))
    table.insert(items, i .. ". " .. escape_latex(text))
  end
  return items
end

-- Add left padding to each line of a code block
local function pad_code(text, spaces)
  local pad = string.rep(" ", spaces)
  local lines = {}
  for line in (text .. "\n"):gmatch("(.-)\n") do
    table.insert(lines, pad .. line)
  end
  return table.concat(lines, "\n")
end

-- Create side-by-side Sokoban layout: map minipage + instructions minipage
local function sokoban_side_by_side(code_block, list_block)
  -- Calculate max line width and line count of the map
  local max_line = 0
  local map_lines = 0
  for line in code_block.text:gmatch("[^\n]+") do
    if #line > max_line then max_line = #line end
    map_lines = map_lines + 1
  end

  -- Wider maps get 40% of page, narrow maps get 33%
  local map_frac = max_line > 25 and 0.40 or 0.33
  local instr_frac = 0.96 - map_frac

  local instructions = render_instructions(list_block)

  -- Split instructions: fit beside the map, overflow goes full-width below.
  -- Each instruction with spacing takes ~1.5 map lines of vertical space.
  local side_count = math.min(#instructions, math.floor(map_lines / 1.5))
  local side_instrs = {}
  local overflow_instrs = {}
  for j = 1, #instructions do
    if j <= side_count then
      table.insert(side_instrs, instructions[j])
    else
      table.insert(overflow_instrs, instructions[j])
    end
  end

  local side_text = table.concat(side_instrs, "\\par\\smallskip\n")

  -- Center the ASCII block within the minipage by padding with spaces.
  -- Estimate ~42 monospace chars per full linewidth at scriptsize.
  local avail_chars = math.floor(42 * map_frac)
  local pad = math.max(0, math.floor((avail_chars - max_line) / 2))
  local padded_map = pad > 0 and pad_code(code_block.text, pad) or code_block.text

  local result =
    "\\begin{minipage}[t]{" .. string.format("%.2f", map_frac) .. "\\linewidth}\n" ..
    "\\begin{Verbatim}[fontsize=\\scriptsize," ..
    "frame=single,framesep=0.3em," ..
    "rulecolor=\\color{codeframe}]\n" ..
    padded_map .. "\n" ..
    "\\end{Verbatim}\n" ..
    "\\end{minipage}\\hfill\n" ..
    "\\begin{minipage}[t]{" .. string.format("%.2f", instr_frac) .. "\\linewidth}\n" ..
    "\\small\\raggedright\n" ..
    side_text .. "\n" ..
    "\\end{minipage}\n"

  -- Add overflow instructions full-width below
  if #overflow_instrs > 0 then
    result = result ..
      "\\par\\smallskip\n" ..
      "{\\small\\raggedright " ..
      table.concat(overflow_instrs, "\\par\\smallskip\n") ..
      "\\par}\n"
  end

  result = result .. "\\medskip"

  return pandoc.RawBlock("latex", result)
end

function Pandoc(doc)
  local blocks = doc.blocks
  local new_blocks = {}
  local skip_until_next_h2 = false
  local skip_epigraph = false
  local i = 1

  while i <= #blocks do
    local block = blocks[i]

    -- Check if we should stop skipping (hit next h2+ after TOC)
    if skip_until_next_h2 and block.tag == "Header" and block.level <= 2 then
      skip_until_next_h2 = false
    end

    if skip_until_next_h2 then
      i = i + 1
      goto continue
    end

    -- Skip the epigraph blockquote right after the title (template handles it)
    if skip_epigraph then
      skip_epigraph = false
      if block.tag == "BlockQuote" then
        i = i + 1
        goto continue
      end
    end

    if block.tag == "Header" then
      local text = pandoc.utils.stringify(block)

      -- Remove document title
      if block.level == 1 then
        skip_epigraph = true
        i = i + 1
        goto continue
      end

      -- Remove Table of Contents section and all content until next ##
      if block.level == 2 and text == "Table of Contents" then
        skip_until_next_h2 = true
        i = i + 1
        goto continue
      end

      -- Part headings → custom LaTeX part page
      if block.level == 2 then
        local part_name = text:match("^Part %w+: (.+)$")
        if part_name then
          table.insert(new_blocks, pandoc.RawBlock("latex",
            "\\clearpage\n" ..
            "\\thispagestyle{partpage}\n" ..
            "\\phantomsection\n" ..
            "\\addcontentsline{toc}{part}{" .. part_name .. "}\n" ..
            "\\vspace*{2in}\n" ..
            "\\begin{center}\n" ..
            "{\\huge\\bfseries " .. part_name .. "}\n" ..
            "\\end{center}\n" ..
            "\\markboth{}{}\n" ..
            "\\clearpage\n" ..
            "\\def\\currentpartname{" .. part_name .. "}"))
          i = i + 1
          goto continue
        end

        if text == "Appendices" then
          table.insert(new_blocks, pandoc.RawBlock("latex",
            "\\clearpage\n" ..
            "\\thispagestyle{partpage}\n" ..
            "\\phantomsection\n" ..
            "\\addcontentsline{toc}{part}{Appendices}\n" ..
            "\\vspace*{2in}\n" ..
            "\\begin{center}\n" ..
            "{\\huge\\bfseries Appendices}\n" ..
            "\\end{center}\n" ..
            "\\markboth{}{}\n" ..
            "\\clearpage\n" ..
            "\\def\\currentpartname{Appendices}"))
          i = i + 1
          goto continue
        end

        -- Non-Part ## headings stay at level 2 → \chapter
      end

      -- Shift ### → level 2 (chapter), #### → level 3 (section), etc.
      if block.level >= 3 then
        block.level = block.level - 1
      end

      -- Break long headings before parenthetical subtitles in LaTeX
      if text:match("Kill You") then
        local inlines = block.content
        for j = 1, #inlines do
          if inlines[j].tag == "Str" and inlines[j].text:match("^%(") then
            table.insert(inlines, j, pandoc.RawInline("latex", "\\\\"))
            block.content = inlines
            break
          end
        end
      end
    end

    -- Make "The Big Picture" code block a floating figure
    if block.tag == "CodeBlock" and block.text:match("Dungeons of Doom") then
      table.insert(new_blocks, pandoc.RawBlock("latex",
        "\\begin{figure}[tp]\n" ..
        "\\centering\n" ..
        "\\begin{minipage}{0.92\\linewidth}\n" ..
        "\\begin{Verbatim}[fontsize=\\footnotesize," ..
        "frame=single,framesep=0.3em," ..
        "rulecolor=\\color{codeframe}]\n" ..
        block.text .. "\n" ..
        "\\end{Verbatim}\n" ..
        "\\end{minipage}\n" ..
        "\\end{figure}"))
      i = i + 1
      goto continue
    end

    -- Sokoban maps: side-by-side with following numbered instructions
    if is_sokoban_map(block) and i + 1 <= #blocks and blocks[i+1].tag == "OrderedList" then
      table.insert(new_blocks, sokoban_side_by_side(block, blocks[i+1]))
      i = i + 2  -- skip both the code block and the list
      goto continue
    end

    -- Convert horizontal rules to decorative diamond ornament (centered)
    -- vfill on both sides so it centers vertically if alone on a page
    if block.tag == "HorizontalRule" then
      table.insert(new_blocks, pandoc.RawBlock("latex",
        "\\null\\vfill\n" ..
        "\\begin{center}\n" ..
        "{\\color[gray]{0.45}" ..
        "\\rule[0.35ex]{3em}{0.4pt}" ..
        "\\hspace{0.4em}" ..
        "\\raisebox{-0.1ex}{\\footnotesize\\textrm{◆}}" ..
        "\\hspace{0.4em}" ..
        "\\rule[0.35ex]{3em}{0.4pt}}\n" ..
        "\\end{center}\n" ..
        "\\vfill\\null"))
      i = i + 1
      goto continue
    end

    table.insert(new_blocks, block)
    i = i + 1
    ::continue::
  end

  return pandoc.Pandoc(new_blocks, doc.meta)
end
