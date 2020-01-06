
.. _class_repos:

Class GitHub Repository
=======================

All of the files that you may need to access for this class will be pushed
to the GitHub repository `amath585w2020
<https://github.com/rjleveque/amath585w2020>`_.

Git is a version control system that you might want to use for your own
work. You are encouraged to do so!  There's a list of some useful
resources at the bottom of this page.

But for the purpose of this class it
will primarily be used as an easy way to distribute materials, and you don't
necessarily need to know much more than what's on this page to use it.  


If you're not familiar with Git and/or do not have it installed on your
laptop, see `Set Up Git <https://help.github.com/articles/set-up-git/>`_ on
GitHub.  Note that GitHub is being used to host the public class repository, but
you do not need a GitHub account to clone the repository.

However, you do need Git installed for the commands below to work!

To clone this repository::

    git clone https://github.com/rjleveque/amath585w2020.git

This will create a directory `amath585w2020`.  

AM585 environment variable
--------------------------

I suggest you define an environment variable `AM585` that points to this
repository, e.g. in the bash shell::

    export AM585=/full/path/to/amath585w2020

You can put this command in the file `~/.bashrc` if you want it to be
executed every time you open a new shell.  

Then you can do, e.g. ::

    cd $AM585

to change directories to the class repository.

Below and elsewhere in these notes, `$AM585` will be used to refer to the
full path to the class repository.

To update
---------

If new files have been added to the class repository, you can get them by
doing::

    cd $AM585
    git pull

Your copy of these files
------------------------

To avoid having to worry about
**conflicts** if you change a file and the same file changes in the repository,
I suggest that you never modify the files in this directory.  Instead, 
create another directory for doing your own work, e.g. ::

    cd
    mkdir my585
    export MY585=/full/path/to/my585

Then copy any files you need to this directory before working with them, e.g. ::

    cp -r $AM585/homeworks/hw1  $MY585/

will recursively copy the directory `hw1`.

Then modify the files in the new `hw1` directory.

Once you have done the homework and want to submit files, this will be done using the Canvas Dropbox as indicated in the homework.

Other git references
--------------------

There are many tutorials and other sources of information available for Git.
In particular, see:

- `Software Carpentry lessons
  <http://swcarpentry.github.io//git-novice/index.html>`_
- `<https://www.atlassian.com/git/tutorials/>`_
- `<https://try.github.io/>`_ walks you through some basics.
- `Set Up Git <https://help.github.com/articles/set-up-git/>`_ from GitHub
  includes information on how to install git.
- `Git cheat sheet
  <https://education.github.com/git-cheat-sheet-education.pdf>`_
- `Some other resources
  <https://help.github.com/articles/good-resources-for-learning-git-and-github/>`_
- `Pro Git book <http://git-scm.com/doc>`_
- Try googling "git tutorial" or a particular command such as "git pull".
- Once you have git installed, type e.g. `git help pull` in a shell.
- See also `GitHub Desktop <https://desktop.github.com/>`_ if you're looking
  for an app to make it easier to interact with GitHub.

