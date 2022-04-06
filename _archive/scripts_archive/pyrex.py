import re
import sys
is_verbose = True

'''
PYthon RegEX 
applies regex to files using python
'''
#%%
# try things out interactively here: https://regex101.com/
# regex = r'(?<!\n)\n(\w)'
# subst = r' \1'


#%%
def apply_pyrex(regex,subst, fnin, fnout=None, do_ignore_yaml=True):
    test_str = 'error, file not loaded'
    # test_str = '''
    # Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
    # incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    # nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
    # fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    # culpa qui officia deserunt mollit anim id est laborum.
    # 
    # Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    # 
    # Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
    # incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    # nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
    # fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    # culpa qui officia deserunt mollit anim id est laborum.
    # '''

    if fnin is None:
        str_in = test_str
    else:
        with open(fnin,'r') as f:
            str_in = f.read()
    if fnout is None:
        fnout = 'out.md'


    str_yaml = ''
    if do_ignore_yaml:
        yaml_split = str_in.split('---')
        str_yaml = '---'+''.join(yaml_split[:2])+'---'
        str_in ='\n'.join(yaml_split[2:])



    #%%
    # do the find and replace, matching 
    result = re.sub(regex, subst, str_in, 0, re.MULTILINE)
    matches = re.findall(regex,str_in)

    #%%
    if do_ignore_yaml:
        result = str_yaml + result
    #%%

    if result:
        # print(result)
        print('done!\n')
    else:
        print('no matches - no result')
        
    with open(fnout,'w+') as f:
        f.write(result)

    if is_verbose:
        print(f'reg:{regex}, sub:{subst}')
        # print(f'in:{fnin}, out:{fnout}')
        print(matches)
# 

#%%
if __name__ == "__main__":
    fnin = None
    fnout = None

    do_ignore_yaml = True 

    regex = r'\w'
    subst = r'\1'
    # python pryex `regex` `subst` `fnin` `fnout`

    if len(sys.argv)>1:
        # regex = re.escape(sys.argv[1])
        regex = sys.argv[1]

    if len(sys.argv)>2:
        subst = sys.argv[2]

    if len(sys.argv)>3:
        fnin = sys.argv[3]

    if len(sys.argv)>4:
        fnout = sys.argv[4]
    
    apply_pyrex(regex,subst, fnin, fnout, do_ignore_yaml)