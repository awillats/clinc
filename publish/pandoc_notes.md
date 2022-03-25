```bash
pandoc -f markdown+tex_math_single_backslash --pdf-engine=xelatex --numbered-sections -o test.pdf manuscript_v0.md
pandoc -f markdown+tex_math_single_backslash --pdf-engine=xelatex --numbered-sections -o test.pdf test.md
pandoc -f markdown+tex_math_single_backslash --pdf-engine=xelatex -o test.pdf test.md ; open test.pdf
pandoc -f markdown+tex_math_single_backslash -o /Users/adam/Documents/Research/Manuscripts/clinc/publish/test.pdf --pdf-engine=pdflatex
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