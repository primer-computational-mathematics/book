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
    new_fpath = fpath.split('_tmp')[-1].split('.ipynb')[0]

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
                        modules_dict[tag].sort()
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

# modules ordered by module codes (EARTXXXXX)
modules_dict = {
    # Year 1
    'module-dynep': ['Dynamic Earth and Planets'],
    'module-strat1': ['Stratigraphy (Year 1)'],
    'module-gmat': ['Geomaterials'],
    'module-prog': ['Programming for Geoscientists'],
    'module-mfg': ['Mathematics for Geoscientists'],
    'module-mm1': ['Mathematics Methods 1'], 
    'module-cfg': ['Chemistry for Geoscientists'],
    'module-ltg': ['Low-Temperature Geochemistry'],
    'module-dte': ['Deforming the Earth'],
    'module-lodt': ['Life over Deep Time'],
    'module-gitf': ['Geology in the Field'],
    'module-phyp': ['Physical Processes'],
    'module-surp': ['Surface Processes'],
    'module-vip': ['Volcanism and Internal Processes'],
    'module-mm2': ['Mathematics Methods 2'],
    'module-exstat': ['Excel and Statistics'],
    'module-graph': ['Graphics'],
    'module-fieldsk': ['Field Skills'],
    # Year 2
    'module-ssg': ['Solar System Geoscience'],
    'module-htg': ['High-Temperature Geochemistry'], 
    'module-maps': ['Maps and Structures'],
    'module-puregp': ['Pure Geophysics'],
    'module-appgp': ['Applied Geophysics'],
    'module-rsitf': ['Rocks and Structures in the Field'],
    'module-fieldgp': ['Field Geophysics'],
    'module-igg': ['Igneous Geology'],
    'module-metg': ['Metamorphic Geology'],
    'module-sedi': ['Sediments'],
    'module-strat2': ['Stratigraphy (Year 2)'],
    'module-rsep': ['Remote Sensing Earth and Planets'],
    'module-mse1': ['Mathematics for Scientists and Engineers 1'],
    'module-mse2': ['Mathematics for Scientists and Engineers 2'], 
    'module-mech': ['Mechanics'], 
    'module-wave': ['Waves'], 
    'module-egacr': ['Environmental Geochemistry and Climate Report'], 
    'module-pala': ['Palaeontology'], 
    'module-om': ['Optical Mineralogy'],  
    'module-seis': ['Seismology'],
    'module-nm': ['Numerical Methods'],
    'module-resource': ['Earth Resources'],
    # Year 3/4
    'module-indpmap': ['Independent Project - Mapping'],
    'module-indpgp': ['Independent Project - Geophysics'],
    'module-indpes': ['Independent Project - Earth Science'], 
    'module-indpls': ['Independent Project - Landing Site'], 
    'module-ct': ['Continental Tectonics'],
    'module-clim': ['Climate'],
    'module-nssi': ['Near Surface Seismic Imaging'],
    'module-ars': ['Advanced Remote Sensing'],
    'module-iafg': ['Integrated Advanced Field Geology'],
    'module-ored': ['Ore Deposits'],
    'module-mem': ['Mining Environmental Management'],
    'module-envsemi': ['Environmental Seminar'],
    'module-astbio': ['Astrobiology'],
    'module-esys': ['Earth Systems'], 
    'module-gace': ['Geological and Coastal Engineering'],
    'module-advprog': ['Advanced Programming'],
    'module-gmod': ['Gravity, Magnetism, and Orbital Dynamics'],
    'module-psdp': ['Practical Seismic Data Processing'],
    'module-plasur': ['Planetary Surfaces'],
    'module-toto': ['Tectonics of the Ocean'],
    'module-aag': ['Advanced Applied Geophysics'],
    'module-hff': ['Hydrogeology and Fluid Flow'],
    'module-gfdocean': ['Geophysical Fluid Dynamics of the Oceans'],
    'module-mgae': ['Mining Geology and Engineering'],
    'module-cps': ['Comparative Planetary Science'],
    'module-dsml': ['Data Science and Machine Learning for Geoscientists'],
    'module-ghaz': ['Geohazards'],
    'module-ageomo': ['Applied Geomorphology'],
    'module-minep': ['Mineral Processing'],
    'module-aes': ['Advanced Exploration Seismology'],
    'module-fgamb': ['Field Geology of an Active Mountain Belt'],
    'module-ginv': ['Geophysical Inversion'],
    'module-gdyn': ['Geodynamics'],
    'module-cac': ['Collisions and Craters'],
    'module-ampap': ['Arc Magmatic Processes and Products'],
    'module-grt': ['Geological Reactive transport'],
    'module-palabio': ['Palaeobiology'],
    'module-palaocean': ['Palaeoceanography'],
    'module-gagp': ['Geophysical Analysis Group Project'],
    'module-plaphy': ['Planetary Physics'],
    'module-plachem': ['Planetary Chemistry'],
    'module-meteo': ['Meteorites']
}
            
modules_year = {
    'Year 1': ['module-dynep', 'module-strat1', 'module-gmat', 'module-prog', 'module-mfg', 
               'module-mm1', 'module-cfg', 'module-ltg', 'module-dte', 'module-lodt', 
               'module-gitf', 'module-phyp', 'module-surp', 'module-vip', 'module-mm2', 
               'module-exstat', 'module-graph', 'module-fieldsk'],
    'Year 2': ['module-ssg', 'module-htg', 'module-maps', 'module-puregp', 'module-appgp',
               'module-rsitf', 'module-fieldgp', 'module-igg', 'module-metg', 'module-sedi',
               'module-strat2', 'module-rsep', 'module-mse1', 'module-mse2', 'module-mech',
               'module-wave', 'module-egacr', 'module-pala', 'module-om', 'module-seis',
               'module-nm', 'module-resource'],
    'Year 3/4': ['module-indpmap', 'module-indpgp', 'module-indpes', 'module-indpls', 'module-ct',
               'module-clim', 'module-nssi', 'module-ars', 'module-iafg', 'module-ored',
               'module-mem', 'module-envsemi', 'module-astbio', 'module-esys', 'module-gace',
               'module-advprog', 'module-gmod', 'module-psdp', 'module-plasur', 'module-toto',
               'module-aag', 'module-hff', 'module-gfdocean', 'module-mgae', 'module-cps',
               'module-dsml', 'module-ghaz', 'module-ageomo', 'module-minep', 'module-aes',
               'module-fgamb', 'module-ginv', 'module-gdyn', 'module-cac', 'module-ampap',
               'module-grt', 'module-palabio', 'module-palaocean', 'module-gagp', 'module-plaphy',
               'module-plachem', 'module-meteo']
}

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
