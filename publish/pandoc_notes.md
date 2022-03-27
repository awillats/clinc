```bash
pandoc -f markdown+tex_math_single_backslash --pdf-engine=xelatex --numbered-sections -o test.pdf manuscript_v0.md
pandoc -f markdown+tex_math_single_backslash --pdf-engine=xelatex --numbered-sections -o test.pdf test.md
pandoc -f markdown+tex_math_single_backslash --pdf-engine=xelatex -o test.pdf test.md ; open test.pdf
pandoc -f markdown+tex_math_single_backslash -o /Users/adam/Documents/Research/Manuscripts/clinc/publish/test.pdf --pdf-engine=pdflatex

pandoc -f markdown+tex_math_single_backslash -o /Users/adam/Documents/Research/Manuscripts/clinc/publish/manuscript_pandoc.pdf --pdf-engine=xelatex --citeproc 

Error producing PDF. ! Package longtable Error: longtable not in 1-column m

```

compile markdown with panflute filters:
```bash
pandoc -f markdown+tex_math_single_backslash+yaml_metadata_block -o panman.md -F panflute manuscript_v0.md             

pandoc -f markdown+tex_math_single_backslash+yaml_metadata_block -o publish/panman.md -F panflute manuscript_v0_.md
source markdown_to_mp3.sh                                                  
```

right now, the necessary flow seems to be:
- `right-click>save as markdown` (manu_v0_.md)
- pandoc -o panfilt.md -F panflute manu_v0_.md 

## Goal: gathered markdown, with latex in-tact, for panflute to operate on
`RIGHT-CLICK`→`open-in-browser`
  - does use panflute
  
`RIGHT-CLICK`→`HTHML`
  - does use panflute
