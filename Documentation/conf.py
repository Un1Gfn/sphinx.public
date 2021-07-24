# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

source_suffix = '.rst'

project = 'beaglebone'
copyright = '2021, Darren Ng'
author = 'Darren Ng'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
#
extensions = [
    'sphinx.ext.extlinks'
]

# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#confval-extlinks
extlinks = {
    'tree': (
        'https://github.com/Un1Gfn/'+project+'/tree/master/%s',
        '%s'
    ),
    'rtdissue': (
        'https://github.com/readthedocs/sphinx_rtd_theme/issues/%s',
        '#%s'
    )
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# https://stackoverflow.com/a/27767165
html_theme_options = {
    'navigation_depth': 99,
}

# https://icon-icons.com/icon/chip-computer-hardware-memory-electronic-device/142017
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['rtd_linux']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',
    ],
}
