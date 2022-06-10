.. include:: include/substitution.txt

===============
TeX Typesetting
===============

`TeX family tree with timeline <https://tex.stackexchange.com/questions/42594>`__

| \
   ``file -L $(pacman -Qql texlive-bin | grep -E '/usr/bin/.*tex.*') | grep -v 'POSIX shell script, ASCII text executable' | less -S``
| :ctan:`tex` |rarr| :ctan:`ptex` |rarr| :ctan:`uptex`
| `tectonic <https://tectonic-typesetting.github.io/>`__ (xelatex+rust)

groff+\ `mom <http://www.schaffter.ca/mom/>`__

`Major (La)TeX Applications <https://tug.org/applications/>`__

`symbols-a4.pdf <https://www.ctan.org/tex-archive/info/symbols/comprehensive/>`__

| TeX :stlink:`FAQ <https://texfaq.org/>`
| wiki `books <https://texfaq.org/FAQ-doc-wiki>`__
|    \
     `TeX     <https://en.wikibooks.org/wiki/TeX>`__
     |vv| :stlink:`LaTeX   <https://en.wikibooks.org/wiki/LaTeX>`
     |vv| `ConTeXt <https://wiki.contextgarden.net/Main_Page>`__
| `alternatives <https://texfaq.org/FAQ-alternatives>`__ to TeX
| `where <https://texfaq.org/FAQ-symbols>`__ can I find the symbol for ...
     (`detexify <http://detexify.kirelabs.org/classify.html>`__)
     (`shapecatcher <http://shapecatcher.com/>`__)

:wp:`ConTeXt` - LaTeX alternative (macro package?)

`KaTeX <https://katex.org/>`__ - MathJax alternative

`tectonic <https://tectonic-typesetting.github.io/>`__ - XeTeX alternative

| \
  (slide) :wp:`beamer <beamer (LaTeX)>`
  |vv| `CTAN <https://ctan.org/pkg/beamer>`__
  |vv| `overleaf <https://www.overleaf.com/learn/latex/Beamer>`__
| themes `matrix <https://hartwork.org/beamer-theme-matrix/>`__
| `metropolis <https://github.com/matze/mtheme>`__ theme
| \
  ``$pacman -Fql texlive-core | grep usr/share/texmf-dist/tex/latex/beamer/beamerth``

| LuaTeX/`pdfTeX vs XeTeX vs LuaTeX <http://www.luatex.org/roadmap.html#tbp>`__
|    :sub:`If such integration is not what you want, you might consider sticking to the other engines (XeTeX?) as there are no real advantages to using LuaTeX then`

| sphinx-contrib/`tikz <https://github.com/sphinx-contrib/tikz>`__
| `complicated geometry figures <https://tex.stackexchange.com/questions/538319/>`__
| `CTAN <https://ctan.org/pkg/pgf>`__
|    `unofficial minimal introduction to TikZ <https://cremeronline.com/LaTeX/minimaltikz.pdf>`__
|    `TiKZ & PGF manual <https://ftp.kaist.ac.kr/tex-archive/graphics/pgf/base/doc/pgfmanual.pdf>`__

`colors <https://en.wikibooks.org/wiki/LaTeX/Colors>`__

| `incorrect spacing <https://tex.stackexchange.com/questions/21598>`__
| :math:`\sin(x+k\pi)=-\sin x  \quad correct`
| :math:`\sin(x+k\pi)=-\sin{x} \quad correct`
| :math:`\sin(x+k\pi)=-\sin{}x \quad incorrect`
| :math:`\sin(x+k\pi)=-{\sin}x \quad incorrect`
| :math:`\sin(x+k\pi)={-\sin}x \quad incorrect`

| `Spacing in math mode         <https://www.overleaf.com/learn/latex/Spacing_in_math_mode>`__
| `Line breaks and blank spaces <https://www.overleaf.com/learn/latex/Line_breaks_and_blank_spaces>`__

`mathematical fonts <https://www.overleaf.com/learn/latex/Mathematical_fonts>`__

| :wp:`typographic unit`
| 1 in is exactly 25.4 mm [#inch]_
| 1 in is exactly 72.27 pt (:wp:`TeX point <point (typography)#American_points>`) [#overleafLengths]_

| :wp:`MetaPost`
| :wp:`PGF/TikZ` :wp:`CircuiTikZ`
| :wp:`PSTricks`

| :ctan:`xltxtra`
| :ctan:`fontspec`
| luatexja-fontspec

`Introduction to LaTeX <https://www.ctan.org/tex-archive/info/lshort/>`__

`lengths <https://www.overleaf.com/learn/latex/Lengths_in_LaTeX>`__

| overleaf.`documentclass <https://www.overleaf.com/learn/latex/Creating_a_document_in_LaTeX>`__
| wikibook.`documentclass <https://en.wikibooks.org/wiki/LaTeX/Document_Structure#Document_classes>`__

| :wp:`EPUB`
|    `tutorial <http://www.jedisaber.com/eBooks/Introduction.shtml>`__
|    `specification <https://www.w3.org/publishing/epub32/>`__
|    `Apple Books <https://apps.apple.com/us/app/id364709193>`__
|    `Amazon Kindle <https://apps.apple.com/us/app/id302584613>`__



Footnotes
=========

.. [#inch] https://en.wikipedia.org/wiki/Inch
.. [#overleafLengths] https://www.overleaf.com/learn/latex/Lengths_in_LaTeX



