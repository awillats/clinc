import sys

'''
put the yaml block from the top of one file at the top of the other 
'''


#%%

#replace with getopt
# print(sys.argv)
src = 'testin.md'
targ = 'testout.md'

if len(sys.argv)>1: src = sys.argv[1]
if len(sys.argv)>2: targ = sys.argv[2]


def transplant_yaml(src,targ):
    with open(src,'r') as fsrc:
        
        content = fsrc.read()
        '''
        pastes the first yaml block, even if its not at the beginning of the source...
        '''
        sections = content.split('---')
        # print(sections[0])
        yaml_block = sections[1]
        yaml_block = f'---{yaml_block}---\n'
        if yaml_block:
            with open(targ,'r+') as ftarg:
                targcontent = ftarg.read()
                ftarg.seek(0)
                ftarg.write(yaml_block+targcontent)

if len(sys.argv)>0:
    transplant_yaml(src,targ)