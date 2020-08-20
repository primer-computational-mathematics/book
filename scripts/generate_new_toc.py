#! /usr/bin/env python3
import sys
import os
from string import Template
import shutil
from natsort import natsorted

# remove any previous attempts
if os.path.isdir('_tmp'):
    shutil.rmtree('_tmp')
os.mkdir('_tmp')
shutil.copytree(os.sep.join(('notebooks','images')),
                os.sep.join(('_tmp','images')))
shutil.copytree('_static', os.sep.join(('_tmp', '_static')))

skiplist = [os.sep.join(('notebooks', 'images'))]

def use_nested():
    return sys.platform != 'win32'

def fix(path, copy=True):
    if use_nested():
        newpath = path.replace('notebooks'+os.sep, '', 1)
    else:
        newpath = '__'.join(path.split(os.sep)[1:])
    if copy:
        os.makedirs(os.sep.join(('_tmp', os.path.dirname(newpath))),
                exist_ok=True)
        shutil.copy(path, os.sep.join(('_tmp', newpath)))
    return newpath

def change_path(root, base):
    if use_nested():
        print(root.replace('notebooks', base, 1))
        print(root.replace(root.rsplit(os.sep, 1)[0],
                            base, 1))
        return root.replace('notebooks', base, 1)
    else:
        return root.replace(root.rsplit(os.sep, 1)[0],
                            base, 1)

### quick and dirty argument parsing
def argv_or_default(key, default):
    try:
        return sys.argv[key]
    except IndexError:
        return default
baseurl = argv_or_default(1, '')
url = argv_or_default(2, '')

### Set up _config.yml
with open('_newconfig.yml.in', 'r') as template_file:
    template = Template(template_file.read())
with open('_tmp'+os.sep+'_config.yml', 'w') as outfile:
    outfile.write(template.substitute(logopath=fix(os.sep.join(("notebooks",
                                                                "images",
                                                                "logo",
                                                                "logo.png")))))

### Set up table of contents

chapter = Template("- file: ${path}\n")
section = Template("  - file: ${path}\n")
subsection = Template("    - file: ${path}\n")
leveltext = [None, chapter, section, subsection]

with open('_tmp'+os.sep+'_toc.yml', 'w') as outfile:

    outfile.write("- file: " + fix(os.sep.join(('notebooks', 'intro.md'))) + "\n")

    for root, dirs, files in os.walk('notebooks'):

        dirs = natsorted(dirs)
        if root == 'notebooks':
            # Skip the base level
            continue

        for _dir in dirs:
            if _dir.startswith('.'):
                skiplist.append(os.sep.join((root, _dir)))

        if root.startswith(tuple(skiplist)):
            print('Not copying ', root)
            continue

        exts = set(os.path.splitext(file)[1] for file in files)
        if ('.ipynb' and '.md') not in exts:
            try:
                shutil.copytree(root, change_path(root, '_tmp'))
                shutil.copytree(root, change_path(root, os.sep.join(('_tmp',
                                                                    '_build',
                                                                    'html'))))
            except FileExistsError:
                pass

        for intro in ['intro.md', 'intro.ipynb']:
            if intro in files:
                filepath = os.sep.join((root, intro))
                level = filepath.count(os.sep)

                outfile.write(leveltext[level - 1].substitute(path=fix(filepath)))
                outfile.write("  " * (level - 1) + 'sections:\n')

                files.remove(intro)
                for file in natsorted(files):
                    _, ext = os.path.splitext(file)
                    filepath = os.sep.join((root, file))
                    level = filepath.count(os.sep)
                    if ext in ('.ipynb',):
                        outfile.write(leveltext[level].substitute(path=fix(filepath)))
                break

    fix('genindex.rst')
    outfile.write("- title: \"Index\"\n  file: genindex.rst\n")
