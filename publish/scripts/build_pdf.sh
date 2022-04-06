#unfiltered 
# python -m compile_markdown manuscript_v1 -pve --out publish/aux/
# with filters
#NOTE: doesnt work any more
#DEBUG:
# python -m compile_markdown manuscript_v0 -vepf

this_annex_folder="_annex/clinc/"
md_in="publish/aux/mv0_filt.md"
tex_in="publish/aux/mv0.tex"
img_width=1.0

# CONVERT markdown to LaTeX (with \autocite{})
pandoc --biblatex -o $tex_in $md_in

# REMOVE EMOJI
python -c "import markdown_manuscript_filters as mmf; mmf.remove_emoji('${tex_in}',do_transcribe_emoji=False)"

# CONVERT figs to .jpeg
# REPLACE include statements with jpeg, set new width
python -c "import markdown_manuscript_filters as mmf;\
  mmf.modify_graphics_path_png_jpeg_width('${tex_in}',\
  new_path='$this_annex_folder',textwidth=$img_width, do_convert_imgs=True)"
  
#REPLACE MATH unicode symbols with latex counterparts
python -c "import markdown_manuscript_filters as mmf ; mmf.math_unicode_to_latex_file('${tex_in}')"

