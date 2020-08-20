import os
import json
from string import Template

from generate_new_toc import fix


def add_module_badges(fpath):
    """ Looks through all markdown cells in a given notebook for
    those tagged with a module-tag. If found, it adds the module
    badges below the header and appends the {doc} directive to
    that notebook to the modules_dict.

    """

    # Fix fpath for badges, remove _tmp
    new_fpath = '.' + fpath.split('_tmp')[-1]

    with open(fpath, 'r+') as f:
        nb = json.load(f)

    file_changed = False
    for cell in nb['cells']:

        ind_header = None
        if cell['cell_type'] == 'markdown':
            for i, line in enumerate(cell['source']):

                # find the first header in the cell, under which we will add badges
                _header = line.split("#")
                if ind_header is None and len(_header) > 1:
                    ind_header = i
                    header = _header[-1]

                # remove any previous module badges
                if '<!-- module-' in line:
                    del cell['source'][i]
                    file_changed = True
                    continue

            _module_tags = []
            try:
                tags = cell['metadata']['tags']
                for tag in tags:
                    if "module-" in tag and tag in modules_dict:
                        _module_tags.append(tag)

                # single line cells don't have \n at the end
                if len(_module_tags) > 0:
                    if '\n' not in cell['source'][ind_header]:
                        cell['source'][ind_header] += '\n'

                    # badges and {doc} links to notebook
                    tags_string = ''
                    for tag in _module_tags:
                        _ref = "{doc}" + f"`{header.strip()} <{new_fpath}>`"
                        modules_dict[tag] += [_ref]
                        tags_string += modules_dict[tag][1] + ' '
                    tags_string += '\n'

                    # add badges to the cell content
                    cell['source'].insert(ind_header + 1, tags_string)
                    file_changed = True

                    print(f"Added {len(_module_tags)} badges to {fpath}")

            except KeyError:
                continue

            if file_changed:
                with open(fpath, 'w') as f:
                    json.dump(nb, f)


def write_module_content():
    """ Writes the values in modules_dict dictionary into the
    second cell of modules.ipynb. Creates a ## header based on
    module name and lists links to notebooks containing cells with
    a corresponding module-tag.

    """

    content = []
    for year in modules_year.keys():
        content += [f'## {year}\n']

        for tag in modules_dict.keys():
            if tag in modules_year[year] and len(modules_dict[tag]) > 2:

                # create target header and badge (first two entries of modules_dict)
                content += [f'({tag})=\n', f'### {modules_dict[tag][0]}\n', '\n', f'{modules_dict[tag][1]}\n', '\n']

                for line in modules_dict[tag][2:]:
                    content += ['- ' + line + '\n']
                content += ['\n']

    with open(modules_path, 'r+') as f:
        nb = json.load(f)

    # write content in the second cell
    nb['cells'][1]['source'] = content
    with open(modules_path, 'w') as f:
        json.dump(nb, f)


modules_path = os.sep.join(('_tmp',
                            fix('notebooks/a_modules/intro.ipynb', copy=False)))

modules_dict = {'module-mm1': ['Maths Methods 1'],
               'module-mm2': ['Maths Methods 2'],
               'module-mse1': ['Maths for Scientists and Engineers 1'],
               'module-mse2': ['Maths for Scientists and Engineers 2'],
               'module-geoinv': ['Geophysical Inversion'],
               'module-dynep': ['Dynamic Earth and Planets'],
               'module-progr': ['Programming for Geoscientists'],
               'module-nm': ['Numerical Methods'],
               'module-rs': ['Remote Sensing'],
               'module-mech': ['Mechanics'],
               'module-advrs': ['Advanced Remote Sensing'],
               'module-seism': ['Seismology'],
               'module-igp': ['Independent Geophysics Project'],
               'module-fieldgps': ['Field Geophysics'],
               'module-gmod': ['Grav., Magn. and Orbital Dynamics'],
               'module-geodyn': ['Geodynamics']}

modules_year = {'Year 1': ['module-mm1', 'module-mm2', 'module-progr', 'module-dynep'],
                'Year 2': ['module-mse1', 'module-mse2', 'module-nm', 'module-rs',
                           'module-seism', 'module-mech', 'module-fieldgps'],
                'Year 3/4': ['module-geoinv', 'module-advrs', 'module-igp', 'module-gmod', 'module-geodyn']}

# module badge buttons, with a {ref}-type link to its header in modules/intro.ipynb
badge = Template("[<!-- ${module_tag} badge --><span class=\"module ${module_tag}\">${module_name}</span>](${module_tag})")

# add badges code to dictionary
for key in modules_dict:
    modules_dict[key] += [badge.substitute(module_tag=key, module_name=modules_dict[key][0])]

for root, dirs, files in os.walk('notebooks'):

    for intro in ['intro.md', 'intro.ipynb']:
        if intro in files:

            files.remove(intro)
            for file in files:
                _, ext = os.path.splitext(file)
                if ext == '.ipynb':
                    filepath = os.sep.join((root, file))
                    print(filepath, fix(filepath))
                    add_module_badges(os.sep.join(('_tmp',
                                                   fix(filepath, copy=False))))
            break

write_module_content()
