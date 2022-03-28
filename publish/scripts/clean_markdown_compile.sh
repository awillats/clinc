#!/bin/sh

# - [ ] to-do clear intermediate files each time, and stop script if one step fails!

# Markdown w/ imports → concatenated markdown file
#    manuscript_v0.md → mv0_out.md
python publish/scripts/compile_markdown_imports.py
# add yaml back to compiled file
python publish/scripts/transplant_yaml.py manuscript_v0.md publish/gen/mv0_out.md

# Concatenated markdown file → clean, minimal, human-readable markdown
#                 mv0_out.md → mv0_filt.md
# remove comments etc. 
# .md useful for debugging / converting to other formats

# -F panflute \
pandoc -f markdown+tex_math_single_backslash+yaml_metadata_block \
  -o publish/gen/mv0_filt.md \
  --filter=publish/panflute_filters/cleanup_filter.py \
  publish/gen/mv0_out.md             
  
# paste yaml back in (might be redundant)
# python publish/scripts/pyrex.py "\\[" "zz" publish/gen/mv0_filt.md publish/gen/mv0_filt.md
# python publish/scripts/pyrex.py "\\]" 'xx' publish/gen/mv0_filt.md publish/gen/mv0_filt.md
python publish/scripts/transplant_yaml.py manuscript_v0.md publish/gen/mv0_filt.md
# undo softwrap - calls pyrex 
source publish/scripts/unwrap_text.sh publish/gen/mv0_filt.md publish/gen/mv0_filt.md

# filtered markdown → PDF
#       mv0_filt.md → mv0_clean.pdf
# NOTE: consider commenting out .css to-do hiding before this 
echo '... starting pdf conversion ... '
# # clean + convert to two-column pdf
pandoc -f markdown+tex_math_single_backslash \
  -o publish/outputs/mv0_clean.pdf --pdf-engine=xelatex \
  publish/gen/mv0_filt.md
# Consider adding: #   -F panflute \
echo 'pdf available at publish/outputs/mv0_clean.pdf'

# #? to HTML?
# pandoc -f markdown+tex_math_single_backslash \
#   -o publish/outputs/mv0_clean.html --pdf-engine=xelatex \
#   publish/gen/mv0_out.md
