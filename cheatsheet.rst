.. include:: include/substitution.txt

==========
Cheatsheet
==========

Bash
====

|:link:| :doc:`bash`

.. highlight:: bash

WIP move everything from :file:`~/cheatsheet.sh`

`sysfs <https://www.kernel.org/doc/html/latest/filesystems/sysfs.html>`__ kernal doc - :manpage:`sysfs(5)`

assertion or error handling ::

   # trap 'echo "SIGINT"; exit 0' SIGINT
   [ ] || { notify-send "${BASH_SOURCE[0]}" "${FUNCNAME[0]}${LF}line ${BASH_LINENO[0]}"; return 1; }
   [ ] || { echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; return 1; }
   [ ] || { echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; exit 1; }
   # ${BASH_COMMAND}

::

   [ ] || @ABRTEXIT@
   [ ] || @ABRTRET@
   ABRTEXIT='{ echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; return 1; }'
   ABRTRET='{ echo "${BASH_SOURCE[0]}:$LINENO:${FUNCNAME[0]}: err"; exit 1; }'
   TMP="$(mktemp /tmp/mktemp-XXX.sh)"
   sed \
      -e "s/@ABRTEXIT@/$ABRTEXIT/g" \
      -e "s/@ABRTRET@/$ABRTRET/g" \
      SCRIPT.sh \
      > "$TMP"
   printf "\e[32m%s\e[0m\n" "running $TMP ..."
   bash "$TMP"

when you have no choice but to pass executable as ``$1``

.. code:: shell-session

   $ /usr/lib/ld-linux-x86-64.so.2 "$(which uname)" -r
   Linux

change terminal emulator title ::

   printf "\e]0;TITLE\a"

horizontal separator ruler / transition line / <hr> ::

   for _ in $(seq 1 "$(tput cols)"); do
     echo -n '-'
   done
   echo
   unset -v _

| :manpage:`console_codes(4)`
| |:red_circle:| :
| ``printf "\n\e[31m  %s\e[0m\n\n" "err"``
| |:green_circle:| :
| ``printf "\n\e[32m  %s\e[0m\n\n" "ok"``
| |:brown_circle:| :
| ``printf "\n\e[33m  %s\e[0m\n\n" "warning"``
| |:blue_circle:| :
| ``printf "\n\e[34m  %s\e[0m\n\n" "info"``
| console_codes(4)
|    - `Linux console controls <https://man.archlinux.org/man/console_codes.4#Linux_console_controls>`__
|       - ECMA-48 Select Graphic Rendition
|          - *2 set half-bright (simulated with color on a color display)*
| ``printf "\e[2;37m  %s\e[0m\n\n" "hint"``
| ``printf "\e[2m  %s\e[0m\n\n" "hint"``

zip archive mojibake ::

   unzip -O sjis SHIFTJIS.ZIP
   unzip -O cp936 GBK.ZIP

`process tree better than pstree <https://unix.stackexchange.com/a/436579>`__ ::

   ps -aef --forest | less -SRM +%

reverse video time stamp ::

   printf "\n\e[7m  %s  \e[0m\n\n" "$(date)"

`kernel module parameters <https://askubuntu.com/q/59135>`__ ::

   modinfo nfsd \
     | grep '^parm:' \
     | cut -d' ' -f12- \
     | sed -E -e 's/^([^:]+):(.+)$/\1:\n  \2\n/g' \
     | less -F +X -S

::

   modinfo -p nfs \
     | sed -E -e 's/^([^:]+):(.+)$/\1:\n  \2\n/g' \
     | less -F +X -S

`How to read the whole shell script before executing it? <https://unix.stackexchange.com/q/331837/>`__ ::

   #!/bin/bash
   function main {
      foo
      bar
   }
   main "$@"; exit

::

   #!/bin/bash
   {
      foo
      bar
   }; exit

| test symbolic link
| python :file:`~/archiso/demo_dfel.py`

