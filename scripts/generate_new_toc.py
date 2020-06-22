#! /usr/bin/env python3

import sys
import os
import glob
from string import Template
import shutil

shutil.rmtree('_tmp', ignore_errors=True)
os.mkdir('_tmp')

def use_nested():
    return sys.platform is not 'win32'

def fix(path):
    if use_nested():
        return path
    else:
        newpath = '__'.join(path.split(os.sep)[1:])
        shutil.copy(path, os.sep.join(('_tmp', newpath)))
        return newpath

def tmpify(path):
    if use_nested():
        return path
    else:
        return os.sep.join(('_tmp', path))

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
with open(tmpify('_config.yml'), 'w') as outfile:
    outfile.write(template.substitute(logopath=fix(os.sep.join(("notebooks",
                                                                "images",
                                                                "logo",
                                                                "logo.png")))))

### Set up table of contents

chapter = Template("""- title: ${title}
  file: ${path}
""")
section = Template("""  - title: ${title}
    file: ${path}
""")
subsection = Template("""    - title: ${title}
      file: ${path}
""")

leveltext = [None, chapter, section, subsection]


for root, dirs, files in os.walk(os.sep.join(("notebooks",
                                              "images"))):
    for file in files:
        fix(os.sep.join((root, file)))

skiplist= [os.sep.join(('notebooks','images')),]


oldlevel = 1

with open(tmpify('_toc.yml'), 'w') as outfile:

    ## scan the files in the directories

    outfile.write(chapter.substitute(path=fix(os.sep.join(('notebooks',
                                                    'intro.md'))),
                                     title='Home'))

    for root, dirs, files in os.walk('notebooks'):
        if root == 'notebooks':
            ## Skip the base level
            continue
        for dir in dirs:
            if dir.startswith('.'):
                skiplist.append(os.sep.join((root, dir)))
        if root.startswith(tuple(skiplist)):
            continue
        
        for file in files:
            name, ext = os.path.splitext(file)
            filepath = os.sep.join((root, file))
            level = filepath.count(os.sep)
            if ext in ('.md',):
                title = root.split(os.sep)[-1].capitalize()
                outfile.write(leveltext[level-1].substitute(path=fix(filepath),
                                                          title=title))
                outfile.write("  "*(level-1)+'sections:\n')
            if ext in ('.ipynb',):
                title = name.replace('_', ' ').capitalize()

                outfile.write(leveltext[level].substitute(path=fix(filepath),
                                                          title=title))


    fix('genindex.rst')
    outfile.write(chapter.substitute(path='genindex.rst',
                                     title='Index'))
