#!/dev/null
# shellcheck shell=bash

# Define everything in a function so that we can terminate immediately with "return"

function hr {
  for _ in $(seq 1 "$(tput cols)"); do
    echo -n '-'
  done
  echo
  unset -v _
}

function f {

  hr

  # Run shellcheck
  /usr/lib/ld-2.33.so /usr/bin/shellcheck ~/beaglebone/u-boot.bashrc

  # https://stackoverflow.com/a/23418127
  # shopt nullglob | hexdump -v -C -c
  local ng
  ng="$(shopt nullglob)"
  { [ "$?" -eq 1 ] && [ "$ng" = "nullglob       "$'\t'"off" ]; } || { echo "${BASH_SOURCE[0]}:$LINENO: err"; return 1; }
  unset -v ng

  # grep -n -s -I -Ee '[^0-9a-zA-Z](yY|Yy)[^0-9a-zA-Z]' /usr/bin/* 2>/dev/null
  # if [[ "$yn" =~ ^[yY][eE][sS]$ ]]; then
  shopt -s nullglob
  for D in u-boot-*/; do
    # Annoying "write-protected"
    # printf "\e[7m%s\e[27m " "${D:?}" && rm -rIf "${D:?}"
    echo -n "remove ${D:?}? [y/N] "
    read -r yn
    [ "$yn" = "y" ] && rm -rf "$D" && echo "removed '$D'"
    unset -v yn
    echo
  done
  unset -v D
  shopt -u nullglob

  # Append to the end of PATH instead of adding to the beginning in case /usr/bin/gcc get masked out
  # export PATH="$PATH:/usr/lib/distcc/"
  export PATH="$PATH:/opt/x-tools7h/arm-unknown-linux-gnueabihf/bin/"
  export CROSS_COMPILE="armv7l-unknown-linux-gnueabihf-"
  export KBUILD_OUTPUT="O"
  hash -r
  ${CROSS_COMPILE}gcc --version | grep -q cross \
    || { echo "${BASH_SOURCE[0]}:$LINENO: err"; return 1; }
  gcc                 --version | grep    cross \
    ;  [ "$?" -eq 1 ] \
    || { echo "${BASH_SOURCE[0]}:$LINENO: err"; return 1; }

  # printf "\e]0;%s\a" "${PWD##*/}"
  echo "PATH=$PATH" && echo
  file "$(which "${CROSS_COMPILE}gcc")" && echo
  [ -L "$(which "${CROSS_COMPILE}gcc")" ] && file "$(realpath "$(which "${CROSS_COMPILE}gcc")")" && echo
  file "$(which gcc)"
  # echo "KBUILD_OUTPUT=$KBUILD_OUTPUT"; echo

  hr

}

f

unset -f hr
unset -f f
