from setuptools import setup

setup(author='Marco Rossi',
      author_email='developer@marco-rossi.com',
      classifiers=['Operating System :: OS Independent',
                   'Programming Language :: Python :: 3.6'],
      description='This is hdf5widget, a widget for viewing the contents of a '
                  'HDF5-file in Jupyter Notebooks using ipywidgets.',
      install_requires=['h5py', 'ipywidgets'],
      license='MIT',
      name='hdf5widget',
      packages=['hdf5widget'],
      python_requires='>=3.6',
      version='0.1',
      url='https://github.com/m-rossi/hdf5widget')
