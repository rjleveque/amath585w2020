"""
Run all the notebooks (or a subset as specified below) and convert
to html.  Then do some post-processing to fix cross references to
other notebooks so they link to the .html rather than the .ipynb file.
Other post-processing could be added to convert_notebooks.py.

The resulting html files are all saved in the build_html directory.
Move them to the html directory, commit, and push to github to get them to
appear online, with the Index at
   https://rjleveque.github.io/amath585w2020/notebooks/html/Index.html

Note: this works because "github pages" is turned on for this repository,
  https://pages.github.com/
"""

import os,sys,glob,re

from convert_notebooks import make_html

run_notebooks = True   # if False, only fix existing html files

if 1:
    # all notebooks in this directory:
    notebook_files = glob.glob('*.ipynb')
    notebooks = [os.path.splitext(f)[0] for f in notebook_files]

    # filter out those not mentioned in the Index, if desired:
    index_file = open('Index.ipynb').read()
    notebooks = ['Index'] + \
                [f for f in notebooks if f+'.ipynb' in index_file]

if 0:
    # test or remake one notebook:
    notebooks = ['Index', 'Advection']

if 'Debugging_hints' in notebooks:
    # this one intentionally fails, so need to make html by hand
    print('Removing Debugging_hints.ipynb -- create html from notebook')
    notebooks.remove('Debugging_hints')
    
make_html(notebooks, run_notebooks=run_notebooks)
