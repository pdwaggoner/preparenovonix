|build| |coverage| |docs| |pypi| |zenodo| 

.. inclusion-marker-do-not-remove

Preparing Novonix Data
======================

**preparenovonix** is a Python package that handles common issues encountered in data files generated with a range of software versions from the `Novonix`_ battery-testers. This package can also add extra information that makes easier coulombic counting and relating a measurement to the experimental protocol. The package provides a master function, *prepare_novonix*, that can run at once the cleaning and adding derived information, with flexibility to choose only some features. There is a separate function to simply read a column by its given name.


Example
-------

The **example.py** runs over the given example data, producing a new file and a plot that compares the original and the prepared data. To run this
example, simply type: :code:`python example.py`.

Requirements and Installation
-----------------------------

This code has been developed in Python 3.7.1 and it is compatible with Python above 3.5 versions. The code has been tested to run in Windows, OSX and Linux operating systems. 

This code uses numpy as specified in docs/requirements.txt. The ploting routine from the *example.py* also requires the use of matplotlib.

The code can be run directly from a cloned GitHub `repository`_ or it can also be installed as a python `package`_ through pip:

.. code::

   pip install preparenovonix

The functions in the package can be used after importing novonix_add, for example as follows:

.. code-block:: python

   import preparenovonix.novonix_add as prep

The code has been tested within Matlab R2018a.

Running `preparenovonix` code from MatLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run the code from Matlab, Python will need to be installed including the packages: numpy, pathlib and preparenovonix (see details above). Ensure that Matlab can see your installation of Python by running `pyversion`_. If this is not the case then: (i) find where your Python executable is (within a python terminal you can do this by typing: `import os, sys ; os.path.dirname(sys.executable)`), (ii) type  within your MatLab interpreter `pyversion [path to python executable]` and (iii) check that now the path to Python is recognised with `pyversion`_. Make sure that 

In your code you can add the following lines that will call the master function from the package, catching exceptions: 

.. code-block:: Matlab

   try
	py.preparenovonix.novonix_prep.prepare_novonix(file_to_open,...
		pyargs('addstate','True',...
		'lprotocol','True',...
                'overwrite','True',...
                'verbose','False'));
   catch e
	e.message
        if(isa(e,'matlab.exception.PyException'))
		e.ExceptionObject
        end
   end


.. _compability:

Compatibility
-------------

This code has been tested with data generated by different versions of
the `Novonix`_ software. If you encounter issues running the code for
any version of Novonix software report an issue. Note that an example
file will be needed in order to improve the code. List of the `Novonix`_
software. If you encounter issues running the code for any version of Novonix software report an issue. Note that an example file will be needed in order to improve the code.
List of the `Novonix`_ software versions the code has been tested against:

-  3.0.2.3
-  3.0.2.1
-  TO
-  2.0.0.7
-  1.9.4.0

.. _Novonix: http://www.novonix.ca/

.. _pyversion: https://uk.mathworks.com/help/matlab/getting-started-with-python.html

.. _package: https://pypi.org/project/preparenovonix/

.. _repository: https://github.com/BatLabLancaster/preparenovonix

.. |build| image:: https://travis-ci.org/BatLabLancaster/preparenovonix.svg?branch=master
    :target: https://travis-ci.org/BatLabLancaster/preparenovonix

.. |coverage| image:: https://codecov.io/gh/BatLabLancaster/preparenovonix/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/BatLabLancaster/preparenovonix
	     
.. |docs| image:: https://readthedocs.org/projects/prepare-novonix-data/badge/?version=latest
   :target: https://prepare-novonix-data.readthedocs.io/en/latest/
   :alt: Documentation Status

.. |pypi| image:: https://img.shields.io/pypi/v/preparenovonix.svg
    :target: https://pypi.org/project/preparenovonix/
	 
.. |zenodo| image:: https://zenodo.org/badge/186994865.svg
   :target: https://zenodo.org/badge/latestdoi/186994865
