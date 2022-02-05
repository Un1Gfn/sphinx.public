# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os, sys, sphinx, time

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# sys.path.append(os.path.abspath('extension'))
sys.path.insert(0, os.path.abspath('extension'))


# -- Project information -----------------------------------------------------

# os.path.realpath(__file__)
# project = os.path.dirname(__file__)
# project = os.path.basename(os.path.dirname(__file__))
project = os.path.basename(os.getcwd())
author = 'Darren Ng'
copyright = time.strftime("%Y")
assert str == type(copyright)
assert copyright
copyright += ', '
copyright += author


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
extensions = [
    # 'sphinx.ext.duration',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',       # https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
    'sphinx.ext.graphviz',
    'sphinx.ext.todo',
    'sphinx_copybutton',            # https://sphinx-copybutton.readthedocs.io/en/latest/
    'sphinxcontrib.programoutput',  # https://pythonhosted.org/sphinxcontrib-programoutput/
    'sphinxcontrib.youtube',        # /usr/lib/python3*/site-packages/sphinxcontrib/youtube/
    'sphinxemoji.sphinxemoji',
    'myextension',
    'sphinx.ext.mathjax',
]

# https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax
# http://docs.mathjax.org/en/latest/web/components/combined.html
# relative to the _static directory
mathjax_path = 'mathjax/tex-mml-chtml.js'

# https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#confval-extlinks
extlinks = {

    'tree':     ('https://github.com/Un1Gfn/' + project + '/tree/master/%s',    '%s',),
    'rtdissue': ('https://github.com/readthedocs/sphinx_rtd_theme/issues/%s',  '#%s',),
    'r':        ('https://www.reddit.com/r/%s',                               'r/%s',),
    'amz':      ('https://www.amazon.com/s?k=%s',                               '%s',),
    'taobao':   ('https://item.taobao.com/item.htm?id=%s',                      '%s',),
    'tmall':    ('https://detail.tmall.com/item.htm?id=%s',                     '%s',),
    'yt':       ('https://www.youtube.com/watch?v=%s',                          '%s',),
    'eol':      ('https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles/%s',  '%s',),

    # extension/define.py:wikiprepend_dict
    'aw':   ('https://wiki.archlinux.org/title/%s',             '%s',),
    'dw':   ('https://wiki.debian.org/%s',                      '%s',),
    'el':   ('https://elinux.org/%s',                           '%s',),
    'gw':   ('https://wiki.gentoo.org/wiki/%s',                 '%s',),
    'wp':   ('https://en.wikipedia.org/wiki/%s',                '%s',),
    'ja':   ('https://ja.wikipedia.org/wiki/%s',                '%s',),
    'zh':   ('https://zh.wikipedia.org/wiki/%s',                '%s',),
    'egw':  ('https://emulation.gametechwiki.com/index.php/%s', '%s',),
    'tw':   ('https://www.thinkwiki.org/wiki/%s',               '%s',),
    'tiw':  ('https://www.theiphonewiki.com/wiki/%s',           '%s',),
    'pmos': ('https://wiki.postmarketos.org/wiki/%s',           '%s',),

    'mt': ('https://app.element.io/#/room/%s', '%s',), # element/matrix

    'ly': ('https://lilypond.org/doc/v2.22/Documentation/%s', '%s',),

}

# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration
todo_include_todos = True
todo_emit_warnings = True

# sphinxemoji_style = 'twemoji' # Too large

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
# f = open('rst_epilog.rst', "r")
# # f = open('rst_epilog.txt', "r")
# # included at the end of every source file
# rst_epilog = f.read()
# assert rst_epilog
# f.close(); del f
rst_epilog = """
.. |project| replace:: %s
.. _project: https://github.com/Un1Gfn/%s
"""%(project,project)

# Caveat: sphinxemoji.sphinxemoji does not work if rst_prolog is set
# f = open('rst_prolog.rst', "r")
# # f = open('rst_prolog.txt', "r")
# # included at the beginning of every source file
# rst_prolog = f.read()
# assert rst_prolog
# f.close(); del f

default_role = None

# "System Message: WARNING/2 (..., line ...)" in html
keep_warnings = False

# https://stackoverflow.com/a/20730381/
# suppress_warnings = []
assert ('suppress_warnings' not in locals()) and ('suppress_warnings' not in globals())

needs_sphinx = '4.1.2'
# assert (4, 1, 2) == sphinx.version_info[:3]

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
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': -1,
    'display_version': True,
    'prev_next_buttons_location': 'None',
}

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl
# sphinx.ext.githubpages
# CNAME
# html_baseurl = 'https://Un1Gfn.github.io/beaglebone'

# https://icon-icons.com/icon/chip-computer-hardware-memory-electronic-device/142017
# html_logo = 'favicon.ico'
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']
html_css_files = [
    'css/custom.css',
]

# Mon Jul 26 21:12:31 WITA 2021
html_last_updated_fmt = '%a %b %d %H:%M:%S WITA %Y'
# html_last_updated_fmt = '%a %b %d %H:%M:%S UTC%z %Y'
# html_last_updated_fmt = '%Y %m %d %H:%M:%S %z %a %A %b %B %c %I %p'
# html_last_updated_fmt = '%c'
# html_last_updated_fmt = ''

html_copy_source = True
