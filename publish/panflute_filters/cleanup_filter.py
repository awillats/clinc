#!/usr/bin/env python
# https://github.com/sergiocorreia/panflute/blob/master/examples/panflute/comments.py
import panflute as pf
import re

# h = pf.Header(pf.Str('hi'))
# # print(h.content)
# h.content = [pf.Str('ho'),pf.Str('ho'),pf.Str('ho')]
# [print(pf.stringify(c)) for c in list(h.content)];

def name_header(elem, doc):
    if isinstance(elem, pf.Header):
        # elem.level 

        if elem.level <= 1:
            title = ''.join(list([pf.stringify(c) for c in list(elem.content)]))
            elem = pf.Para(pf.Str('SECTION: '+title))
            # +''.join(title)))
            pass
        elif elem.level >= 2:
            title = ''.join(list([pf.stringify(c) for c in list(elem.content)]))
            elem = pf.Para(pf.Str('SUBSECTION: '+title))

            # elem.content = pf.Para(pf.Str('SUBSECTION:'+title))
            pass
        else:
            pass
    return elem

"""
Pandoc filter that causes everything between
'<!-- BEGIN COMMENT -->' and '<!-- END COMMENT -->'
to be ignored.  The comment lines must appear on
lines by themselves, with blank lines surrounding
them.
"""
'''
Classes: http://scorreia.com/software/panflute/code.html#low-level-classes
Para for most text 
Header 
Emph 
RawBlock


elem.text.replace()

remove YAML with MetaBlocks ?


'''

def replace_or_not(msg=None, plaintext=False):
    if msg and plaintext: return msg 
    if msg and not plaintext: return pf.Str(msg)
    if not msg and plaintext: return ''
    if not msg and not plaintext: return
    else: return

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

def no_equations_fn(elem,doc, rep_msg=None):
    if isinstance(elem,pf.Math):
        elem = replace_or_not(rep_msg)
        return elem
    f = genfn_delete_between_marks('\[','\]',rep_msg)
    return f(elem,doc)

    
def no_cite_fn(elem,doc, rep_msg=None):
    if isinstance(elem,pf.Citation):
        # can't seem to replace citations with different classes ... 
        return []
    if isinstance(elem, pf.Cite):
        'might get false positive on @import ... '
        # elem.args = '???'
        return replace_or_not(rep_msg)
    
    # \\cite{[\w]+}
    no_tex_cite = genfn_delete_between_marks("\\\(cite|ref){","}", rep_msg)
    return no_tex_cite(elem,doc)
    
    

# no_todo = genfn_delete_between_marks("!!!!","\n",'<todo delete>')
# no_comment = genfn_delete_between_marks("<!--","-->",'<comment deleted>')
# no_equations = genfn_delete_between_marks("$$","$$",'eq')


#%%
def main(doc=None):
    use_rep_msg = False
    
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

    pf.run_filter(name_header, doc=doc)

    pf.run_filter(no_comment,   doc=doc, prepare=prepare)
    pf.run_filter(no_todo,      doc=doc, prepare=prepare)
    pf.run_filter(no_cite,      doc=doc, prepare=prepare) 
    pf.run_filter(no_equations, doc=doc, prepare=prepare)
    # pf.run_filter(no_img,       doc=doc, prepare=prepare)
    # pf.run_filter(no_collapse,  doc=doc, prepare=prepare)

    #probably have to escape these ... 
    # [('<style>','</style>'),
    #     ('---','---'),
    #     ('[\^*]:','\n'),
         # ('- [','\n'),
        # (']:','\n','foot?')
        # ('![](',')','figure'),

    delims =[ ('==','=='),
            ('<img src="https://latex','/>','X'),
            ('<img','/>','<image>'),
            ('<details>','</details>'),
            ('<style>','</style>'),
            ('<p ','/p>'),
            ('<a','/a>'),
            ('@ import','"'),]
            
            #
            
    for delim in delims:
        rep_msg = delim[2] if len(delim)>2 else None
        pf.run_filter(genfn_delete_between_marks(delim[0],delim[1],rep_msg), doc=doc,prepare=prepare)
        
    # no_tex_cite = genfn_delete_between_marks("\\\cite{","}", cite_rep_msg)
    # pf.run_filter(no_tex_cite, doc=doc, prepare=prepare) #, replace_with = rep_msg)

    
    # pf.run_filter(genfn_delete_between_marks("<details>","</details>"), doc=doc, prepare=prepare)

    # pf.run_filter(bump_header, doc=doc)
    # pf.run_filter(bump_header, doc=doc)    
    # pf.run_filter(replace_with_text, doc=doc)
    # pf.toJSONFilter(comment, prepare=prepare)
    return

if __name__ == "__main__":
    main()
# #%%

# #%%
# if __name__ == "__main__":
#     main()