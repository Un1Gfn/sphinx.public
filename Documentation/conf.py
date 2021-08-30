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
import os, sys
# sys.path.append(os.path.abspath('extension'))
sys.path.insert(0, os.path.abspath('extension'))
del os, sys


# -- Project information -----------------------------------------------------

project = 'beaglebone'
author = 'Darren Ng'
import time
copyright = time.strftime("%Y")
del time
assert str == type(copyright)
assert copyright
copyright += ', '
copyright += author


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
extensions = [
    # 'sphinx.ext.duration',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',       # https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
    'sphinx.ext.todo',
    'sphinxemoji.sphinxemoji',
    'sphinxcontrib.youtube',        # /usr/lib/python3*/site-packages/sphinxcontrib/youtube/
    'sphinxcontrib.programoutput',  # https://pythonhosted.org/sphinxcontrib-programoutput/
    'archlinux',
    'xxlink',  # emlink stlink
    'wikilink'  # wp:Wikipedia aw:ArchWiki
]

# sphinxemoji_style = 'twemoji' # Too large

# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#confval-extlinks
extlinks = {
    'tree': (
        'https://github.com/Un1Gfn/' + project + '/tree/master/%s',
        '%s'
    ),
    'rtdissue': (
        'https://github.com/readthedocs/sphinx_rtd_theme/issues/%s',
        '#%s'
    ),
    'r': (
        'https://www.reddit.com/r/%s',
        'r/%s'
    ),
    # archlinux.py
    # https://en.wikipedia.org/wiki/Help:Interwiki_linking
    # 'wp': (
    #     'https://en.wikipedia.org/wiki/%s',
    #     'wp:%s'
    # ),
    # archlinux.py
    # https://wiki.archlinux.org/title/Help:Editing#Interwiki_links
    # 'aw': (
    #     'https://wiki.archlinux.org/title/%s',
    #     'aw:%s'
    # ),
    # Explicitly Banned in extension/archlinux.py
    # 'aur': (
    #     'https://aur.archlinux.org/packages/%s',
    #     'aur/%s'
    # ),
}

# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration
todo_include_todos = True
todo_emit_warnings = True

source_suffix = {'.rst': 'restructuredtext'}

source_encoding = 'utf-8-sig'

# Changed in version 4.0: Renamed master_doc to root_doc.
# Don't use "Index.rst" or there will be "Index.html" instead of "index.html"
# https://www.sphinx-doc.org/en/master/glossary.html#term-master-document
root_doc = 'index'

# exclude_patterns = [
#     'rst_epilog.rst',
#     'rst_prolog.rst',
# ]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# # https://www.tutorialkart.com/python/python-read-file-as-string/
# import os
# f = open('rst_epilog.rst', "r")
# # f = open('rst_epilog.txt', "r")
# # included at the end of every source file
# rst_epilog = f.read()
# assert rst_epilog
# f.close(); del f
# del os

# import os
# f = open('rst_prolog.rst', "r")
# # f = open('rst_prolog.txt', "r")
# # included at the beginning of every source file
# rst_prolog = f.read()
# assert rst_prolog
# f.close(); del f
# del os

default_role = None

# "System Message: WARNING/2 (..., line ...)" in html
keep_warnings = False

# https://stackoverflow.com/a/20730381/
# suppress_warnings = []
assert ('suppress_warnings' not in locals()) and ('suppress_warnings' not in globals())

import sphinx
needs_sphinx = '4.1.2'
assert (4, 1, 2) == sphinx.version_info[:3]
del sphinx

# :manpage:`uname(1)`
# https://manpages.debian.org/buster/coreutils/uname.1.en.html
# https://man.archlinux.org/man/uname.1
# manpages_url = 'https://manpages.debian.org/{path}'
manpages_url = 'https://man.archlinux.org/man/{page}.{section}'

smartquotes = True

# https://stackoverflow.com/q/44376893/selectively-disable-readthedocs-syntax-highlighting
# highlight_language = 'none'
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
# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    'navigation_depth': -1,
    # 'titles_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'None',
    # 'style_external_links': True,
}

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl
# sphinx.ext.githubpages
# CNAME
# html_baseurl = 'https://Un1Gfn.github.io/beaglebone'

html_context = {'css_files': [
    '_static/code.css',
    '_static/narrow_nav.css',
    '_static/problematic.css',
    '_static/theme_overrides.css',
]}

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
