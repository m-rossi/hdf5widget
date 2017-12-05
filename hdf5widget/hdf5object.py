import h5py
import ipywidgets as widgets
from ipywidgets import Layout


class HDF5Object:
    def __init__(self, h5object):
        self.h5object = h5object

        # init list of objects to display
        vbox = []

        # iterate groups and datasets
        children = {}
        datasets = []
        for name, obj in self.h5object.items():
            if isinstance(obj, h5py.Dataset):
                datasets.append(name)
            elif isinstance(obj, h5py.Group):
                children[name] = HDF5Object(obj).widget

        # create accordion object
        self.groups = widgets.Accordion(
            children=[val for val in children.values()], selected_index=None)
        vbox.append(self.groups)

        # name each accordion sub-object
        for ii, val in enumerate(children):
            self.groups.set_title(ii, val)

        def dataset_selection_changed(change):
            datasets_info = []
            for dataset in change['new']:
                values = [f'<b>{dataset}</b>',
                          f'<i>shape</i>: {self.h5object[dataset].shape}',
                          f'<i>dtype</i>: {self.h5object[dataset].dtype}']
                for attr in self.h5object[dataset].attrs:
                    values.append(
                        f'<i>{attr}</i>: {h5object[dataset].attrs[attr]}')
                datasets_info.append(widgets.HTML(
                    value='<br/>'.join(values),
                    layout=Layout(width='100%')))
            self.datasets_info.children = datasets_info
        # init vbox for dataset attributes and info
        self.datasets_info = widgets.VBox([])

        # create SelectMultiple widget for datasets
        if len(datasets) > 0:
            self.datasets = widgets.SelectMultiple(options=datasets)
            self.datasets.observe(dataset_selection_changed, names='value')
            vbox.append(self.datasets)
            vbox.append(self.datasets_info)

        # create VBox for attributes
        attributes = []
        for attr in self.h5object.attrs:
            attributes.append(f'<i>{attr}</i>: {self.h5object.attrs[attr]}')
        self.attributes = widgets.HTML(value='<br/>'.join(attributes),
                                       layout=Layout(width='100%'))

        # create widget
        if len(attributes) > 0:
            self.widget = widgets.Tab([widgets.VBox(vbox),
                                       self.attributes])
            self.widget.set_title(0, 'Groups / Datasets')
            self.widget.set_title(1, 'Attributes')
        else:
            self.widget = widgets.VBox(vbox)
