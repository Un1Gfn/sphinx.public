.. include:: include/substitution.txt

===========
TeX組版処理
===========

雑
===

| ダミーテキスト
|    :ja:`いろは歌`
|    外務省/`世界人権宣言（仮訳文） <https://www.mofa.go.jp/mofaj/gaiko/udhr/1b_001.html>`__
|    lorem ipsum/:ja:`訳 <lorem ipsum#テキストの出典>`
|    `吾輩は猫である <https://www.aozora.gr.jp/cards/000148/files/789_14547.html>`__

| `japanese.tex (pdf) <https://ctan.math.washington.edu/tex-archive/macros/latex/contrib/babel-contrib/japanese/>`__

`Requirements for Japanese Text Layout 日本語組版処理の要件 <https://www.w3.org/TR/jlreq/>`__

| `LaTeXの良さとXeLaTeXの日本語環境について <https://yyhhyy.hatenablog.com/entry/2015/10/17/203000>`__
| `TeXでつくるプロポーショナル組日本語文書 <https://qiita.com/zr_tex8r/items/0512dd43e9806483013a>`__
| `日本語 LaTeX の新常識 2021 <https://qiita.com/wtsnjp/items/76557b1598445a1fc9da>`__
| :ctan:`uplatex`\ +\ :ctan:`jlreq`\ +\ :ctan:`pxchfon`
|    `徹底攻略 pxchfonを使いこなそう <https://qiita.com/zr_tex8r/items/a13c195d42b7fca69378>`__
|    `LuaLaTeXでUDフォントを使う <https://qiita.com/kakinaguru_zo/items/22c4db21e03d4608e300>`__
|    `(Linux) upLaTeX + jlreq で小説原稿を作る <https://aznote.jakou.com/linux/latex_novel.html>`__

`international language support <https://www.overleaf.com/learn/latex/International_language_support>`__
|rarr| `Japanese <https://www.overleaf.com/learn/latex/Japanese>`__

| :pr:`xecjk`
| :ctan:`luatexja` |rarr| Sources /macros/luatex/generic/luatexja |rarr| doc |rarr| luatexja-ruby.pdf

| TeXWiki.`TeX/LaTeX入門 <https://texwiki.texjp.org/>`__
| Wikibooks.`TeX/LaTeX入門 <https://ja.wikibooks.org/wiki/TeX/LaTeX%E5%85%A5%E9%96%80>`__

| wp.:ja:`禁則処理`
| 平プロモート.`禁則処理 <https://www.tairapromote.co.jp/column/284/>`__


フォント
========

`TeXとフォント <https://texwiki.texjp.org/?TeX%E3%81%A8%E3%83%95%E3%82%A9%E3%83%B3%E3%83%88>`__

::

   (/usr/share/texmf-dist/tex/luatex/luatexja/patches/lltjfont.sty
   (/usr/share/texmf-dist/tex/latex/base/tuenc.def))
   (/usr/share/texmf-dist/tex/luatex/luatexja/patches/lltjdefs.sty
   luaotfload | db : Font names database not found, generating new one.
   luaotfload | db : This can take several minutes; please be patient.
   (/usr/share/texmf-dist/tex/luatex/jlreq/jfm-jlreqv.lua)
   (/usr/share/texmf-dist/tex/luatex/jlreq/jfm-jlreq.lua))

LuaTeX-ja.`フォントの指定 <https://ja.osdn.net/projects/luatex-ja/wiki/LuaTeX-ja%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9#h3-.E3.83.95.E3.82.A9.E3.83.B3.E3.83.88.E3.81.AE.E6.8C.87.E5.AE.9A>`__

`日本語フォント設定ツール kanji-config-updmap <https://www.ctan.org/pkg/ptex-fontmaps>`__
