#!/usr/bin/env python3
# https://github.com/sergiocorreia/panflute/blob/master/examples/panflute/comments.py
import sys,os
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")
import panflute as pf
# try:
#     
# except:
#     with open('err.txt', 'w') as f:
#         sys.stdout = f 
#         print('ERROR: cant find panflute from:')
#         print(os.getcwd())
#         print (os.environ['CONDA_DEFAULT_ENV'])
#     raise Exception("Cant find panflute")
import re

'''
Classes: http://scorreia.com/software/panflute/code.html#low-level-classes
Para for most text 
Header 
Emph 
RawBlock


elem.text.replace()
remove YAML with MetaBlocks ?

-----
TODO: figure out raw find and replace within a paragraph 
    - just run a python script on the text file?
    
    
TODO: add spoken version of LaTeX math 
    - would need to do this *before* mume renders latex to imgs
    - sqrt{}: square root 
    - x^b: x to the b 
    - x_i: x sub i OR x i 
    - x→y: x to y 
    - \dot{x}: x dot 
    - f(x | t): f of x given t 
    - \sum^{\inf}_{k=0}{W_k}: sum of W sub k from k=0 to inf
    - \frac{WWs^2}{Ws*Ws}: W W over Ws times Ws 

TODO: split file at section headings to make several audio files


cut footnotes
\[\^.*\}
\[\^.*\](?!:)
'''
# h = pf.Header(pf.Str('hi'))
# # print(h.content)
# h.content = [pf.Str('ho'),pf.Str('ho'),pf.Str('ho')]
# [print(pf.stringify(c)) for c in list(h.content)];
#%%
def replace_or_not(msg=None, plaintext=False):
    if msg and plaintext: return msg 
    if msg and not plaintext: return pf.Str(msg)
    if not msg and plaintext: return ''
    if not msg and not plaintext: return
    else: return
#%%
def speak_header(elem, doc):
    '''
    removes # replaces with section or subsection - intended for text-to-speech
    '''
    if isinstance(elem, pf.Header):
        # elem.level 

        if elem.level <= 1:
            title = ''.join(list([pf.stringify(c) for c in list(elem.content)]))
            elem = pf.Para(pf.Str('SECTION: '+title))
            # +''.join(title)))
            pass
        elif elem.level >= 2:
            title = ''.join(list([pf.stringify(c) for c in list(elem.content)]))
            elem = pf.Para(pf.Str('SUB SECTION: '+title))

            # elem.content = pf.Para(pf.Str('SUBSECTION:'+title))
            pass
        else:
            pass
    return elem
    
# def replace_with_text(elem, doc):
#     # def findrep(s):
#     #     s.replace('a'
# 
#     if isinstance(elem,pf.Para):
#         # doc.replace_keyword('asdasd',pf.Str('@'))
# 
#         if hasattr(elem.content,'text'):
#             for i,c in enumerate(elem.content):
#                 # works...but steamrolls formatting ...
#                 s = pf.stringify(c)
#                 s = s.replace('a','@')
#                 elem.content[i] = pf.Str(s)
#                 # works, if its already a string ... 
#                 # elem.content[i].text = elem.content[i].text.replace('d','#')
# 
#         # return pf.Para(pf.Str(s)+pf.Str(s))
#         return elem
        
def prepare(doc):
    doc.ignore = False    

  
def genfn_delete_between_marks(start_ignore="<!--", end_ignore="-->",replace_with=None):
    selector_fn = lambda e: True # change this to apply selectively
    
    def comment_fn(elem,doc):
        if elem is None or elem==[]:
        #isinstance(elem,list):
            'untested'
            return elem
    
        # if not hasattr(doc,'ignore'):
        #     return None
            
        is_selected = selector_fn(elem)
        
        if is_selected and re.search(start_ignore, pf.stringify(elem)):
            doc.ignore=True
        
        if doc.ignore == True:
            if is_selected and re.search(end_ignore, pf.stringify(elem)):
                doc.ignore = False
                            
                if replace_with is None:
                    return [] 
                if hasattr(elem, 'content'):
                    elem.content = [replace_or_not(replace_with)]
                elif hasattr(elem, 'text'):
                    #probably a html block?
                    # elem.text = replace_or_not(replace_with, True)
                    elem = pf.Str(replace_or_not(replace_with, True))
                # else:
                #     return []   
                return elem
            return []
    return comment_fn

def gather_delim_fns(delims):
    delim_fns = []
    for delim in delims:
        rep_msg = delim[2] if len(delim)>2 else None
        delim_fn = genfn_delete_between_marks(delim[0],delim[1],rep_msg)
        delim_fns.append(delim_fn)
    return delim_fns
#%%
# More specific functions
def no_equations_fn(elem,doc, rep_msg=None):
    if isinstance(elem,pf.Math):
        elem = replace_or_not(rep_msg)
        return elem
    f = genfn_delete_between_marks('\[','\]',rep_msg)
    return f(elem,doc)

