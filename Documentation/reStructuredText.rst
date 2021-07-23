================
reStructuredText
================

.. image:: https://img.shields.io/badge/%F0%9F%9B%A1%EF%B8%8F-shield-success

|

.. warning::
  A plain text ``README`` in ``$(git rev-parse --show-toplevel)`` points here. There is **NO** ``readme.rst.``

Ongoing Transition from GitHub Flavored Markdown to reStructuredText ...

`live reST online <http://rst.ninjs.org>`__

| rtd_linux
| |b| `Specific guidelines for the kernel documentation`_
| |b| `conf.py`_
| |b| `theme_overrides.css <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/sphinx-static/theme_overrides.css>`__

Render HTML to ``~/beaglebone.gh-pages`` and push to ``gh-pages`` branch

| `roles`_ - inline elements
| `directives`_ - block elements

.. `roles`_
..   inline elements

.. `directives`_
..   block elements


.. code:: bash

  cd ~/beaglebone/Documentation
  sphinx-quickstart

.. code:: bash

  rm -rfv ~/beaglebone/Documentation/_build
  rm -rfv ~/cgi/cgi-tmp/sphinx

`sphinx-build(1)`_

.. code:: bash

  cd ~/beaglebone/Documentation
  ls -d1 conf.py *rst | entr sphinx-build -b html . _build
  ls -d1 conf.py *rst | entr sphinx-build -b html . ~/cgi/cgi-tmp/sphinx
  printf "\n  file://%s\n\n" "$(realpath _build/index.html)"


:kbd:`Ctrl+C`

:file:`default.conf`

| Unicode
| |b| `unicode.rst <_sources/unicode.rst.txt>`__
| |b| `<http://www.amp-what.com/>`__
| |b| `<https://www.toptal.com/designers/>`__

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions

rtd missing bullets
`#1145 <https://github.com/readthedocs/sphinx_rtd_theme/issues/1145>`__
`#1115 <https://github.com/readthedocs/sphinx_rtd_theme/issues/1115>`__

.. role:: raw-html(raw)

    :format: html

:raw-html:`<span style="text-align: center; color: green;">build</span>`

----

.. https://docutils.sourceforge.io/docs/ref/rst/directives.html#include

.. include:: unicode.rst

.. _roles: https://docutils.sourceforge.io/docs/ref/rst/roles.html
.. _directives: https://docutils.sourceforge.io/docs/ref/rst/_directives.html
.. _conf.py: https://github.com/torvalds/linux/blob/master/Documentation/conf.py
.. _Specific guidelines for the kernel documentation: https://www.kernel.org/doc/html/latest/doc-guide/sphinx.html#specific-guidelines-for-the-kernel-documentation
.. _sphinx-build(1): https://www.sphinx-doc.org/en/master/man/sphinx-build.html
