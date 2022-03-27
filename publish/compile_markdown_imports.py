import re
import os
# import glob

def f2str(fn):
    with open(fn,'r') as f:
        return f.read()

'''
TURN INTO COMMANDLINE SCRIPT
wrap in function
fix relative paths
'''
def find_in_subdir(name, path):
    print(os.getcwd())
    print(f' finding {name} in {path} .')
    for root, dirs, files in os.walk(path):
        # print(files)
        if name in files:
            print('found')
            return os.path.join(root, name)
        else:
            raise Exception(f'ERROR, cant find {name} in {path}')
    raise Exception('path contains no dirs')


def f2str_in_subdir(fn, start_dir='./'):
    fn = find_in_subdir(fn, start_dir)
    return f2str(fn)

def compile_markdown_imports(fnin,fnout=None, basedir='',is_recurse=False):        
    if fnout is None:
        fnout = fnin.replace('.md','_out.md')
    
    def import_str_to_file(imp_str):
        is_import = re.search('@import "(.*)"', imp_str)
        if is_import:
            file_to_import = is_import.group(1)
            return file_to_import
        else:
            return None

    fninin = fnin
    fnin = find_in_subdir(fnin, basedir)
    fnout = os.path.join(basedir,fnout) #write all output to basedir
    
    
    with open(fnin,'r') as f:
        with open(fnout,'w') as fo:
            lines = f.readlines()
            for L in lines:
                file_to_import = import_str_to_file(L)
                if file_to_import is not None:
                    print('importing:',file_to_import)
                    # write comment describing where content came from
                    L = L.replace('@import','imported from').rstrip('\n')
                    L = f'<!--{L}-->\n'

                    basedir = basedir.rstrip('/')+'/'
                    full_file_to_import =  basedir+file_to_import.lstrip('/')
                    file_tail = full_file_to_import.rsplit('/',1)[1]
                    
                    # print(f'import_str: from {full_file_to_import}')
                    import_str = f2str(full_file_to_import)
                    
                    if '@import' in import_str:
                        print(f'\n\nRECURSIVE IMPORT -- {full_file_to_import} --')
                        relative_dir = file_to_import.rsplit('/',1)[0]+'/'
                        full_relative_dir = basedir+relative_dir
                        import_str = compile_markdown_imports(fnin=file_tail,basedir=full_relative_dir,is_recurse=True)

                    L += import_str+f'\n<!-- end of import from "{file_tail}" -->\n'    
                    print('success')
                fo.write(L)
    with open(fnout,'r') as fo:        
        return fo.read()
#%%
compile_markdown_imports('manuscript_v0.md',basedir='./'); 
