#unfiltered 
# python -m compile_markdown manuscript_v1 -pve --out publish/aux/
# with filters
#NOTE: doesnt work any more
#DEBUG:
# python -m compile_markdown manuscript_v0 -vepf

pandoc --biblatex -o publish/aux/mv0.tex publish/aux/mv0_filt.md
# python -c "import markdown_manuscript_filters as mmf ; mmf.unicode_to_latex_file('publish/aux/mv0.tex',is_verbose=True)"

# python -c "import markdown_manuscript_filters as mmf; import re; mmf.apply_pyrex(re.escape('\includeg'),'%'+re.escape('\includeg'),'test.md','test_out.md',do_ignore_yaml=False)"
# python -c "import markdown_manuscript_filters as mmf ; mmf.unicode_to_latex_file('test_out.md',is_verbose=True)"
# python -c "import markdown_manuscript_filters as mmf; mmf.apply_pyrex(r'[^\x00-\x7F]+','X' ,'test_out.md','test_out.md',do_ignore_yaml=False)"



#REMOVE INCLUDE 
python -c "import markdown_manuscript_filters as mmf; import re; mmf.apply_pyrex(re.escape('\includeg'),'FIG: %'+re.escape('\includeg'),'publish/aux/mv0.tex','publish/aux/mv0.tex',do_ignore_yaml=False)"
#REPLACE MATH
python -c "import markdown_manuscript_filters as mmf ; mmf.unicode_to_latex_file('publish/aux/mv0.tex',is_verbose=True)"
#REMOVE UNICODE
python -c "import markdown_manuscript_filters as mmf; mmf.apply_pyrex(r'[^\x00-\x7F]+','???' ,'publish/aux/mv0.tex','publish/aux/mv0.tex',do_ignore_yaml=False)"
