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

`The Python Language Reference <https://docs.python.org/3/reference/>`__ -
:wp:`BNF <Backus–Naur_form>`

| |b| Define a custom role ``:emlink:``, similar to `\:download\:`__
| |b| Render |emlink_role| to |emlink_html|
| |b| Post to `SO/q/9645321`__

.. |emlink_role| replace:: :code:`:emlink:`x <y>``
.. |emlink_html| replace:: :code:`<em><a style="font-style:italic;" href="y">x</em>`

.. __: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-download
.. __: https://stackoverflow.com/questions/9645321/insert-a-link-into-bold-text-in-restructuredtext

.. https://stackoverflow.com/q/44376893/selectively-disable-readthedocs-syntax-highlighting

.. code:: text

   :raw-html:`<a style="font-style:italic;" href="([^"]+)">([^<]+)</a>`
   :emlink:`\2 <\1>`

`extend the HTML writer to produce a proper <del> tag <https://stackoverflow.com/a/62493316/>`__

| custom configuration value
| |b| `developing extensions for Sphinx <https://www.sphinx-doc.org/en/master/extdev/index.html>`__
| |b| `sphinx.application.Sphinx.add_config_value() <https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_config_value>`__
| |b| `sphinx.application.Sphinx.connect() <https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.connect>`__
| |b| `sphinx.config.Config <https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.config.Config>`__
| |b| `exampleTD <https://www.sphinx-doc.org/en/master/development/tutorials/todo.html>`__
| |b| `exampleEX <https://github.com/sphinx-doc/sphinx/blob/7682353574e7c8b54330f2ce8f273a16816a6d02/sphinx/ext/extlinks.py#L82>`__

| more
| |b| `sphinx- extending sphinx <https://www.sphinx-doc.org/en/master/development/index.html>`__
| |b| `sphinx API - create markup elements (i.e. roles & directives) <https://www.sphinx-doc.org/en/master/extdev/markupapi.html>`__
| |b| `docutils API - create roles <https://docutils.sourceforge.io/docs/howto/rst-roles.html>`__
| |b| `readthedocs - create link roles <https://protips.readthedocs.io/link-roles.html>`__
| |b| `doughellmann - create roles <https://doughellmann.com/posts/defining-custom-roles-in-sphinx/>`__


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


Doctree
=======

`pickle <https://docs.python.org/3/library/pickle.html>`__

list all labels ::

   ./label.py | grep -i devtools


Syntax.Roles\ :raw-html:`<br />`\ Inline Elements
=================================================

| :emlink:`Cross-reference manpage <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-manpages_url>`
| Man page of :manpage:`uname(1)`


Syntax.\ `Directives`__\ :raw-html:`<br />`\ Block Elements
===========================================================

.. __: https://docutils.sourceforge.io/docs/ref/rst/directives.html


`Admonitions`__
---------------

.. __: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives

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

`Showing Code Examples`__
-------------------------

.. __: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#showing-code-examples

| |b| `.. highlight::      <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-highlight>`__
| |b| `.. code-block::     <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`__
|     `:emphasize-lines:   <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-option-code-block-emphasize-lines>`__
|     `:caption:           <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-option-code-block-caption>`__
| |b| `.. literalinclude:: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude>`__

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
