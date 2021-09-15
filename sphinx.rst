.. include:: include/substitution.txt

======
Sphinx
======

Misc
====

`awesome-sphinxdoc <https://github.com/yoloseem/awesome-sphinxdoc>`__

| Tutorials
| |b| `Getting Started <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`__
| |b| `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`__
| |b| `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__
| |b| `Sphinx tutorial <https://www.sphinx-doc.org/en/master/tutorial/index.html>`__

| ?
| |b| `Read the Docs - Getting Started with Sphinx <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`__
| |b| `TYPO3 - Writing documentation <https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/Index.html>`__
| |b| `RST | Sphinx | Sublime | GitHub <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html>`__

| Documentations from `Sphinx`_
| |b| `Sphinx documentation <https://www.sphinx-doc.org/en/master/contents.html>`__
| |b| `Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`__
| |b| `Directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`__
| |b| `Domains <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html>`__

:download:`Sphinx Favicon (SVG)<https://raw.githubusercontent.com/sphinx-doc/sphinx/master/doc/_static/favicon.svg>`.

| rtd_linux
| |b| `conf.py`__
| |b| `theme_overrides.css`__
| |b| `Specific guidelines for the kernel documentation`__

.. __: https://github.com/torvalds/linux/blob/master/Documentation/conf.py
.. __: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/sphinx-static/theme_overrides.css
.. __: https://www.kernel.org/doc/html/latest/doc-guide/sphinx.html#specific-guidelines-for-the-kernel-documentation


`Extensions`__
==============

.. __: https://www.sphinx-doc.org/en/master/usage/extensions/index.html

`The Python Language Reference <https://docs.python.org/3/reference/>`__ -
:wp:`BNF <Backus–Naur_form>`

| `sphinx-toolbox <https://github.com/sphinx-toolbox/sphinx-toolbox>`__

| `sphinx.ext.todo <https://www.sphinx-doc.org/en/master/usage/extensions/todo.html>`__
| `sphinxcontrib-emojicodes <https://github.com/sphinx-contrib/emojicodes>`__

| `sphinx.ext.ifconfig <https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html>`__
| `sphinx.ext.graphviz <https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html>`__
| `sphinxcontrib-plantuml <https://github.com/sphinx-contrib/plantuml>`__
| `sphinxcontrib-tikz <https://github.com/sphinx-contrib/tikz>`__

| `sphinxcontrib-video <https://github.com/sphinx-contrib/video>`__
| `sphinxcontrib-youtube <https://github.com/sphinx-contrib/youtube>`__

| `sphinxcontrib-doxylink <https://github.com/sphinx-contrib/doxylink>`__
| `sphinxcontrib-examplecode <https://github.com/sphinx-contrib/examplecode>`__

| Create [#]_ [#]_ [#]_ [#]_ [#]_ [#]_ [#]_ an `extension`__
| |b| Define a custom role ``:emlink:``, similar to `\:download\:`__
| |b| Render |emlink_role| to |emlink_html|
| |b| Post to `SO/q/9645321`__

.. |emlink_role| replace:: :code:`:emlink:`x <y>``
.. |emlink_html| replace:: :code:`<em><a style="font-style:italic;" href="y">x</em>`

.. __: https://www.sphinx-doc.org/en/master/usage/extensions/index.html
.. __: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-download
.. __: https://stackoverflow.com/questions/9645321/insert-a-link-into-bold-text-in-restructuredtext

.. https://stackoverflow.com/q/44376893/selectively-disable-readthedocs-syntax-highlighting

.. code:: text

   :raw-html:`<a style="font-style:italic;" href="([^"]+)">([^<]+)</a>`
   :emlink:`\2 <\1>`

`extend the HTML writer to produce a proper <del> tag <https://stackoverflow.com/a/62493316/>`__


Building
========

| Build to ``~/beaglebone.gh-pages`` and push to ``gh-pages`` branch
| |b| `GitHub Pages with Python Sphinx <https://www.docslikecode.com/articles/github-pages-python-sphinx>`__
| |b| `sphinx.ext.githubpages <https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html>`__

.. conf.py .. highlight_language = 'bash'

.. code::

   cd ~/beaglebone/Documentation
   sphinx-quickstart

`sphinx-build(1) <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`__

.. code:: bash

   cd ~/beaglebone/Documentation
   make clean; make --no-print-directory entr


Syntax.Roles\ :raw-html:`<br />`\ Inline Elements
=================================================

| :emlink:`Cross-reference manpage <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-manpages_url>`
| Man page of :manpage:`uname(1)`


Syntax.\ `Directives`__\ :raw-html:`<br />`\ Block Elements
===========================================================

.. __: https://docutils.sourceforge.io/docs/ref/rst/directives.html

`Admonitions <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives>`__

.. | `directives`_ - block elements

.. danger::
   danger

.. error::
   error

.. warning::
   warning

.. caution::
   caution

.. attention::
   attention

.. important::
   important

.. hint::
   hint

.. tip::
   tip

.. note::
   note

`showing code examples <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#showing-code-examples>`__

.. highlight:: text

::

   echo "$((date))" >/dev/null

.. code-block::

   echo "$((date))" >/dev/null

.. literalinclude:: include/test.txt

.. highlight:: bash

::

   echo "$((date))" >/dev/null

.. code-block::

   echo "$((date))" >/dev/null

.. literalinclude:: include/test.txt


sphinx_rtd_theme
================

`doc <https://sphinx-rtd-theme.readthedocs.io>`__
- `changelog <https://sphinx-rtd-theme.readthedocs.io/en/stable/changelog.html>`__


Footnotes
=========

.. [#] https://www.sphinx-doc.org/en/master/extdev/index.html
.. [#] https://www.sphinx-doc.org/en/master/extdev/appapi.html
.. [#] https://www.sphinx-doc.org/en/master/extdev/markupapi.html
.. [#] https://www.sphinx-doc.org/en/master/development/index.html
.. [#] https://docutils.sourceforge.io/docs/howto/rst-roles.html
.. [#] https://protips.readthedocs.io/link-roles.html
.. [#] https://doughellmann.com/posts/defining-custom-roles-in-sphinx/
