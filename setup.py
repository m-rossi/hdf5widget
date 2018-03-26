import os
from setuptools import setup


# Get the long description from the README file
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       'README.rst'),
          encoding='utf-8') as f:
    long_description = f.read()

setup(
    author='Marco Rossi',
    author_email='developer@marco-rossi.com',
    classifiers=['Operating System :: OS Independent',
                 'Development Status :: 3 - Alpha',
                 'Framework :: Jupyter',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.6'],
    description='This is hdf5widget, a widget for viewing the contents of a '
                'HDF5-file in Jupyter Notebooks using ipywidgets.',
    install_requires=['h5py', 'ipywidgets>=7.0'],
    license='MIT',
    keywords=['jupyter', 'hdf5', 'notebook'],
    long_description=long_description,
    name='hdf5widget',
    packages=['hdf5widget'],
    python_requires='>=3.6',
    setup_requires=['setuptools_scm'],
    url='https://github.com/m-rossi/hdf5widget',
    use_scm_version=True)
