#! /usr/bin/env python3

import sys
import os
import glob
from string import Template

### quick and dirty argument parsing
def argv_or_default(key, default):
    try:
        return sys.argv[key]
    except IndexError:
        return default
baseurl = argv_or_default(1, '')
url = argv_or_default(2, '')

### Set up _config.yml

with open('_config.yml.in', 'r') as template_file:
    template = Template(template_file.read())
with open('_config.yml', 'w') as outfile:
    outfile.write(template.substitute(baseurl=baseurl,
                                      url=url))

### Set up table of contents

with open('_data/toc.yml.in', 'r') as template_file:
    template = template_file.read()

chapter = Template("""- title: ${title}
  url: /${dir}/intro
  not_numbered: true
  expand_sections: true
""")
section = Template("""  - title: ${sec_title}
    url: /${dir}/${name}
    not_numbered: true
""")


dirs = {'maths':'Mathematics',
        'coding':'Coding',
        'geosciences': 'Geosciences'}

with open('_data/toc.yml', 'w') as outfile:
    outfile.write(template)

    ## scan the files in the directories
    
    for dir, title in dirs.items():
        outfile.write(chapter.substitute(dir=dir,
                                         title=title))
        notebooks = glob.glob(os.path.join('./notebooks', dir, '*.ipynb'))
        if notebooks:
            outfile.write("  sections:\n")
        for notebook in notebooks:
            name = os.path.basename(notebook).rsplit('.', 1)[0]
            sec_title = name.replace('_', ' ')
            outfile.write(section.substitute(sec_title=sec_title,
                                             dir=dir,
                                             name=name))