`RIGHT-CLICK`→`save-as-markdown`
  - renders LaTeX with codecogs :(
  - *doesn't* use panflute
  - (but does compile md imports)
`RIGHT-CLICK`→`PANDOC`
  - preserves LaTeX (renders nicely!)
  - but *doesn't* use panflute 
`Preview:Pandoc Parser`
  - does use panflute
  - LaTeX is plaintext!
    - even without panflute

### 3-stage to focus pdf: md-(compiled)-md-(filtered)-md-(formatted)-pdf 
+yaml_metadata_block?

python publish/compile_markdown_imports.py
 - yaml preserved! 
 
pandoc -f markdown+tex_math_single_backslash -o mc_pf_audio.md -F panflute manuscript_v0_out.md
  - yaml lost :(
  
pandoc -f markdown+tex_math_single_backslash -o pf_audio.pdf --pdf-engine=xelatex --defaults=publish/pd_defaults.yaml mc_pf_audio.md

pandoc -f markdown+tex_math_single_backslash+yaml_metadata_block -o pf_audio.pdf --pdf-engine=xelatex -F panflute --defaults=_meta/meta_default.yaml manuscript_v0_out.md
- can't quite go from 
  
  
pandoc -f markdown+tex_math_single_backslash -o pf_audio.pdf --pdf-engine=xelatex -F panflute --defaults=_meta/meta_default.yaml manuscript_v0_out.md

maybe want to ignore latex altogether? or substitute before pandoc!!!!

`COMPILE: `
  python publish/compile_markdown_imports.py

`FILTER: commandline pandoc (save-as-)md→md`
  - (using Pandoc Parser for preview may no matter?)
  - uses panflute
  - `pandoc -f markdown+tex_math_single_backslash -o preview_saveas_pf.md -F panflute manuscript_v0_.m`
  
`POLISH: commandline pandoc md→pdf`
  - doesnt use panflute?
   `pandoc -f markdown+tex_math_single_backslash -o preview_saveas_pf.pdf --pdf-engine=xelatex preview_saveas_pf.md`
   - may require re-adding yaml for filter or adding filter in commandline
     ```yaml
     classoption: twocolumn
     geometry: margin=1.5cm
     ```
     
### 3-stage to audio pdf: md-(compiled)-html-(...)-md-(filtered)-md-(formatted)-pdf 
<!-- pandoc -f markdown+tex_math_single_backslash -o html_pf.md -F panflute comp.html  -->
pandoc -s -o html.md comp.html
  - convers latex to weird half-plaintext triple slash escaped
pandoc -f markdown+tex_math_single_backslash -o html_pf.md --filter=publish/panflute_filters/cleanup_filter.py html.md
pandoc -f markdown+tex_math_single_backslash -o html_pf.pdf --pdf-engine=xelatex -F panflute --defaults=publish/pd_defaults.yaml html_pf.md


### For polished & formatted pdf
### For audio (preserve latex)
- to compile: any parser - RC:HTML
- to filter: html→md in commandline


## Troubleshooting 

### when using panflute filters, check section headings to make sure all the important pieces are still there 
sometimes checking for delimiters deletes more than you expected. 
if you have nested delimiters, you'll often have this situation:
`A A B B` → `cut:{A a b} B` rather than: `cut:{A-a-b-B}`
- will require fancier regex to fix 

### save to markdown produces latex embeds 
- save as markdown seems to be required to compile imports...but converts equations 
  - see `Math Rendering Online Service ` in settings
  


### longtable error
`longtable` error could be due to rogue `--` in text, remove these

> ! Package amsmath Error: Erroneous nesting of equation structures;
(amsmath)                trying to recover with 'aligned'.

from `\[ begin{align} ...`
- should just be able to cut/filter our align for now 
https://tex.stackexchange.com/questions/284538/align-aligned-and-r-markdown


works for pandoc, but not mpe:
```LaTeX
\begin{align}
\mathbb{V}_{i}(C|S=\text{closed},\sigma^2_S) &= \sigma^2_S \\
\mathbb{V}_{i}(C|S=\text{closed},\sigma^2_S) &\perp \mathbb{V}_{i}(C)
\end{align}
```
works for mpe, but not pandoc
```
\[
\begin{align}
\mathbb{V}_{i}(C|S=\text{closed},\sigma^2_S) &= \sigma^2_S \\
\mathbb{V}_{i}(C|S=\text{closed},\sigma^2_S) &\perp \mathbb{V}_{i}(C)
\end{align}
\]
```
works in both, but produces eq numbers for pandoc
\[
\begin{aligned}
\mathbb{V}_{i}(C|S=\text{closed},\sigma^2_S) &= \sigma^2_S \\
\mathbb{V}_{i}(C|S=\text{closed},\sigma^2_S) &\perp \mathbb{V}_{i}(C)
\end{aligned}
\]
(solve with panflute filter? 
- `\[ \begin{align}` to `\begin{align}`
## Options
https://pandoc.org/MANUAL.html#extension-tex_math_single_backslash

---
`Error: Command failed: pandoc -f markdown+tex_math_single_backslash -o /Users/adam/Documents/Research/Manuscripts/clinc/publish/test.pdf --pdf-engine=xelatex`
 
see: https://tex.stackexchange.com/questions/284538/align-aligned-and-r-markdown
 
 watch out for "---" gets interpreted as a footnote
 
 - [ ] change absolute paths to relative paths? or filter before pandoc
	- use `--resource-path`
 - [ ] pandoc remove any collapsible sections
 https://stackoverflow.com/questions/24208889/how-to-specify-numbered-sections-in-pandocs-front-matter
 
- extending MPE in js: https://shd101wyy.github.io/markdown-preview-enhanced/#/extend-parser



## Useful Panflute notes 

`run_filter(action, *args, **kwargs)`

`run_filters(actions[, prepare, finalize, ...])`
to run multiple filters

`debug(*args, **kwargs)`
Same as print, but prints to stderr (which is not intercepted by Pandoc).

`stringify(element[, newlines])`
Return the raw text version of an element (and its children elements).



