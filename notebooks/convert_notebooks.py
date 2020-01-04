
"""
Convert a set of notebooks to html files for posting on the website.
"""

import os,sys,glob,re

    
def make_html(notebooks='all', run_notebooks=True, html_dir='build_html'):

    os.system('mkdir -p %s' % html_dir)

    if notebooks == 'all':
        notebook_files = glob.glob('*.ipynb')
        notebooks = [os.path.splitext(f)[0] for f in notebook_files]
    
    notebook_files = [f+'.ipynb' for f in notebooks]

    print('notebook_files = ', notebook_files)
    print('notebooks = ', notebooks)

    for file in notebook_files:
        os.system('cp %s %s/' % (file, html_dir))

    os.chdir(html_dir)

    if run_notebooks:
        for file in notebook_files:
            fname = os.path.splitext(file)[0]
            print('converting %s' % file)
            cmd = 'jupyter nbconvert --to html  --execute ' + \
                  '--ExecutePreprocessor.kernel_name=python3 ' +\
                  '--ExecutePreprocessor.timeout=-1  %s' % file
            print(cmd)
            os.system(cmd)


    html_files = [fname + '.html' for fname in notebooks]
    print('html_files = ', html_files)

    # fix cross reference links:
    for file in html_files:
        infile = open(file,'r')
        lines = infile.readlines()
        infile.close()
        print('Fixing %s' % file)
        with open(file,'w') as outfile:
            for line in lines:
                #for notebook_name in notebooks:
                #    line = re.sub(notebook_name+'.ipynb', notebook_name+'.html', line)
                line = re.sub('.ipynb', '.html', line)
                outfile.write(line)

    # remove the notebooks from html_dir
    os.system('rm *.ipynb')

    # go back to the main directory:
    os.chdir('..')

    print("The html files can be found in %s" % html_dir)

if __name__ == '__main__':
    
    make_html('all')
