#! /usr/bin/env python3

import os
import glob
from string import Template

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

with open('_data/toc.yml', 'w') as outfile:
    outfile.write(template)
    dirs = {'maths':'Mathematics',
            'python':'Python'}
    
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
