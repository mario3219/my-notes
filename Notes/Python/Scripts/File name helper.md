```
import os
import argparse

def replace(path, substring, newstring):
    files = [p for p in os.listdir(path) if substring in p]
    for file in files:
        string_parts = file.split(substring)
        left = string_parts[0]
        right = string_parts[-1]
        os.rename(os.path.join(path,file),os.path.join(path,left+newstring+right))
    print('Done')

def append(path, substring):
    files = [p for p in os.listdir(path)]
    for file in files:
        os.rename(
                os.path.join(path,file),
                os.path.join(path,file+substring)
                )
    print('Done')

def main(**args):
    if args['replace']:
        replace(path=args['path'],
                substring=args['substring'],
                newstring=args['newstring']
                )
    if args['append']:
        append(path=args['path'],
               substring=args['substring']
               )

if __name__=='__main__':
    parser = argparse.ArgumentParser(
            description="Replaces substrings from all contents in a directory"
            )
    #General arguments
    parser.add_argument('--path', type=str,default='',help='Absolute path to directory')
    parser.add_argument('--substring',type=str,default='',help='Substring')
    parser.add_argument('--newstring',type=str,default='',help='New substring')
    #Function calls
    parser.add_argument('--replace',action='store_true',default=False,help='Runs replace substring')
    parser.add_argument('--append',action='store_true',default=False,help='Appends substring to all files in path')
    args = vars(parser.parse_args())
    main(**args)

```