def standardize_equation_delims(elem,doc):
    elem.replace_keyword('\[',pf.Str('$$'))
    elem.replace_keyword('\]',pf.Str('$$'))

    # if isinstance(elem, pf.RawInline):
    #     # elem.replace_keyword('\[',pf.Str('$$'))
    #     # elem.replace_keyword('\]',pf.Str('$$'))
    #     elem.text = 'RI:'+elem.text 
    # if isinstance(elem, pf.Para):
    #     elem.replace_keyword('\[',pf.Str('$$'))
    #     elem.replace_keyword('\]',pf.Str('$$'))
    #     elem.content.insert(0,pf.Str('PP:'))
    #     # for b in elem.content:
    #     clen = len(elem.content)
    #     if clen==22:
    #         note = '\n'.join([str(type(b)) for b in elem.content])
    #         elem.content.insert(0,pf.Str(note))
    # 
    # if isinstance(elem, pf.Math) or isinstance(elem, pf.Str):
    #     # not working???
    # # if hasattr(elem,'text'):
    #     elem.text = elem.text.replace('[','(((')
    #     elem.text = elem.text.replace(']',')))')
    #     if isinstance(elem, pf.Math):
    #         elem.text = 'MATH:'+elem.text
    #     if isinstance(elem, pf.Str):
    #         # elem.text = '-'+elem.text
    #         pass
    #     # elem.text = 'QQQQQQQQQQQQQQQQQ'
    return elem

def no_cite_fn(elem,doc, rep_msg=None):
    if isinstance(elem,pf.Citation):
        # can't seem to replace citations with different classes ... 
        return []
    if isinstance(elem, pf.Cite):
        'might get false positive on @import ... '
        # elem.args = '???'
        return replace_or_not(rep_msg)
    
    # \\cite{[\w]+}
    no_tex_cite = genfn_delete_between_marks("\\\(cite|ref)","}", rep_msg)
    return no_tex_cite(elem,doc)
    
# no_todo = genfn_delete_between_marks("!!!!","\n",'<todo delete>')
# no_comment = genfn_delete_between_marks("<!--","-->",'<comment deleted>')
# no_equations = genfn_delete_between_marks("$$","$$",'eq')

#%%
def frontload_all_yaml(elem,doc):
    if isinstance(elem, pf.MetaBlocks):
        doc.content.insert(0, pf.Para(pf.Str('TOP OF THE WORLD')))
    
def finalize(doc):
    # doc.content.insert(0, pf.Para(pf.Str('TOP OF THE WORLD')))
    # simply repastes metadata as YAML again
    # meta = doc.get_metadata()
    # meta_str = '\n'.join([f'{k}: {str(v)}' for k,v in meta.items()])
    # meta_str = f"---\n{meta_str}\n---"
    # doc.content.insert(0,pf.RawBlock(meta_str))
    pass
    
    
#%%
def main(doc=None):
    use_rep_msg = False
    to_audio = True
    is_hyper_focused = True
    do_standardize_eq = True
    
    cmt_rep_msg  = '<comment deleted>' if use_rep_msg else None
    todo_rep_msg = '<todo deleted>'    if use_rep_msg else None
    cite_rep_msg = '<cite deleted>'    if use_rep_msg else None
    eq_rep_msg   = '<eq deleted>'      if use_rep_msg else None
    
    no_comment  = genfn_delete_between_marks("<!--","-->", cmt_rep_msg)
    no_todo     = genfn_delete_between_marks("!!!!","\n",  todo_rep_msg)
    no_cite     = lambda e,d: no_cite_fn(e,d, cite_rep_msg)
    no_equations= lambda e,d: no_equations_fn(e,d, eq_rep_msg)
    # no_img = genfn_delete_between_marks('<img src=','/>')
    # no_collapse = genfn_delete_between_marks('<details>','</details>')
        
    #probably have to escape these ... 
    # [('<style>','</style>'),
    #     ('---','---'),
    #     ('[\^*]:','\n'), #doesnt work yet
         # ('- [','\n'),
        # (']:','\n','foot?')
        # ('![](',')','figure'),
    focus_delims =[('==','=='),
                   ('!!!!','\n'),
                   ('<details>','</details>'), #no collapsible sections 
                   ('@ import','"'),]
            
    audio_delims = [('<img src="https://latex','/>','X'), #replaces rendered latex with 'X'
                    ('<img','/>','<image>'),
                    ('<style>','</style>'), #no css 
                    ('<a','/a>'), #no section labels
                    ]
                    # ('<p ','>'),
                    # ('>< ','/p>'),] #aligned paragraphs 
    
    # focus_funs = []
    # audio_funs = []
    focus_funs = [no_todo, no_comment]+gather_delim_fns(focus_delims)
    audio_funs = [speak_header, no_cite]+gather_delim_fns(audio_delims)
    
    funs = []
    if do_standardize_eq:
        funs += [standardize_equation_delims]
        
    funs += focus_funs

    if to_audio:
        funs += audio_funs
    if is_hyper_focused:
        funs += [no_cite]
    
    # pf.run_filters(funs,      doc=doc, prepare=prepare)
    pf.run_filter(standardize_equation_delims,      doc=doc, prepare=prepare)
    
    # null function
    # pf.run_filter(lambda e,d: e, doc=doc, prepare=prepare)

    # no_tex_cite = genfn_delete_between_marks("\\\cite{","}", cite_rep_msg)
    # pf.run_filter(no_tex_cite, doc=doc, prepare=prepare) #, replace_with = rep_msg)
    # pf.toJSONFilter(comment, prepare=prepare)
    
    return

if __name__ == "__main__":
    main()
# #%%

# #%%
# if __name__ == "__main__":
#     main()