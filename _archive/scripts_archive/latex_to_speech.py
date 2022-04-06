import re 
import pyrex 
import remove_yaml
#%%
#%%


fnin = 'publish/gen/mv0_filt.md'
fnout = 'publish/gen/mv0_auto_audio.md'#'../gen/mv0_auto_audio.md'
do_ignore_yaml = True

# pyrex.apply_pyrex('x\^2','TEST',fnin=fnin, fnout=fnout)

import shutil 
shutil.copy(fnin,fnout)
apply_this_replacement = lambda r,s: pyrex.apply_pyrex(r,s,fnin=fnout, fnout=fnout, do_ignore_yaml=do_ignore_yaml)



math_symb = '[=+\-\*\\\/\.]'
alpha_math = '[\w=+\-\*\\\/\.]'
multi_alpha_math = f'(('+alpha_math+'*))' #w/capture

math_or_open_paren = '[{(=+\-\\\/\.]'
alpha_num_math_fun = '([=+\-*\\\/\.]|[\w\s\^\|]|[\{\(])'
multi_alpha_num_math_fun = '(('+alpha_num_math_fun+'*))' #w/capture
#=+\-*\\\/
#'
#'(\w|\s|\^|\||[{(=+\-\\])' 

left_parens = '['+re.escape('{([')+']'
right_parens = '['+re.escape('})]')+']'

# e.g. \sum_{i=0}^{infinity}{x_i}
sum_regex = re.escape('\sum_{')+multi_alpha_math+re.escape('}^{')\
                   +multi_alpha_math+re.escape('}')
# e.g. \sum_{i=0}^N{x_i}
sum_regex_simple_upper = re.escape('\sum_{')+multi_alpha_math+re.escape('}^')+'(\w*)[\s|\{]'

frac_regex = re.escape('\\frac{')+'(\w*)'+re.escape('}{')+'(\w*)'+re.escape('}')
frac_regex_more = re.escape('\\frac{')+multi_alpha_num_math_fun+\
                       re.escape('}{')+multi_alpha_num_math_fun+re.escape('}')
    
print(sum_regex)
print(frac_regex)                                                                                                                                                    
#%%
replacements = \
    {
    re.escape('losed-loop'): 'losed loop',
    re.escape('pen-loop'): 'pen loop',
    
    'https://((.*)[).])': 'link \\1',
    '\((.*).md\)' : ' link.',
    
    #add separators to acronyms - shouldnt be necessary depending on the speech
    # 'Figure ([A-Z]*):': 'Figure \\1 ' ,
    # '(?<=([A-Z])(?=[A-Z]))':' ',
    
    sum_regex: ' the sum from \\1 to \\3 of ... ',
    sum_regex_simple_upper: ' the sum from \\1 to \\3 of ... ',

    # turns X_t to "X sub t"
    # '_\{([^\}]*)\}' : ' sub \\1',
    # '(\w)_(\w)(?!\w)' : '\\1 sub \\2',
    
    # turns X_t to "X t"
    '_\{([^\}]*)\}' : ' \\1',
    '(\w)_(\w)(?!\w)' : '\\1 \\2',
    
    frac_regex:' \\1 ... over \\2 ',
    frac_regex_more:' \\1 ... ... over \\4 ',
    

    
    re.escape('f(')  : 'a function of ',
    re.escape('}(')  : ' of ',
    '(\w)\((\w)'  : '\\1 of \\2',
    re.escape('\widetilde{')+'(\w*)\}' : ' \\1 tilde ',
    '([\w\}])\^' : '\\1 to the ', 
    re.escape('}^{') : ' to the ',
    re.escape('\dot{')+multi_alpha_math+'\}' : ' \\1 dot ',
    '([A-Z])\-([A-Z])' : ' \\1 minus \\2 ',
    '([\w\s])\|([\w\s])' : '\1 given \\2',
    re.escape('\mid') : '... given ... ', #doesnt work??
    # exponent 
    # sub 
    # dot
    
    # simple substitutions
    re.escape('\sim')   :' is approximately ',
    re.escape('\approx'):' is approximately ',
    re.escape('&='  ) :' = ',
    re.escape('='  )  :' = ',

    re.escape('\\\\'  ) : '... \n ...',
    re.escape('^{T}') : ' transpose ', 
    re.escape('^{-1}') : ' inverse ',
    re.escape('to the 2') : 'squared',
    re.escape('to the -1') : 'inverse',
    re.escape('to the T') : 'transpose',

    re.escape('\sqrt{')+multi_alpha_num_math_fun+'\}' :' square root of \\1',
    re.escape('\gg' ) : ' is much greater than ', 
    re.escape('\ll ' ) : ' is much less than ',
    re.escape('\gt' ) : ' is greater than ', 
    re.escape('\lt' ) : ' is less than ', 
    re.escape('\geq' ) : ' is greater than or equal to ',
    re.escape('\leq') : ' is less than or equal to ',
    re.escape('\infty' ) : ' infinity ', 
    re.escape('→'   ) : ' to ',
    re.escape('\neq') : ' is not equal to', 
    # deletions
    # '\\math(\w*)'     :'',
    re.escape("\\left")+left_parens :'', 
    re.escape("\\right")+right_parens :'', 
    re.escape('\\text')    :'', 
    re.escape('\\begin{')+'(\w*)\}':'',
    re.escape('\\end{')  +'(\w*)\}'  :'',
    re.escape('$$')  : '',
    re.escape('$')   : '',
    # re.escape('\\math')+'(\w*)\{((\w|\s)*)\}' : '\\2', #doesnt work?
    re.escape('\\math')+'(\w*)' : '', #doesnt work?
    '\[\^\w*\](?!:)'   :'', #inline footnote refs
    }
#%%
for reg, sub in replacements.items():
    apply_this_replacement(reg,sub)
    print(reg)
    print(sub)
    print('applied')
#%%
#behead yaml 
remove_yaml.remove_yaml(fnout)
#%%

    