::

   echo
   cd /tmp
   rm -rf /tmp/x
   mkdir $_
   cd $_
   mkdir dir
   ln -sv "dir" lnk
   function test2 {
      printf -- "%5s " "$1"
      for o in -d -e -f -L; do
         if [ "$o" "$1" ]; then
            printf -- "$o true  ";
         else
            printf -- "$o false ";
         fi
      done
      echo
   }
   test2 dir
   test2 lnk
   echo
   rmdir -v dir
   test2 lnk
   echo

.. table::
   :align: left
   :widths: auto

   ================================= ================== ================== ================== ==================
    type                              -d                 -e                 -f                 -L
   ================================= ================== ================== ================== ==================
    \
    file                              |:red_circle:|     |:green_circle:|   |:green_circle:|   |:red_circle:|
    dir                               |:green_circle:|   |:green_circle:|   |:red_circle:|     |:red_circle:|
    \
    symlink2file                      |:red_circle:|     |:green_circle:|   |:green_circle:|   |:green_circle:|
    symlink2dir                       |:green_circle:|   |:green_circle:|   |:red_circle:|     |:green_circle:|
    \
    deadlink2file |br| deadlink2dir   |:red_circle:|     |:red_circle:|     |:red_circle:|     |:green_circle:|
    \
    nonexist                          |:red_circle:|     |:red_circle:|     |:red_circle:|     |:red_circle:|
   ================================= ================== ================== ================== ==================

xdotool ::

   xdotool search --desktop 0 Chromium windowactivate

unicode to hex escape ``\x??`` ::

   # https://stackoverflow.com/q/5724761/ascii-hex-convert-in-bash/
   # https://unix.stackexchange.com/q/467310/how-to-include-a-backslash-in-the-hexdump-output-format-string
   function s2h {
     printf "\n"
     printf %s 'echo -e "'
     printf %s "$1" \
       | hexdump -v -e '"\\" 1/1 "x%x"'
     printf "%s\n" \"
     printf "\n"
   }

   s2h "こんにちは"


| :manpage:`bash(1)`
  - Parameter Expansion
  - ``parameter ... shell parameter ... or an array reference``

