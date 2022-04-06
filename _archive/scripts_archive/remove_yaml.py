import sys

'''
put the yaml block from the top of one file at the top of the other 
'''


#%%
def remove_yaml(src,targ=None):
    if targ is None:
        targ = src 
        
    with open(src,'r') as fsrc:
        
        content = fsrc.read()
        '''
        pastes the first yaml block, even if its not at the beginning of the source...
        '''
        sections = content.split('---')
        # print(sections[0])
        
        if len(sections) > 2:
            yaml_block = sections[1]
            yaml_block = f'---{yaml_block}---\n'
            src_content = ''.join(sections[2:])
        else:
            print('no yaml to remove!')
            src_content = content
        src_content = src_content.lstrip('\n')
        # print(sections)
        
    with open(targ,'w') as ftarg:
        # targcontent = ftarg.read()
        ftarg.seek(0)
        ftarg.write(src_content)

if __name__ == "__main__":
    #replace with getopt
    # print(sys.argv)
    # src = 'testin.md'
    # targ = 'testout.md'
    # print(sys.argv)
    src = None
    targ = None
    if len(sys.argv)>0:
        if len(sys.argv)>1: src = sys.argv[1]
        if len(sys.argv)>2: 
            targ = sys.argv[2]
            
    remove_yaml(src,targ)