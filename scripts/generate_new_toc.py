#! /usr/bin/env python3

import sys
import os
import glob
from string import Template
import shutil
import io
from nbformat import read
import re


def nb_title(fname):
    with io.open(fname, 'r', encoding='utf-8') as f:
        nb = read(f, 4)

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            title = re.search("# (.*?)\n", cell['source'])\

            if title is not None:
                title = title.group().split("#")[-1].strip()
                return title


# remove any previous attempts
if os.path.isdir('_tmp'):
    shutil.rmtree('_tmp')
os.mkdir('_tmp')
shutil.copytree(os.sep.join(('notebooks','images')),
                os.sep.join(('_tmp','images')))
skiplist= [os.sep.join(('notebooks','images')),]

def use_nested():
    return sys.platform != 'win32'

def fix(path):
    if use_nested():
        newpath = path.replace('notebooks'+os.sep, '', 1)
    else:
        newpath = '__'.join(path.split(os.sep)[1:])
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

chapter = Template("""- title: "${title}"
  file: ${path}
""")
section = Template("""  - title: "${title}"
    file: ${path}
""")
subsection = Template("""    - title: "${title}"
      file: ${path}
""")

leveltext = [None, chapter, section, subsection]


oldlevel = 1

with open('_tmp'+os.sep+'_toc.yml', 'w') as outfile:

    ## scan the files in the directories

    outfile.write(chapter.substitute(path=fix(os.sep.join(('notebooks',
                                                    'intro.md'))),
                                     title='Home'))

    for root, dirs, files in os.walk('notebooks'):
        if root == 'notebooks':
            ## Skip the base level
            continue

        for dir in dirs:
            if dir.startswith('.') or not (os.path.isfile(os.sep.join((root, dir, "intro.md"))) or os.path.isfile(os.sep.join((root, dir, "intro.ipynb")))):
                skiplist.append(os.sep.join((root, dir)))
        if root.startswith(tuple(skiplist)):
            continue

        exts = set(os.path.splitext(file)[1] for file in files)
        if ('.ipynb' not in exts and
            '.md' not in exts):
            shutil.copytree(root, change_path(root, '_tmp'))
            shutil.copytree(root, change_path(root,
                                              os.sep.join(('_tmp',
                                                           '_build',
                                                           'html'))))
        title = root.split(os.sep)[-1].title().replace('_', ' ')
        if 'intro.md' in files:
            filepath = os.sep.join((root, 'intro.md'))
            level = filepath.count(os.sep)
            
            outfile.write(leveltext[level-1].substitute(path=fix(filepath),
                                                          title=title))
            outfile.write("  "*(level-1)+'sections:\n')
        elif 'intro.ipynb' in files:
            filepath = os.sep.join((root, 'intro.ipynb'))
            level = filepath.count(os.sep)
            
            outfile.write(leveltext[level-1].substitute(path=fix(filepath),
                                                          title=title))
            outfile.write("  "*(level-1)+'sections:\n')
        
        for file in files:
            name, ext = os.path.splitext(file)
            filepath = os.sep.join((root, file))
            level = filepath.count(os.sep)
            if ext in ('.ipynb',):
                title = nb_title(filepath)
                if title is None:
                    title = name.replace('_', ' ').title()

                outfile.write(leveltext[level].substitute(path=fix(filepath),
                                                          title=title))


    fix('genindex.rst')
    outfile.write(chapter.substitute(path='genindex.rst',
                                     title='Index'))

print('_toc.yml generated. Directories skipped: ')
[print(i, directory) for i, directory in enumerate(skiplist, 1)]
