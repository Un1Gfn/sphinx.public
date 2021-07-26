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

project = 'beaglebone'
author = 'Darren Ng'
import time
copyright = time.strftime("%Y")
assert str == type(copyright)
assert copyright
copyright += ', '
copyright += author
del time

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
#
extensions = ['sphinx.ext.extlinks']

# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#confval-extlinks
extlinks = {
    'tree': (
        'https://github.com/Un1Gfn/' + project + '/tree/master/%s',
        '%s'
    ),
    'rtdissue': (
        'https://github.com/readthedocs/sphinx_rtd_theme/issues/%s',
        '#%s'
    )
}

source_suffix = {'.rst': 'restructuredtext'}

source_encoding = 'utf-8-sig'

# Changed in version 4.0: Renamed master_doc to root_doc.
root_doc = 'Index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

default_role = None

keep_warnings = True

# https://stackoverflow.com/a/20730381/
# suppress_warnings = []
assert ('suppress_warnings' not in locals()) and ('suppress_warnings' not in globals())

import sphinx
needs_sphinx = '4.1.1'
assert (4, 1, 1) == sphinx.version_info[:3]

# :manpage:`uname(1)`
# https://manpages.debian.org/buster/coreutils/uname.1.en.html
# https://man.archlinux.org/man/uname.1
# manpages_url = 'https://manpages.debian.org/{path}'
manpages_url = 'https://man.archlinux.org/man/{page}.{section}'

smartquotes = True

highlight_language = 'bash'


# -- Options for internationalization ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# https://stackoverflow.com/a/27767165
html_theme_options = {
    'navigation_depth': 99
}

html_context = {
    'css_files': ['_static/theme_overrides.css']
}

# https://icon-icons.com/icon/chip-computer-hardware-memory-electronic-device/142017
# html_logo = 'favicon.ico'
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['rtd_linux']

# Mon Jul 26 21:12:31 WITA 2021
html_last_updated_fmt = '%a %b %d %H:%M:%S UTC%z %Y'
# html_last_updated_fmt = '%Y %m %d %H:%M:%S %z %a %A %b %B %c %I %p'
# html_last_updated_fmt = '%c'
# html_last_updated_fmt = ''

html_copy_source = True
