#!/bin/sh

#python for @import to compiled - implicitly from /manuscript_v0.md to /publish/gen/mv0_out.md
python publish/scripts/compile_markdown_imports.py
# add yaml back to compiled file
# pwd
python publish/scripts/transplant_yaml.py manuscript_v0.md publish/gen/mv0_out.md

#remove comments etc. 
# # For debugging / converting to other formats
pandoc -f markdown+tex_math_single_backslash+yaml_metadata_block \
  -o publish/gen/mv0_filt.md \
  -F panflute \
  publish/gen/mv0_out.md             

# paste yaml back in (might be redundant)
python publish/scripts/transplant_yaml.py manuscript_v0.md publish/gen/mv0_filt.md

echo '... starting pdf conversion ... '
# clean + convert to two-column pdf
# pandoc -f markdown+tex_math_single_backslash \
#   -o publish/outputs/mv0_clean.pdf --pdf-engine=xelatex \
#   publish/gen/mv0_filt.md
# # Consider adding: #   -F panflute \
# echo 'pdf available at publish/outputs/mv0_clean.pdf'
# #? to HTML?
# pandoc -f markdown+tex_math_single_backslash \
#   -o publish/outputs/mv0_clean.html --pdf-engine=xelatex \
#   publish/gen/mv0_out.md
