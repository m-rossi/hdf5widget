import h5py
from .hdf5object import HDF5Object
import ipywidgets as widgets
import os


class HDF5Widget:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.isfile(filename):
            raise FileNotFoundError(f'File {filename} not found!')
        self.h5object = h5py.File(filename, 'r', libver='latest')
        self.close_button = widgets.Button(description='Close file')
        self.close_button.on_click(self.close)
        self.widget = widgets.VBox([self.close_button,
                                    HDF5Object(self.h5object).widget])

    def __exit__(self):
        self.h5object.close()
        self.widget.close()

    def close(self, _):
        self.__exit__()
