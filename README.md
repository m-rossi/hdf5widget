# HDF5-Widget

[![PyPi Version](https://img.shields.io/pypi/v/hdf5widget.svg)](https://pypi.python.org/pypi/hdf5widget)
[![Conda Version](https://img.shields.io/conda/vn/mrossi/hdf5widget.svg)](https://anaconda.org/mrossi/hdf5widget)


This is hdf5widget, a widget for viewing the contents of a [HDF5](https://support.hdfgroup.org/HDF5/)-file in [Jupyter](http://jupyter.org/) Notebooks using [ipywidgets](https://github.com/jupyter-widgets/ipywidgets).

## Install

### Installing with pip

```
pip install hdf5widget
```

### Installing with conda

```
conda install -c mrossi hdf5widget
```

## Usage

Assume you have a HDF-file `file.hdf5`.

```python
from hdf5widget import HDF5Widget

HDF5Widget('file.hdf5').widget
```
