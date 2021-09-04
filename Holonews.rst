.. include:: include/substitution.txt

============
`Holonews`__
============

.. __: https://github.com/Un1Gfn/holonews


Misc
====

| filter by flair
| |b| `EN Issue  <https://www.reddit.com/r/HoloNews/?f=flair_name:"EN%20Issue">`__
| |b| `News Post <https://www.reddit.com/r/HoloNews/?f=flair_name:"News%20Post">`__

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


download.sh
===========

::

   cd ~/holonews
   source ~/proxy.bashrc

.. code:: text

   ./download.sh 2021 0802 0808 p1pn6c
   ./download.sh 2021 0809 0815 p64ave
   ./download.sh 2021 0816 0822 pant15


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
