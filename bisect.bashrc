#!/dev/null

function f {

  # https://stackoverflow.com/a/8796647
  # git show-ref --tags -d | grep -F 'v2021.01^{}'
  # git show-ref --tags -d | grep -F 'v2020.10^{}'
  # git show-ref v2021.01 -d
  # git show-ref v2020.10 -d

  # https://stackoverflow.com/a/1862542
  # https://stackoverflow.com/a/24469132
  [ "$(git rev-list -n 1 v2021.01)" = c4fddedc48f336eabc4ce3f74940e6aa372de18c ] || echo err
  [ "$(git rev-list -n 1 v2020.10)" = 050acee119b3757fee3bd128f55d720fdd9bb890 ] || echo err
  [ "$(git rev-parse --verify 'v2021.01^{}')" = c4fddedc48f336eabc4ce3f74940e6aa372de18c ] || echo err
  [ "$(git rev-parse --verify 'v2020.10^{}')" = 050acee119b3757fee3bd128f55d720fdd9bb890 ] || echo err
  [ "$(git rev-parse --verify 'v2021.01^{commit}')" = c4fddedc48f336eabc4ce3f74940e6aa372de18c ] || echo err
  [ "$(git rev-parse --verify 'v2020.10^{commit}')" = 050acee119b3757fee3bd128f55d720fdd9bb890 ] || echo err

  # Deleted
  # git log --name-status -- configs/am335x_boneblack_defconfig

  # Generic
  # git log -- configs/am335x_evm_defconfig

  # Problematic
  # git log --compact-summary -- configs/am335x_boneblack_vboot_defconfig

  local L='git log --oneline --decorate --graph --no-abbrev-commit'
  diff -u <($L v2020.10^...v2021.01) <($L v2020.10^..v2021.01) || echo err

  alias l2="$L v2020.10^..v2021.01"

}

f
unset -v f
