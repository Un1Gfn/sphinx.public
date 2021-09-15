.. include:: include/substitution.txt

============
`Holonews`__
============

.. __: https://github.com/Un1Gfn/holonews


Misc
====

in a new terminal ::

   make -C ~/sphinx.public/

in i3 scratchpad git terminal ::

   # source ~/git.bashrc
   cd ~/holonews
   subl \
      ~/sphinx.public/Holonews.rst \
      ~/holonews/download.sh

| filter by flair
| |b| `EN Issue  <https://www.reddit.com/r/HoloNews/?f=flair_name:"EN%20Issue">`__
| |b| `News Post <https://www.reddit.com/r/HoloNews/?f=flair_name:"News%20Post">`__

| :manpage:`tree(1)`
| :manpage:`vidir(1)`

| pdf thumbnail preview
| |b| /usr/local/share/thumbnailers/imagemagick-pdf.thumbnailer [#pdfthumb]_
| |b| :pr:`nautilus <- evince`

| http
| `filebrowser <https://github.com/filebrowser/filebrowser>`__ (go+vue) (`site <https://filebrowser.org/>`__)
| `miniserve <https://github.com/svenstaro/miniserve>`__ (rust)
|  ``sudo miniserve -D -g -H -l -q -r -v -z -i 192.168.0.223 -p 80 -- ~/cgi/``

| disable delta compression
| |b| `<https://confluence.atlassian.com/stashkb/how-to-disable-delta-compression-on-stash-server-for-a-particular-file-type-761242185.html>`__
| |b| `<https://stackoverflow.com/questions/7102053/git-pull-without-remotely-compressing-objects>`__
| |b| `<https://public-inbox.org/git/20100514051049.GF6075@coredump.intra.peff.net/>`__
| |b| `<https://git-scm.com/docs/gitattributes>`__


Download
========

`YouTube Metadata <https://mattw.io/youtube-metadata/>`__

::

   cd ~
   tree --charset=ascii -C holonews

.. code:: text

   holonews
   |-- download.sh
   |-- 20210802_20210808_p1pn6c_News.d
   |-- 20210802_20210808_p1pn6c_News.pdf
   |-- 20210809_20210815_p64ave_News.d
   |-- 20210809_20210815_p64ave_News.pdf
   |-- 20210809_20210816_p6rlkt_Special-Live-Events.d
   |-- 20210809_20210816_p6rlkt_Special-Live-Events.pdf
   |-- 20210816_20210822_pant15_News.d
   |-- 20210816_20210822_pant15_News.pdf
   |-- 20210822_20210823_pbkt4a_Special-HoloCouncil-Debut.d
   |-- 20210822_20210823_pbkt4a_Special-HoloCouncil-Debut.pdf
   |-- 20210823_20210829_pf7kx8_News.d
   |-- 20210823_20210829_pf7kx8_News.pdf
   |-- ...

::

   source ~/proxy.bashrc
   ~/holonews/holonews.sh 20210823 20210829 pf7kx8 News
   ~/holonews/holonews.sh 20210809 20210816 p6rlkt Special-Live-Events
   ~/holonews/holonews.sh 20210822 20210823 pbkt4a Special-HoloCouncil-Debut


Comment
=======

reddit comment template

::

   
   function reddit_comment_template {
   echo
   [ 4 -eq "$#" ] || return
   IFS0="$IFS"; IFS=_; BASE="$*"; IFS=$IFS0
   local SP=' '
   read -erp "clipboard will be overwritten, ok? "; echo
   # sed -e "s/@ID@/$1/g" <<EOT | xclip -i -selection clipboard
   xclip -i -selection clipboard <<EOT
   ${BASE}${SP}${SP}
   PDF format${SP}${SP}
   [artifact](https://github.com/Un1Gfn/holonews/blob/master/${BASE}/${BASE}.pdf)${SP}${SP}
   [download link 1](https://raw.githubusercontent.com/Un1Gfn/holonews/master/${BASE}/${BASE}.pdf)${SP}${SP}
   [download link 2](https://github.com/Un1Gfn/holonews/raw/master/${BASE}/${BASE}.pdf)
   EOT
   echo "dump clipboard below https://www.reddit.com/r/HoloNews/comments/$4"; echo
   }

::

   reddit_comment_template 2021 0816 0822 pant15


Manually
========

| for   2021\_0802\_0808_\ **p1pn6c**
| visit https://www.reddit.com/r/HoloNews/comments/p1pn6c

| PDF link
| |b| `raw.githubusercontent.com/:owner/:repo/:branch/path/to/file <https://raw.githubusercontent.com/Un1Gfn/holonews/master/2021_0802_0808_p1pn6c/2021_0802_0808_p1pn6c.pdf>`__
| |b| `github.com/:owner/:repo/raw/:branch/path/to/file <https://github.com/Un1Gfn/holonews/raw/master/2021_0802_0808_p1pn6c/2021_0802_0808_p1pn6c.pdf>`__

To download images from reddit/twitter post

1. Visit the post in a new browser window
2. Open the pages in new tabs, one by one
3. Visit the post on smartphone
4. Make sure pages and tabs are in the same order
5. Close the post in browser
6. Copy all URLs (extension?)
7. Construct wget oneliners with text editor, and add output filename
8. Copy, paste to terminal, and execute


Footnotes
=========

.. [#pdfthumb] :aw:`file manager functionality#Use_PCManFM_to_get_thumbnails_for_other_file_types`
