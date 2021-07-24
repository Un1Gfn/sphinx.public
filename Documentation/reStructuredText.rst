======================
|ico| reStructuredText
======================

.. image:: https://img.shields.io/badge/%F0%9F%9B%A1%EF%B8%8F-shield-success
  :target: https://shields.io/
  :alt: [shield]

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

.. | `directives`_ - block elements
.. | `roles`_ - inline elements
.. | .. \`x <y>`_  - Named hyperlink reference
.. | .. \`x <y>`__  - Anonymous hyperlink reference

`Directives`_
  block elements

`Roles`_
  inline elements

\.. \`example <\https://example.org>`_
  Named hyperlink reference

\.. \`example <\https://example.org>`__
  Anonymous hyperlink reference

\:doc:\`Hardware`
  `Direct link to documents <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-doc>`__

\:file:\`default.conf`
  File

\:kbd:\`Ctrl+C`
  Key press


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

| Unicode
| |b| `substitution.rst <_sources/substitution.rst.txt>`__
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

.. include:: substitution.rst

.. _roles: https://docutils.sourceforge.io/docs/ref/rst/roles.html
.. _directives: https://docutils.sourceforge.io/docs/ref/rst/_directives.html
.. _conf.py: https://github.com/torvalds/linux/blob/master/Documentation/conf.py
.. _Specific guidelines for the kernel documentation: https://www.kernel.org/doc/html/latest/doc-guide/sphinx.html#specific-guidelines-for-the-kernel-documentation
.. _sphinx-build(1): https://www.sphinx-doc.org/en/master/man/sphinx-build.html
