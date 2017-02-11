# matlab_nbconvert

This is an exporter for `nbconvert` that turns matlab-notebooks into neatly formatted matlab (`.m`) files. You need to have `nbconvert` installed.

Usage: type `jupyter nbconvert --to matlab 'notebookname.ipynb'`, inserting your filename as needed.

All cells in the resulting `.m` files are delimited by the matlab sectioning `%%`, which means you can run your code as sections in Matlab like you would in jupyter. All code cells have the heading "Cell [X]", where X is the output number present in your notebook.

You can then turn these `.m` files into _Matlab Live Scripts_, which is Mathwork's version of a notebook. In future releases, I may release something like this as well.

Install by cloning this repository, opening a terminal in the directory, and typing `pip install .`, or get the package from pypi by typing `pip install matlab_nbconvert`.
