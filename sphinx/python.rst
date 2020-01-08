
.. _python:

Python and Jupyter
==================

See :ref:`codes` for links to the notebooks developed for this class.

Some general resources
-----------------------

Many other tutorials and books can be found online!

- `AMath 583 class notes (from 2014)
  <http://faculty.washington.edu/rjl/classes/am583s2014/notes/index.html#python>`_

- `The Python Tutorial <https://docs.python.org/3/tutorial/>`_

- `IPython documentation <http://ipython.org/documentation.html>`_ (with
  many other links)

- `Jupyter <http://jupyter.org/>`_

- `Jupyter Notebook documentation
  <http://jupyter-notebook.readthedocs.org/en/latest/>`_

- `A gallery of interesting Jupyter Notebooks
  <https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks>`_

Scientific Python
------------------

Numpy, Scipy, and matplotlib are the core packages for scientific Python.

- `NumPy Documentation <http://www.numpy.org/>`_ (Supports numerical arrays)

- `NumPy for Matlab users
  <https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html>`_
  (Useful list of commands, and Matlab equivalents)

- `SciPy Documentation <http://scipy.org/>`_ (Includes many other scientific
  packages, e.g. for interpolation, quadrature, etc.)

- `Matplotlib Gallery <http://matplotlib.org/gallery.html>`_ 
  (illustrating how to make various types of plots)

- See also the :ref:`biblio_python` section of the bibliography.

Many other packages are also useful, e.g.

- `SymPy <https://www.sympy.org/en/index.html>`_ (Symbolic mathematics)

- `pandas <https://pandas.pydata.org/>`_ and `xarray <http://xarray.pydata.org/en/stable/>`_ (Labelled
  arrays)

Python2 vs. Python3
-------------------

The notebooks for this class should be compatible with either Python 2.7 or 3.x.
The main difference that affects us is that in Python 3 `print` is a function
rather than a statement, e.g. ::

    print('x has the value %.6e' % x)

rather than::

    print 'x has the value %.6e' % x 

To get a code written using the print function to work in Python 2, you can
include this line at the top of the file::

    from __future__ import print_function

(with 2 underscores before and after `future`).

Installation options
---------------------

The `Anaconda Python Distribution <https://www.anaconda.com/distribution/>`_
is one easy way to get everything you need.  If you install this, you can
also then use the `conda package installer
<https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/>`_
to install various extensions easily.  

You might also want to check out `conda environments
<https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_
as a way to compartmentalize versions of Python packages for different projects.

Jupyter notebook installation
-----------------------------

If you installed
the Anaconda Python, you can insure you have jupyter and  are up to date 
via the bash commands::

    conda install jupyter
    conda update jupyter

Then in a bash shell you should be able to execute::

    jupyter notebook

to start the notebook server.  You can then navigate your browser
to the address shown when the notebook starts, e.g. ::

    http://localhost:8888/tree

If you want to easily run notebooks without installing any software, you
might try `CoCalc <https://cocalc.com/>`_ (previously known as
SageMathCloud) or `binder <http://mybinder.org>`_.  

See :ref:`codes` for more information about these services and about
running the notebooks for this class.

