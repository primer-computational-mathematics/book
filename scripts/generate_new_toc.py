#! /usr/bin/env python3
import sys
import os
from string import Template
import shutil

# remove any previous attempts
if os.path.isdir('_tmp'):
    shutil.rmtree('_tmp')
os.mkdir('_tmp')
shutil.copytree(os.sep.join(('notebooks','images')),
                os.sep.join(('_tmp','images')))

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

chapter = Template("""- file: ${path}
""")
section = Template("""  - file: ${path}
""")
subsection = Template("""    - file: ${path}
""")

leveltext = [None, chapter, section, subsection]

with open('_tmp'+os.sep+'_toc.yml', 'w') as outfile:

    outfile.write("- file: " + fix(os.sep.join(('notebooks', 'intro.md'))) + "\n")

    for root, dirs, files in os.walk('notebooks'):
        if root == 'notebooks':
            # Skip the base level
            continue

        if ('intro.md' or 'intro.ipynb') not in files:
            print('Skipped directory', root)
            continue

        exts = set(os.path.splitext(file)[1] for file in files)
        if ('.ipynb' not in exts and
            '.md' not in exts):
            shutil.copytree(root, change_path(root, '_tmp'))
            shutil.copytree(root, change_path(root,
                                              os.sep.join(('_tmp',
                                                           '_build',
                                                           'html'))))

        for intro in ['intro.md', 'intro.ipynb']:
            if intro in files:
                filepath = os.sep.join((root, intro))
                level = filepath.count(os.sep)

                outfile.write(leveltext[level - 1].substitute(path=fix(filepath)))
                outfile.write("  " * (level - 1) + 'sections:\n')

        for file in sorted(files, key=str.lower):
            name, ext = os.path.splitext(file)
            filepath = os.sep.join((root, file))
            level = filepath.count(os.sep)
            if ext in ('.ipynb',):
                outfile.write(leveltext[level].substitute(path=fix(filepath)))

    # Index
    outfile.write("""- title: \"Index\"\n  file: genindex.rst\n""")
