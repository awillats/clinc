#!/bin/sh
# pandoc -f markdown+tex_math_single_backslash -o mc_pf_audio.md --filter=publish/panflute_filters/cleanup_filter.py manuscript_v0_out.md
# python transplant_yaml.py manuscript_v0_out.md mc_pf_audio.md
# pandoc -f markdown+tex_math_single_backslash -o pf_audio.pdf --pdf-engine=xelatex mc_pf_audio.md