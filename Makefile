pandoc -f markdown+tex_math_single_backslash -o /Users/adam/Documents/Research/Manuscripts/clinc/publish/test.pdf --pdf-engine=xelatex

# pandoc -f markdown+tex_math_single_backslash -o /Users/adam/Documents/Research/Manuscripts/clinc/publish/test.pdf --pdf-engine=pdflatex



# https://pandoc.org/MANUAL.html#extension-tex_math_single_backslash

# Error: Command failed: pandoc -f markdown+tex_math_single_backslash -o /Users/adam/Documents/Research/Manuscripts/clinc/publish/test.pdf --pdf-engine=xelatex Error producing PDF. ! Package amsmath Error: Erroneous nesting of equation structures; (amsmath) trying to recover with `aligned'.
# 
# See the amsmath package documentation for explanation. Type H for immediate help. ...
# 
# l.510 \end{align}
# 
# 
# see: https://tex.stackexchange.com/questions/284538/align-aligned-and-r-markdown
# 
# watch out for ---
# 
# - [ ] pandoc remove any collapsible sections