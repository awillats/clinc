import markdown_manuscript_filters as mmf
import os
import subprocess, shlex

#%%
do_send_to_dropbox = False
# _cleaned is created semi-manually 
# - delete excess comments
# - see manuscript-filters/regex_notes.md 

md_output = 'publish/manuscript_v1_out_cleaned.md'
tex_file = 'publish/manuscript_v1_out_autotex.tex'
md_output_tail = md_output.rsplit('/',1)[1]
tex_file_tail = tex_file.rsplit('/',1)[1]

#%%
def run_in_shell(cmd):
    #NOTE: cant use this for piping commands together 
    return subprocess.run(shlex.split(cmd))

pre_file = 'publish/scripts/latex_preamble.tex'
post_file = 'publish/scripts/latex_postamble.tex'
#%%
os.chdir('/Users/adam/Documents/Research/Manuscripts/clinc')
mmf.compile_markdown_imports('manuscript_v1.md',basedir='.',is_verbose=True)

mmf.standardize_tex_math(fnin=md_output)
mmf.apply_pyrex('/figures/','figures/',fnin=md_output,fnout=md_output)


#%% LATEX
# import re
run_in_shell(f'pandoc --biblatex -o {tex_file} {md_output}')
mmf.unwrap(f'{tex_file}', is_verbose=True, do_ignore_yaml=False)
mmf.apply_pyrex(mmf.pyrex.MATCH_UNICODE,'- ',fnin=tex_file,fnout=tex_file)
mmf.modify_graphics_path(new_path='',new_size=mmf.tex_width(1.0),fnin=tex_file)


#%%
#NOTE: can't cat a file into itself!
os.system(f'cat {pre_file} {tex_file} {post_file} > __temp.tex')
os.system(f'mv __temp.tex {tex_file}')
#%%
# if do_send_to_dropbox:
#     os.system(f'cp {md_output} /Users/adam/Dropbox\ \(GaTech\)/Willats_Research/CLINC_manuscript/{md_output_tail}')
#     os.system(f'cp {tex_file} /Users/adam/Dropbox\ \(GaTech\)/Willats_Research/CLINC_manuscript/{tex_file_tail}')
#%%
# TODO: LaTeX to pdf!
