# file __init__.py
# from traitlets.config import Config
from traitlets import default
from nbconvert.exporters.templateexporter import TemplateExporter
# path utils to add template to search path
import os.path

"""Matlab script Exporter class"""

# Copyright (c) Jan Freyberg
# Distributed under the terms of the Modified BSD License.


class MatlabExporter(TemplateExporter):
    """
    Exports a Python code file.
    """

    @default('file_extension')
    def _file_extension_default(self):
        return '.m'

    template_path = ['.', os.path.join(os.path.dirname(__file__),
                          "templates")]

    @default('template_file')
    def _template_file_default(self):
        # return os.path.join(os.path.dirname(__file__), 'templates', 'matlab.tpl')
        return 'matlab'

    # not sure if this is required
    # output_mimetype = 'text/matlab'

# Init this class for testing
if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'templates', 'matlab.tpl'), 'r') as f:
        print(f)
