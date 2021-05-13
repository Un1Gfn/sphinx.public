<!-- alarm.md -->

---

&bullet; [u-boot.md](https://github.com/Un1Gfn/beaglebone/blob/master/u-boot.md)\
**&#9656; alarm.md**\
&bullet; [readme.md](https://github.com/Un1Gfn/beaglebone)

---

<!-- NAV_END -->

## &AElig; - Misc 1

alarm &equiv; **A**rch **L**inux **ARM**

[Monitor Commands - Overview](https://source.denx.de/u-boot/u-boot/-/blob/master/README#L3129)

Clear screen\
1&period; <kbd>Space</kbd>\
2&period; <kbd>Ctrl</kbd>+<kbd>A</kbd>\
3&period; <kbd>C</kbd>\
4&period; <kbd>Ctrl</kbd>+<kbd>;</kbd>\
5&period; <kbd>Enter</kbd>

<details><summary>printenv</summary>

```
addr_fit=0x90000000
arch=arm
args_mmc=run finduuid;setenv bootargs console=${console} ${optargs} root=PARTUUID=${uuid} rw rootfstype=${mmcrootfstype}
baudrate=115200
board=am335x
board_name=BBGW
board_rev=GW1A
board_serial=BBGW16054424
boot_a_script=load ${devtype} ${devnum}:${distro_bootpart} ${scriptaddr} ${prefix}${script}; source ${scriptaddr}
boot_efi_binary=load ${devtype} ${devnum}:${distro_bootpart} ${kernel_addr_r} efi/boot/bootarm.efi; if fdt addr ${fdt_addr_r}; thei
boot_efi_bootmgr=if fdt addr ${fdt_addr_r}; then bootefi bootmgr ${fdt_addr_r};else bootefi bootmgr;fi
boot_extlinux=sysboot ${devtype} ${devnum}:${distro_bootpart} any ${scriptaddr} ${prefix}${boot_syslinux_conf}
boot_fdt=try
boot_fit=0
boot_net_usb_start=usb start
boot_prefixes=/ /boot/
boot_script_dhcp=boot.scr.uimg
boot_scripts=boot.scr.uimg boot.scr
boot_syslinux_conf=extlinux/extlinux.conf
boot_targets=mmc0 legacy_mmc0 mmc1 legacy_mmc1 nand0 usb0 pxe dhcp
bootcmd=if test ${boot_fit} -eq 1; then run update_to_fit; fi; run findfdt; run init_console; run envboot; run distro_bootcmd
bootcmd_dhcp=setenv devtype dhcp; run boot_net_usb_start; if dhcp ${scriptaddr} ${boot_script_dhcp}; then source ${scriptaddr}; fi;
bootcmd_legacy_mmc0=setenv mmcdev 0; setenv bootpart 0:2 ; run mmcboot
bootcmd_legacy_mmc1=setenv mmcdev 1; setenv bootpart 1:2 ; run mmcboot
bootcmd_mmc0=devnum=0; run mmc_boot
bootcmd_mmc1=devnum=1; run mmc_boot
bootcmd_nand=run nandboot
bootcmd_pxe=run boot_net_usb_start; dhcp; if pxe get; then pxe boot; fi
bootcmd_usb0=devnum=0; run usb_boot
bootdir=/boot
bootenvfile=uEnv.txt
bootfile=zImage
bootm_size=0x10000000
bootpart=0:2
bootscript=echo Running bootscript from mmc${mmcdev} ...; source ${loadaddr}
console=ttyO0,115200n8
cpu=armv7
dfu_alt_info_emmc=rawemmc raw 0 3751936;boot part 1 1;rootfs part 1 2;MLO fat 1 1;MLO.raw raw 0x100 0x100;u-boot.img.raw raw 0x3001
dfu_alt_info_mmc=boot part 0 1;rootfs part 0 2;MLO fat 0 1;MLO.raw raw 0x100 0x100;u-boot.img.raw raw 0x300 0x1000;u-env.raw raw 01
dfu_alt_info_nand=SPL part 0 1;SPL.backup1 part 0 2;SPL.backup2 part 0 3;SPL.backup3 part 0 4;u-boot part 0 5;u-boot-spl-os part 09
dfu_alt_info_ram=kernel ram 0x80200000 0x4000000;fdt ram 0x80f80000 0x80000;ramdisk ram 0x81000000 0x4000000
distro_bootcmd=for target in ${boot_targets}; do run bootcmd_${target}; done
dtboaddr=0x89000000
efi_dtb_prefixes=/ /dtb/ /dtb/current/
envboot=mmc dev ${mmcdev}; if mmc rescan; then echo SD/MMC found on device ${mmcdev};if run loadbootscript; then run bootscript;el;
eth1addr=88:c2:55:81:a8:5a
eth2addr=88:c2:55:81:a8:58
eth3addr=de:ad:be:ef:00:01
ethaddr=88:c2:55:81:a8:58
fdt_addr_r=0x88000000
fdtaddr=0x88000000
fdtcontroladdr=9df38010
fdtfile=undefined
findfdt=if test $board_name = A335BONE; then setenv fdtfile am335x-bone.dtb; fi; if test $board_name = A335BNLT; then setenv fdtfi
finduuid=part uuid mmc ${bootpart} uuid
get_overlaystring=for overlay in $name_overlays;do;setenv overlaystring ${overlaystring}'#'${overlay};done;
importbootenv=echo Importing environment from mmc${mmcdev} ...; env import -t ${loadaddr} ${filesize}
init_console=if test $board_name = A335_ICE; then setenv console ttyO3,115200n8;else setenv console ttyO0,115200n8;fi;
kernel_addr_r=0x82000000
load_efi_dtb=load ${devtype} ${devnum}:${distro_bootpart} ${fdt_addr_r} ${prefix}${efi_fdtfile}
loadaddr=0x82000000
loadbootenv=fatload mmc ${mmcdev} ${loadaddr} ${bootenvfile}
loadbootscript=load mmc ${mmcdev} ${loadaddr} boot.scr
loadfdt=load ${devtype} ${bootpart} ${fdtaddr} ${bootdir}/${fdtfile}
loadimage=load ${devtype} ${bootpart} ${loadaddr} ${bootdir}/${bootfile}
loadramdisk=load mmc ${mmcdev} ${rdaddr} ramdisk.gz
mmc_boot=if mmc dev ${devnum}; then devtype=mmc; run scan_dev_for_boot_part; fi
mmcboot=mmc dev ${mmcdev}; devnum=${mmcdev}; devtype=mmc; if mmc rescan; then echo SD/MMC found on device ${mmcdev};if run loadima;
mmcdev=0
mmcloados=if test ${boot_fdt} = yes || test ${boot_fdt} = try; then if run loadfdt; then bootz ${loadaddr} - ${fdtaddr}; else if t;
mmcrootfstype=ext4 rootwait
mtdids=nand0=nand.0
mtdparts=mtdparts=nand.0:128k(NAND.SPL),128k(NAND.SPL.backup1),128k(NAND.SPL.backup2),128k(NAND.SPL.backup3),256k(NAND.u-boot-spl-)
name_fit=fitImage
nandargs=setenv bootargs console=${console} ${optargs} root=${nandroot} rootfstype=${nandrootfstype}
nandboot=echo Booting from nand ...; run nandargs; nand read ${fdtaddr} NAND.u-boot-spl-os; nand read ${loadaddr} NAND.kernel; boo}
nandroot=ubi0:rootfs rw ubi.mtd=NAND.file-system,2048
nandrootfstype=ubifs rootwait=1
netargs=setenv bootargs console=${console} ${optargs} root=/dev/nfs nfsroot=${serverip}:${rootpath},${nfsopts} rw ip=dhcp
netboot=echo Booting from network ...; setenv autoload no; dhcp; run netloadimage; run netloadfdt; run netargs; bootz ${loadaddr} }
netloadfdt=tftp ${fdtaddr} ${fdtfile}
netloadimage=tftp ${loadaddr} ${bootfile}
nfsopts=nolock
partitions=uuid_disk=${uuid_gpt_disk};name=bootloader,start=384K,size=1792K,uuid=${uuid_gpt_bootloader};name=rootfs,start=2688K,si}
pxefile_addr_r=0x80100000
ramargs=setenv bootargs console=${console} ${optargs} root=${ramroot} rootfstype=${ramrootfstype}
ramboot=echo Booting from ramdisk ...; run ramargs; bootz ${loadaddr} ${rdaddr} ${fdtaddr}
ramdisk_addr_r=0x88080000
ramroot=/dev/ram0 rw
ramrootfstype=ext2
rdaddr=0x88080000
rootpath=/export/rootfs
run_fit=bootm ${addr_fit}#${fdtfile}${overlaystring}
scan_dev_for_boot=echo Scanning ${devtype} ${devnum}:${distro_bootpart}...; for prefix in ${boot_prefixes}; do run scan_dev_for_ex;
scan_dev_for_boot_part=part list ${devtype} ${devnum} -bootable devplist; env exists devplist || setenv devplist 1; for distro_boot
scan_dev_for_efi=setenv efi_fdtfile ${fdtfile}; if test -z "${fdtfile}" -a -n "${soc}"; then setenv efi_fdtfile ${soc}-${board}${be
scan_dev_for_extlinux=if test -e ${devtype} ${devnum}:${distro_bootpart} ${prefix}${boot_syslinux_conf}; then echo Found ${prefix}i
scan_dev_for_scripts=for script in ${boot_scripts}; do if test -e ${devtype} ${devnum}:${distro_bootpart} ${prefix}${script}; thene
scriptaddr=0x80000000
serial#=BBGW16054424
soc=am33xx
spiargs=setenv bootargs console=${console} ${optargs} root=${spiroot} rootfstype=${spirootfstype}
spiboot=echo Booting from spi ...; run spiargs; sf probe ${spibusno}:0; sf read ${loadaddr} ${spisrcaddr} ${spiimgsize}; bootz ${l}
spibusno=0
spiimgsize=0x362000
spiroot=/dev/mtdblock4 rw
spirootfstype=jffs2
spisrcaddr=0xe0000
static_ip=${ipaddr}:${serverip}:${gatewayip}:${netmask}:${hostname}::off
stderr=serial@0
stdin=serial@0
stdout=serial@0
update_to_fit=setenv loadaddr ${addr_fit}; setenv bootfile ${name_fit}
usb_boot=usb start; if usb dev ${devnum}; then devtype=usb; run scan_dev_for_boot_part; fi
usbnet_devaddr=de:ad:be:ef:00:01
vendor=ti
ver=U-Boot 2021.04 (May 12 2021 - 15:27:22 +0800)

Environment size: 9974/131068 bytes
```

</details>

<details><summary>bdinfo</summary>

```plain
boot_params = 0x80000100
DRAM bank   = 0x00000000
-> start    = 0x80000000
-> size     = 0x20000000
flashstart  = 0x00000000
flashsize   = 0x00000000
flashoffset = 0x00000000
baudrate    = 115200 bps
relocaddr   = 0x9ff6c000
reloc off   = 0x1f76c000
Build       = 32-bit
current eth = ethernet@4a100000
ethaddr     = 88:c2:55:81:a8:58
IP addr     = <NULL>
fdt_blob    = 0x9df38010
new_fdt     = 0x9df38010
fdt_size    = 0x00013ea0
lmb_dump_all:
    memory.cnt             = 0x1
    memory.size            = 0x0
    memory.reg[0x0].base   = 0x80000000
                   .size   = 0x20000000

    reserved.cnt           = 0x1
    reserved.size          = 0x0
    reserved.reg[0x0].base = 0x9df36de8
                     .size = 0x20c9218
arch_number = 0x00000e05
TLB addr    = 0x9fff0000
irq_sp      = 0x9df38000
sp start    = 0x9df37ff0
Early malloc usage: 7d8 / 1000
```

</details>

iminfo

>82000000 is 2080Mi\
>printf "%x\n" $((2080\*1024\*1024))

    ## Checking Image at 82000000 ...
    Unknown image format!

coninfo

    List of available devices:
    serial@0 00000007 IO stdin stdout stderr
    serial   00000003 IO

## A - Set up Ethernet

PC

    su -

<div></div>

    sleep 1; ip link set enp0s31f6 down
    sleep 1; ip addr flush enp0s31f6
    sleep 1; ethtool -s enp0s31f6 mdix on
    sleep 1; ip addr add 192.168.2.2/24 dev enp0s31f6
    sleep 1; ip link set enp0s31f6 up

BBGW USB eth (below L3) - [vars](https://source.denx.de/u-boot/u-boot/-/blob/master/README#L3316)

    usb start

<div></div>

    if test $eth4addr = '00:0e:c6:d3:2d:5f'; then
      # ax88179_eth
      setenv ethprime eth4
      setenv ethact eth4
      setenv ethrotate no
      setenv netretry  no
      echo OK
    else
      echo "FAIL"
    fi
    printenv ethprime ethact ethrotate netretry

BBGW USB eth (L3) - [vars](https://source.denx.de/u-boot/u-boot/-/blob/master/README#L3316)

    setenv serverip  192.168.2.2
    setenv gatewayip 192.168.2.2
    setenv ipaddr    192.168.2.1
    setenv netmask   255.255.255.0
    setenv loadaddr  0x82000000

Ping

    ping ${serverip}
    # Using ax88179_eth device
    # host 192.168.2.2 is alive

Misc

    setenv silent_linux no
    printenv serial#
    ...

## B - TFTP

[Example 1 -- old-style (non-FDT) kernel booting](https://source.denx.de/u-boot/u-boot/-/blob/master/doc/uImage.FIT/howto.txt#L153)

[Example 2 -- new-style (FDT) kernel booting](https://source.denx.de/u-boot/u-boot/-/blob/master/doc/uImage.FIT/howto.txt#L265)

[Booting ARM Linux](https://www.kernel.org/doc/Documentation/arm/Booting)

|File|Address|
|-:|-:|
|zImage|kernel_addr_r|
|initramfs-linux.img|ramdisk_addr_r|
|dtbs/am335x-bonegreen-wireless.dtb|fdt_addr_r|
<!-- ||| -->

Verify

    if test 0 -eq 0 \
      -a ${bootport}        =  "0:2"            \
      -a ${bootfile}        =  "zImage"         \
      -a ${fdtfile}         =  "undefined"      \
      -a ${console}         =  "ttyO0,115200n8" \
      -a ${kernel_addr_r}  -eq 0x82000000       \
      -a ${fdt_addr_r}     -eq 0x88000000       \
      -a ${ramdisk_addr_r} -eq 0x88080000       \
    ; then
      echo OK
    else
      echo ERR
    fi

Set up TFTP client

    if test 0 -eq 0; then
      setenv tftpdstp 69
      # setenv tftpblocksize
      setenv tftptimeout 5000
      setenv tftptimeoutcountmax 0
      # setenv tftpwindowsize
      printenv tftpdstp tftptimeout tftptimeoutcountmax
    fi

Set up TFTP server

    file /home/darren/beaglebone/ArchLinuxARM-am33x-latest/boot
    # sudo busybox udpsvd -Ev -c 1 -u darren:darren -l 820g3 192.168.2.2 69 tftpd -r -u darren /home/darren/beaglebone/ArchLinuxARM-am33x-latest/boot
    sudo busybox udpsvd -Ev -c 1 -l 820g3 192.168.2.2 69 tftpd -r /home/darren/beaglebone/ArchLinuxARM-am33x-latest/boot

[Receive 3 files](https://www.debian.org/releases/stable/armel/ch05s01.en.html) (load ramdisk *last* to get proper [filesize](https://www.denx.de/wiki/DULG/UBootEnvVariables) for bootz)

    tftpboot ${kernel_addr_r}   "zImage"
    tftpboot ${fdt_addr_r}      "dtbs/am335x-bonegreen-wireless.dtb"
    tftpboot ${ramdisk_addr_r}  "initramfs-linux.img"

Naked boot - [boot.txt](https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/boot.txt)

    # WARNING: Your 'console=ttyO0' has been replaced by 'ttyS0'
    # This ensures that you still see kernel messages. Please
    # update your kernel commandline.
    setenv bootargs "console=tty0 console=${console} root=PARTUUID=${uuid} rw rootwait"
    setenv uuid "f8fc2322-bcf0-4540-9c6c-8be8e22d7b95"
    bootz ${kernel_addr_r} ${ramdisk_addr_r}:${filesize} ${fdt_addr_r}

## C - NFS

    # busybox ip link
    1: lo: <LOOPBACK> mtu 65536 qdisc noop qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

[0b95:1790 requires ax88179_178a](https://linux-hardware.org/?id=usb:0b95-1790)

    $ modinfo ax88179_178a | grep -i depends
    depends:        usbnet,mii
    $ modinfo usbnet | grep -i depends
    depends:        mii
    $ $ modinfo mii | grep -i depends
    depends:

<div></div>

    $ modinfo ArchLinuxARM-am33x-latest/usr/lib/modules/5.10.13-1-ARCH/kernel/drivers/net/usb/ax88179_178a.ko.gz | grep -i -e dep -e arm
    depends:
    vermagic:       5.10.13-1-ARCH preempt mod_unload ARMv7 p2v8

https://unix.stackexchange.com/a/486592

Minicom

    cat | base64 -d >/ax88179_178a.ko.gz

<kbd>Ctrl</kbd>+<kbd>A</kbd> then <kbd>Q</kbd>

PC (in another terminal)

    KO="/home/darren/beaglebone/ArchLinuxARM-am33x-latest/usr/lib/modules/5.10.13-1-ARCH/kernel/drivers/net/usb/ax88179_178a.ko.gz"
    sha1sum "$KO"
    base64 >/dev/ttyUSB0 "$KO"
    unset -v KO

Start minicom, then immediately press <kbd>Ctrl</kbd>+<kbd>D</kbd>

    sha1sum /ax88179_178a.ko.gz
    # Make sure checksums match
    insmod /ax88179_178a.ko.gz
    lsmod

Now we have `eth0` in `ip link`

<!-- Fail - Stuck after several characters

Generate self-extracting script for `ax88179_178a.ko.gz`

    truncate -s0 /tmp/minicom.ascii.sh
    printf 'base64 -d >ax88179_178a.ko.gz <<<"' >>/tmp/minicom.ascii.sh
    base64 -w0 /home/darren/beaglebone/ArchLinuxARM-am33x-latest/usr/lib/modules/5.10.13-1-ARCH/kernel/drivers/net/usb/ax88179_178a.ko.gz >>/tmp/minicom.ascii.sh
    echo '"' >>/tmp/minicom.ascii.sh
    echo '---'
    cat /tmp/minicom.ascii.sh
    echo '---'
    sudo ln -sv /tmp/minicom.ascii.sh -t /root/MINICOM_RES/

Send with minicom in <kbd>Ctrl</kbd>+<kbd>A</kbd> - <kbd>S</kbd> - ascii
-->

?

    setenv bootargs root=/dev/nfs rw nfsroot=${serverip}:${rootpath}
    setenv bootargs ${bootargs} ip=${ipaddr}:${serverip}:${gatewayip}:${netmask}:${hostname}:${netdev}:off panic=1
    tftp /path/to/tftp/location/kernel.itb
    iminfo

## &Zcaron; - Misc 2

[firmware-beaglebone](https://archlinuxarm.org/packages/armv7h/firmware-beaglebone) - [Request to upgrade wl18xx firmware](https://github.com/beagleboard/Latest-Images/issues/73)

https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless

    cd ~/beaglebone
    sudo bsdtar -x -p -f ArchLinuxARM-am33x-latest.tar.gz -C /mnt/

community/libguestfs

    gunzip -l ArchLinuxARM-am33x-latest.tar.gz | tail -1 | tr -s ' ' | cut -d' ' -f3 | numfmt --suffix=MiB --to-unit=1Mi
    # 1055MiB
    virt-make-fs -s 1280M -F raw -t ext2 -v ArchLinuxARM-am33x-latest.tar.gz ArchLinuxARM-am33x-latest.ext2.img

archivemount+genimage

    ?

Unprivileged

    cd ~/beaglebone
    mkdir ArchLinuxARM-am33x-latest
    bsdtar -x --no-xattr -f ArchLinuxARM-am33x-latest.tar.gz -C "$_"

Escalate

    su -

Inspect

    cd /home/darren/beaglebone/ArchLinuxARM-am33x-latest
    PACMAN='pacman --sysroot /home/darren/beaglebone/ArchLinuxARM-am33x-latest'
    $PACMAN -Q  | tee | install -vm644 -gdarren -odarren /dev/stdin /home/darren/beaglebone/alarm_pacman_Q
    $PACMAN -Qq | tee | install -vm644 -gdarren -odarren /dev/stdin /home/darren/beaglebone/alarm_pacman_Qq
    $PACMAN -Rsc --color auto $($PACMAN -Qq)

USB to Ethernet

0b95:1790 ASIX Electronics Corp. AX88179 Gigabit Ethernet

[OUI Lookup Tool](https://www.wireshark.org/tools/oui-lookup.html)

    00:0e:c6:d3:2d:5f
    00:0E:C6 Asix Electronics Corp.

[README.usb](https://source.denx.de/u-boot/u-boot/-/raw/master/doc/README.usb)

    # Disconnect
    ping 192.168.2.2 # Dead
    # Connect
    ping 192.168.2.3 # Dead
    ping 192.168.2.2 # Alive

    # Could not flush host TX2 fifo: csr: 2003
    # usb stop
    # Wait for 3 seconds
    # usb start

[Generate MAC addr](https://www.denx.de/wiki/view/DULG/WhereCanIGetAValidMACAddress)

    gcc -Wall -Wextra tools/gen_eth_addr.c -o tools/gen_eth_addr
    $ tools/gen_eth_addr
    ..:..:..:..:..:..
