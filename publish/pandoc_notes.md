```bash
pandoc -f markdown+tex_math_single_backslash --pdf-engine=xelatex --numbered-sections -o test.pdf manuscript_v0.md
pandoc -f markdown+tex_math_single_backslash --pdf-engine=xelatex --numbered-sections -o test.pdf test.md
pandoc -f markdown+tex_math_single_backslash --pdf-engine=xelatex -o test.pdf test.md ; open test.pdf
pandoc -f markdown+tex_math_single_backslash -o /Users/adam/Documents/Research/Manuscripts/clinc/publish/test.pdf --pdf-engine=pdflatex
```
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