::

   # Remove matching prefix pattern
   ${parameter#word}
   ${pm_Arr[@]#word}

   # Remove matching suffix pattern
   ${parameter%word}
   ${pm_Arr[@]%word}

| find
  `recently modified <https://unix.stackexchange.com/q/33850/>`__
  C source file,
  `excluding dir <https://stackoverflow.com/q/4210042/>`__
| |:warning:| ``-o`` after -prune

::

   find /home/darren \
     -path /home/darren/.cache/paru/clone -prune -o \
     -type f \
     -name '*.c' \
     -mtime -30 \
     |& fgrep -v '’: Permission denied'

| :pmos:`to run applications in i3 from console, set up your environment similar to the environment in which i3 is running <Plasma Mobile#Running_Apps_from_SSH_session>`
| not only ``DISPLAY``

::

   [ "1" = "$(pidof i3 | wc -w)" ] && {
      export $(cat /proc/$(pidof i3)/environ | tr '\0' '\n')
      alacritty
   }

xrandr ::

   # dell U2417H
   xrandr --output DP-1 --mode 1920x1080 --right-of eDP-1 --rotate left

| :pr:`woeusb-ng`
| woeusb 5.2.4

::

   
   sudo woeusb \
      --workaround-bios-boot-flag \
      --tgt-fs FAT \
      -d /home/darren/Downloads/en-us_windows_10_enterprise_ltsc_2021_x64_dvd_d289cf96.iso \
      /dev/sda

| :manpage:`sed(1)` append text after matched line
| |b| Zero- or One- address commands |rarr| ``a \ text`` |rarr| Append text
| |b| Addresses |rarr| ``/regexp/`` |rarr| Match lines matching the regular expression regexp
| |rarr| `README.profile.rst <https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.profile.rst>`__ - #airootfs

::

   sed -e "/^file_permissions=(/a $APPEND" "$RELENG/profiledef.sh" >"$ARCHLIVE/profiledef.sh"


C
===

.. highlight:: C

WIP move everything from :file:`~/cheatsheet.c`

:wp:`C11 extensions <C11_(C_standard_revision)#Changes_from_C99>`

`cdecl: C gibberish ↔ English <https://cdecl.org/>`__

| `Sparse, Smatch, and Coccinelle <https://thenewstack.io/checking-linuxs-code-with-static-analysis-tools/>`__\ [#]_
| |b| :wp:`Coccinelle_(software)`
| gcc `-fanalyzer <https://developers.redhat.com/blog/2020/03/26/static-analysis-in-gcc-10>`__
| `splint <https://github.com/splintchecker/splint>`__

compile flags ::

   -std=gnu11 -g -O0 -Wextra -Wall -Winline -Wshadow -fanalyzer -o a.out

stringify macro ::

   #define STR0(x) #x
   #define STR(x) STR0(x)

range-based for loop macro ::

   #define for_range_int(var,range) for(size_t var=0;var<sizeof(range)/sizeof(int);++var)
   int arr[]={19,89,6,4}
   for_range_int(i,arr){
      printf("%d ",arr[i]);
   }
   puts("");

instant linked list ::

   typedef struct _Node{
     int ele;
     struct _Node *next;
   } Node;
   #define M malloc(sizeof(Node))
   Node *root=M;
   *(*(*(*
     root=(Node){1,M}
   ).next=(Node){2,M}
   ).next=(Node){3,M}
   ).next=(Node){4,M};

eprintf macro ::

   #define eprintf(...) fprintf(stderr,__VA_ARGS__)

lambda macro ::

   #define LAMBDA(X) ({ X f;})
   g_array_sort(edges,LAMBDA(gint f(const void *x,const void *y){
     return ((Edge*)x)->weight - ((Edge*)y)->weight ;
   }));

dump contents of ``FILE *stdin`` to ``char *buf`` ::

   #include <stdio.h>
   assert(
     0==fseek(stdin,0,SEEK_END) &&
     0==feof(stdin) &&
     0==ferror(stdin)
   );
   const long l=ftell(stdin);
   char *buf=calloc(1,l+1);
   assert(buf);
   rewind(stdin);
   assert((long long)l==(long long)fread(buf,1,l,stdin));
   assert(0==fclose(stdin));
   // ...
   free(buf);buf=NULL;

gperf gprof valgrind kcachegrind flamegraph ...
`1 <https://daiwk.github.io/posts/knowledge-gperftools.html>`__
`2 <https://gernotklingler.com/blog/gprof-valgrind-gperftools-evaluation-tools-application-level-cpu-profiling-linux/>`__
`3 <https://github.com/brendangregg/FlameGraph>`__
`4 <https://oprofile-list.sf.narkive.com/tdvTGecS/oprofile-vs-perf-vs-gperf>`__

`temporarily suppress a warning <https://stackoverflow.com/questions/3378560/how-to-disable-gcc-warnings-for-a-few-lines-of-code>`__ ::

   #pragma GCC diagnostic push
   #pragma GCC diagnostic ignored "-Wsequence-point"
   #pragma GCC diagnostic pop

:manpage:`getopt(3)`

.. table:: argv
   :align: left
   :widths: auto

   ======= ===================
    -abc    option element
    a b c   option characters
   ======= ===================

.. table:: optstring
   :align: left
   :widths: auto

   ============== =======================
    \...x...       switch
    \...x:...      requires an argument
    \...x\:\:...   takes an optional arg
    +...           $POSIXLY_CORRECT
   ============== =======================

`encrypt text with ssh rsa public key <https://superuser.com/questions/576506/how-to-use-ssh-rsa-public-key-to-encrypt-a-text>`__ ::

   ssh-keygen -f ~/.ssh/id_rsa.pub -e -m PKCS8 >~/.ssh/id_rsa.pub.pem
   cat <<EOF | openssl rsautl -encrypt -pubin -inkey ~/.ssh/id_rsa.pub.pem -ssl | base64 -w0

::

   This is a secret.
   EOF

decrypt ::

   base64 -d <<EOF | openssl rsautl -decrypt -inkey ~/.ssh/id_rsa

::

   ...
   EOF

awesome-c
|vv| `oz123 <https://github.com/oz123/awesome-c>`__
|vv| `inputsh <https://github.com/inputsh/awesome-c>`__
|vv| `uhub <https://github.com/uhub/awesome-c>`__
|vv| `Bfgeshka <https://github.com/Bfgeshka/awesome-c#json>`__
|vv| `mazurov <https://notabug.org/mazurov/awesome-c>`__


FFmpeg
======

bannerbear/`adding soft subtitles <https://www.bannerbear.com/blog/how-to-add-subtitles-to-a-video-file-using-ffmpeg/#adding-soft-subtitles>`__ ::

   ffmpeg -i <Vin> -i <SRT> -c copy -c:s mov_text -metadata:s:s:0 language=eng <Vout>

| bannerbear/`adding hard subtitles <https://www.bannerbear.com/blog/how-to-add-subtitles-to-a-video-file-using-ffmpeg/#adding-hard-subtitles>`__
| ffmpegwiki/`burn text subtitles <https://trac.ffmpeg.org/wiki/HowToBurnSubtitlesIntoVideo>`__

::

   ffmpeg -i <Vin> -vf subtitles=<SRT> <Vout>

| ffmpegwiki/`map <https://trac.ffmpeg.org/wiki/Map>`__
| \
      take y0\ :sup:`th` stream from x0\ :sup:`th` file, ...,
  and take yN\ :sup:`th` stream from xN\ :sup:`th` file,
  then merge them into Vout

::

   ffmpeg \
      -i <Vin0> ... -i <VinM> \
      -map x0:y0 -c copy ... -map xN:yN -c copy \
      <Vout>

convert mkv subtitles (subrip srt) to mp4 subtitles (mov_text) ::

   ffmpeg -i <IN.MKV> -c copy -map 0:0 -map 0:1 va.mp4
   ffmpeg -i <IN.MKV> -map 0:10 tmp.srt
   ffmpeg -i va.mp4 -i tmp.srt -c:v copy -c:a copy -c:s mov_text <OUT.MP4>

| video/audio sync
| ffmpegwiki/`-itsoffset <https://trac.ffmpeg.org/wiki/UnderstandingItsoffset>`__

::

   yt-dlp -f137 -o v.mp4 "https://www.youtube.com/watch?v=EVAckHD9o0Y"
   yt-dlp -f140 -o a.m4a "https://www.youtube.com/watch?v=np42odaM8jw"

   # ffmpeg -i v.mp4 -i a.m4a -c copy mismatch.mp4

   # Checkpoints
   # A 00:42
   # A 02:25

   # org.openshot.OpenShot
   : [Menu Bar] -- [View] -- [Views] -- [Advanced View]
   : [Menu Bar] -- [File] -- [Import Files...] -- a.m4a
   : [Menu Bar] -- [File] -- [Import Files...] -- v.mp4
   : drag v.mp4 from [Project Files] to [Timeline] -- [Track...]
   : drag a.m4a from [Project Files] to [Timeline] -- [Track...]
   : drag [Video Preview] panel to [OpenShot Video Editor] title bar, then move it to a new wm workspace
   : [Timeline] -- [Track...] -- v.mp4 -- Mouse.RightClick -- [Properties] -- Position=5.30
   : [Video Preview] -- play

   # apply
   ffmpeg \
      -i v.mp4 \
      -itsoffset -5.30 -i a.m4a \
      -c copy va.mp4

   scp va.mp4 x200:/NOBACKUP/Do.You.Know.Hip.Hop.너희가.힙합을.아느냐.mp4

youtube subtitles vtt2srt ::

   export HTTP_PROXY=192.168.0.223:8080 HTTPS_PROXY=192.168.0.223:8080

   yt-dlp --skip-download --list-subs ...

   CMD=(
     yt-dlp
     https://youtu.be/wlyRGXUwjVA
     -f140+137
     --write-subs --sub-format vtt --sub-langs id
     -o orig
   )

   "${CMD[@]}"

   ffmpeg -i orig.id.vtt -c:s srt orig.srt

   /usr/local/bin/subtitles3.sh orig.srt >3.srt

   ffmpeg \
      -i orig.mp4 -i 3.srt \
      -c copy \
      -metadata:s:1 language=ind \
      -metadata:s:2 language=ind \
      Bebas3.mkv

/usr/local/bin/subtitles3.sh





GDB
===

.. highlight:: text

break at label ::

   b [<file>:]<function>:<label>


Git
===

.. highlight:: bash

convert shallow clone to full ::

   git clone --depth=1 https://github.com/libgit2/libgit2
   cd libgit2
   git fetch --unshallow

`drop changes from staging area <https://stackoverflow.com/q/66465810#comment121377736_66470532>`__ ::

   git restore -SW -- FILE

diff

.. table::
   :align: left
   :widths: auto

   +-------------+----------+---------------------------------------+
   | worktree vs | commit   | :file:`git diff -R <commit>`          |
   |             +----------+---------------------------------------+
   |             | staging  | :file:`git diff -R`                   |
   +-------------+----------+---------------------------------------+
   | staging vs  | worktree | :file:`git diff`                      |
   |             +----------+---------------------------------------+
   |             | commit   | :file:`git diff -R --staged <commit>` |
   +-------------+----------+---------------------------------------+
   | commit vs   | staging  | :file:`git diff --staged <commit>`    |
   |             +----------+---------------------------------------+
   |             | worktree | :file:`git diff <commit>`             |
   |             +----------+---------------------------------------+
   |             | commit   | :file:`git diff <commit> <commit>`    |
   +-------------+----------+---------------------------------------+

submodules.full.oneshot ::

   git clone --recurse-submodules URL

submodules.full.2step ::

   git clone URL
   cd REPO
   git submodule update --init --progress --recursive

submodules.shallow.oneshot ::

   git clone --depth 1 --recurse-submodules --shallow-submodules URL

submodules.update ::

   git submodule update --progress --depth 1
   git submodule status --recursive

delete remote branch

.. code:: bash

   git push -u origin ':main'

| `checking out pull requests locally <https://docs.github.com/en/github/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally>`__
| `clone from pull request <https://stackoverflow.com/questions/14947789>`__

::

   mkdir -pv /tmp/genimage
   cd /tmp/genimage
   git init
   git remote add origin git@github.com:pengutronix/genimage.git
   git fetch origin pull/166/head --depth=1
   git checkout -b pr166 FETCH_HEAD

Filter-Repo
-----------

.. warning::

   | Once ``git filter-repo`` is run, any matched files are removed forever |dumpster_fire|
   | For backing up locally, modify is easily and catastrophically `confused with <grammar/comments/39yc0i/>` orig,
   |  |:o:| ``rm -rf modify; cp -a orig   modify``
   |  |:x:| ``rm -rf orig;   cp -a modify orig`` |:radioactive:| |:boom:|
   | Recommended SOP
   |  1\. sync all branches, make sure local and remote are at the exact same state
   |  2\. (remote) move repo to :file:`repo.private.archived`
   |  3\. (remote) recreate blank repog
   |  4\. (local) do the housekeeping
   |  5\. (local) push to the recreated blank remote
   |  6\. leave :file:`repo.private.archived` unattended for a sufficient period of time
   | Benefits
   |  |b| possible to recover from readonly :file:`repo.private.archived` at any time
   |  |b| drops `blobs only accessible via their SHA-1 hashes in cached views <https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>`__

| `removing sensitive data from a repository <https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>`__
| `git tools - rewriting history <https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History>`__

| :manpage:`git-filter-branch(1)`
| |b| recommended **against** in :manpage:`git-filter-branch(1)`
| |b| ``-d /tmp``

| `bfg-repo-cleaner <https://rtyley.github.io/bfg-repo-cleaner/>`__
| |b| ask :pkg:`AUR/bfg` to rename to :pkg:`AUR/bfg-bin`
| |b| create :pkg:`AUR/bfg` according to :pkg:`AUR/bfg-git`
| |b| :aw:`scala` - `sbt <https://www.scala-sbt.org/>`__ - /`build.sbt <https://github.com/rtyley/bfg-repo-cleaner/blob/master/build.sbt>`__

| :pkg:`community/git-filter-repo` - `github repo <https://github.com/newren/git-filter-repo>`__
| |b| arch :manpage:`git-filter-repo(1)`
| |b| official `git-filter-repo.1 <https://www.mankier.com/1/git-filter-repo>`__
| |b| recommended in :manpage:`git-filter-branch(1)`
| |b| `repo-filter vs bfg <https://github.com/newren/git-filter-repo/blob/main/Documentation/converting-from-bfg-repo-cleaner.md#deleting-files>`__
| |b| `<https://git.github.io/rev_news/2019/08/21/edition-54/#an-introduction-to-git-filter-repo--written-by-elijah-newren>`__

find deleted files ::

   env COLUMNS=99 git --no-pager log --oneline --compact-summary --diff-filter='DTUXB' | grep Bin
   env COLUMNS=99 git --no-pager log --oneline --stat            --diff-filter='DTUXB' | grep Bin
   git log --oneline --stat --diff-filter='DTUXB'
   git log --oneline --name-status --diff-filter='DTUXB'
   git log --oneline --name-status --diff-filter='DRTUXB'
   git log --oneline --name-status --diff-filter='DTUXB*'

local fresh clone ::

   cd /tmp
   git clone --no-local PATH_TO_ORIG_REPO /tmp/REPO.filter
   cd REPO.filter/

remove leftovers ::

   rm -rfv .git/filter-repo

analyze ::

   git filter-repo --analyze
   subl .git/filter-repo/analysis/path-deleted-sizes.txt
   # subl .git/filter-repo/analysis/path-all-sizes.txt
   # subl .git/filter-repo/analysis/extensions-deleted-sizes.txt
   # subl .git/filter-repo/analysis/extensions-all-sizes.txt
   # for i in .git/filter-repo/analysis/*; do
   #    printf "\n  %s\n\n" "$i"
   #    cat "$i"
   # done

| strip everything other than filenames from :file:`path-deleted-sizes.txt`
| sort the filenames
| paste to :manpage:`meld(1)`

discard files from git history ::

   CMD=(git filter-repo --invert-paths)
   while IFS= read -r line; do
      CMD+=(--path-match "$line")
      # echo "#$line#"
   done <.git/filter-repo/analysis/path-deleted-sizes.txt
   CMD+=(--use-base-name)
   "${CMD[@]}"

view change logs ::

   for i in .git/filter-repo/*; do printf "\n  %s\n\n" "$i"; cat "$i"; done

remove change logs ::

   rm -rv .git/filter-repo

gc ::

   git gc --aggressive --prune=now

analyze, strip and paste again, then compare in meld

remove leftovers ::

   rm -rfv .git/filter-repo

add remote ::

   git remote add origin "$(git -C PATH_TO_ORIG_REPO remote get-url origin)"
   git remote -v

force push, track all ::

   git push -u origin --all

check remote on web

`quote <https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>`__

.. code:: text

   make commits with sensitive data unreachable from any branches or tags in your GitHub repository
   however ... may still be accessible ... clones or forks .. SHA-1 hashes in cached views[1] .. pull requests
   [1]: https://github.com/Un1Gfn/sphinx.public/tree/[0-9a-z]{40}

| to drop them from github, either
| |b| delete and recreate repo, then adjust the default branch; or
| |b| contact `GitHub Support <https://support.github.com/contact?tags=docs-generic>`__

remove PATH_TO_ORIG_REPO

ImageMagick
===========

.. highlight:: bash

misc (please split this blob) ::

   #!/dev/null

   magick convert -size 4096x2048 xc:#0000AA Blue.png

   magick convert -size 4096x4096 -background 'rgb(0,0,170)' Emblem_of_the_Kuomintang.svg Emblem_of_the_Kuomintang.png
   magick convert -size 1024x1024 -background 'rgb(0,0,170)' -blur 0x64 Emblem_of_the_Kuomintang.svg Emblem_of_the_Kuomintang.blurred.png

   cd /tmp
   magick convert -size 1024x1024 -background 'rgb(255,255,255)' Network-e72c038278.svg Network-e72c038278.png
   magick convert -size 1024x1024 -background 'rgb(255,255,255)' Network-8f37df9f10.svg Network-8f37df9f10.png

   rm -fv Emblem_of_Okinawa_County*
   P="Emblem_of_Okinawa_Prefecture"
   C1="Emblem_of_Okinawa_County1"
   C2="Emblem_of_Okinawa_County2"
   cat "$T.svg" \
     | sed -e "s/fill:#ffffff/fill:#0000AA/g" \
     | sed -e "s/fill:#c90037/fill:#ffffff/g" \
     > "$C1.svg"
   cat "$T.svg" \
     | sed -e "s/fill:#c90037/fill:#0000AA/g" \
     > "$C2.svg"
   convert -size 2048x2048 -background 'rgb(  0,  0,170)' "$C1.svg" "$C1.png"
   convert -size 2048x2048 -background 'rgb(255,255,255)' "$C2.svg" "$C2.png"

   Hsiao-Feng_Yin
   Hiu-Fung_Wan ♂️ ♂
   尹曉風 ♂️ ♂
   尹曉風 ♂️
   1949年17歲 生日1932-02-18
   https://home.gamer.com.tw/creationDetail.php?sn=3670959
   https://truth.bahamut.com.tw/s01/201708/8148c7ea0e4fd05a31d1b39875709bf5.JPG?w=1000
   convert -define jpeg:size=401x696 Hiu-Fung_Wan.jpeg -thumbnail 401x401^ -gravity North -extent 401x401 Hiu-Fung_Wan.png

crop and resize ::

   W=$((360*2))
   H=$((480*2))
   I="$HOME/Telegram Desktop/photo_2021-09-01_14-17-35.jpg"
   O="/tmp/resize.jpg"
   echo
   magick convert "$F" -gravity center -crop 3:4 -resize "${W}x${H}" "$O"
   echo
   file "$O"
   echo
   ls -lh "$O"
   echo

| `view binary data as image <https://superuser.com/q/294270/>`__
| |b| refer to corebootlibreboot\:\ :ref:`BMP <ref_label_imagemagick_bin2bmp_diff>`

rotate ::

   for i in IMG_????; do
      magick convert -rotate 270 -quality 100 "${i}"{_ORIG,}.HEIC
   done

`square and pad with transparency <https://stackoverflow.com/a/34992414/>`__ ::

   magick convert -background none -gravity center /tmp/spcl_logo.png -resize 172x172 -extent 172x172 /tmp/o.png




Makefile
========

`Appendix A Quick Reference <https://www.gnu.org/software/make/manual/html_node/Quick-Reference.html>`__

`Special Built-in Target Names <https://www.gnu.org/software/make/manual/html_node/Special-Targets.html>`__

.. highlight:: bash

see the full list of `default rules and variables <https://www.gnu.org/software/make/manual/html_node/Catalogue-of-Rules.html>`__::

   make -p -f/dev/null >/tmp/default.Makefile

.. highlight:: Makefile

::

   COMPILE.c = $(CC) $(CFLAGS) $(CPPFLAGS) $(TARGET_ARCH) -c
   %.o: %.c
      $(COMPILE.c) $(OUTPUT_OPTION) $<

::

   LINK.o = $(CC) $(LDFLAGS) $(TARGET_ARCH)
   %: %.o
      $(LINK.o) $^ $(LOADLIBES) $(LDLIBS) -o $@
   .o:
      $(LINK.o) $^ $(LOADLIBES) $(LDLIBS) -o $@

::

   LINK.c = $(CC) $(CFLAGS) $(CPPFLAGS) $(LDFLAGS) $(TARGET_ARCH)
   %: %.c
      $(LINK.c) $^ $(LOADLIBES) $(LDLIBS) -o $@

| `Automatic Variables <https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html>`__
| \
  :makevar:`$@`
  :makevar:`$<`
  :makevar:`$^`
  :makevar:`$(@D)`
  :makevar:`$(<D)`
  :makevar:`$(^D)`
  :makevar:`$(@F)`
  :makevar:`$(<F)`
  :makevar:`$(^F)`
| \
  :makevar:`$%`
  :makevar:`$?`
  :makevar:`$+`
  :makevar:`$*`
  :makevar:`$(%D)`
  :makevar:`$(?D)`
  :makevar:`$(+D)`
  :makevar:`$(*D)`
  :makevar:`$(%F)`
  :makevar:`$(?F)`
  :makevar:`$(+F)`
  :makevar:`$(*F)`
| \
  :makevar:`$|`

`Functions for String Substitution and Analysis
<https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#Text-Functions>`__ ::

   $(word 2,$^)
   $(filter-out $<,$^)
   $(filter-out $(word 3,$^),$^)

recursively remove binary ::

   clean:
   	find . -type f -a \( -name "*.o" -o -name "*.out" \) -exec rm -v {} \;

`PlantUML <https://plantuml.com/>`__ ::

   clean:
   	@find .                                          \
   		-type f                                       \
   		-a                                            \
   		\(                                            \
   			-name 'DUMMY'                              \
   			-o -name "*.o"                             \
   			-o -name "*.out"                           \
   			-o -name "puml_*.eps"                      \
   			-o -name "puml_*.pdf"                      \
   			-o -name "puml_*.png"                      \
   			-o -name "puml_*.svg"                      \
   		\)                                            \
   		-a                                            \
   		\(                                            \
   			-not -name 'DUMMY'                         \
   			-a -not -name "puml_cdecl.svg"             \
   			-a -not -name "puml_submit_divl_lib32.svg" \
   			-a -not -name "puml_utos.svg"              \
   		\)                                            \
   		-exec rm -v {} \;


Tar
===

.. highlight:: bash

`flatten entire archive <https://stackoverflow.com/a/14295908/>`__ ::

   tar xzf archive.tgz --transform='s/.*\///'

extract single file ::

   tar -x -f /customrepo/libim*glue*.tar.zst usr/lib/libimobiledevice-glue-1.0.so.0.0.0 -v --xform='s,.*/,,'


Verilog
=======

.. highlight:: verilog

`assertion <https://stackoverflow.com/a/31302223>`__ ::

   `define assert(signal,value) \
   if(signal!==value)begin \
       $display("ASSERTION FAILED in %m: signal != value"); \
       $finish; \
   end

   // ui.out: ui.c:21: shm_connect: Assertion `shmid>=0' failed.

   if()begin
     $display("%s:%03d: %m: Assertion failed.",`__FILE__,`__LINE__);
     $finish();
   end

timeout ::

   initial begin #100 $finish;

conditional VCD dump ::

   `ifdef VCD
     initial begin
       $dumpfile(`VCD);
       $dumpvars;
     end
   `endif

Footnotes
=========

.. [#] Used by U-Boot. ``make help | grep cocci``
