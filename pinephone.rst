.. include:: include/substitution.txt
.. highlight:: text

=========
pinephone
=========

#misc#
======

| allwinner/`A64-H <https://www.allwinnertech.com/index.php?c=product&a=index&id=9>`__
| pdf.\ `usermanual <https://linux-sunxi.org/images/b/b4/Allwinner_A64_User_Manual_V1.1.pdf>`__
| pdf.\ `datasheet <https://dl.linux-sunxi.org/A64/A64_Datasheet_V1.1.pdf>`__

| osdev/:osdev:`PinePhone`

| github/`linux-sunxi <https://github.com/linux-sunxi>`__
| sunxi/:sunxi:`PinePhone`
| sunxi/:sunxi:`BROM`
| sunxi/:sunxi:`Cedrus`

| pine64/`pinephone <https://www.pine64.org/pinephone/>`__
| pine64/:pine64:`jumpdrive <PinePhone Installation Instructions#Using_JumpDrive>`
| `jumpdrive <https://github.com/dreemurrs-embedded/Jumpdrive/>`__

| pmos/v22.06/`device-pine64-pinephone          <https://pkgs.postmarketos.org/package/v22.06/postmarketos/aarch64/device-pine64-pinephone>`__
| pmos/v22.06/`linux-postmarketos-allwinner     <https://pkgs.postmarketos.org/package/v22.06/postmarketos/aarch64/linux-postmarketos-allwinner>`__
| pmos/v22.06/`linux-postmarketos-allwinner-dev <https://pkgs.postmarketos.org/package/v22.06/postmarketos/aarch64/linux-postmarketos-allwinner-dev>`__
| megous/`linux <https://github.com/megous/linux>`__

| AUR/`*sunxi* <https://aur.archlinux.org/packages?K=sunxi>`__

`the pinephone pro is here (and it runs mobian!) <https://blog.mobian-project.org/posts/2021/12/28/pinephone-pro/>`__


battery
=======

| :sunxi:`AXP209`
| /sys/class/power_supply/axp20x-battery/voltage_{max,min}_design
| /sys/class/power_supply/axp20x-battery/voltage_{now,ocv}


CPU
===

| sunxi/:sunxi:`sun50iw1=A64 <A64>`
| :pine64:`overclocking`
| `danct12 <https://danct12.github.io/PinePhone-CPU-overclocking/>`__

| :sunxi:`optimizing system performance`
| :sunxi:`cpufreq`
| cpupower :aw:`governors <CPU frequency scaling#Scaling_governors>`
| install cpupower{,-openrc} and modify /etc/conf.d/cpupower

eMMC
====

| noatime
| alpine/main/openrc/`remount-root.patch <https://git.alpinelinux.org/aports/tree/main/openrc/remount-root.patch>`__
| openrc/init.d/`root.in <https://github.com/OpenRC/openrc/blob/master/init.d/root.in>`__ |rarr| root


(A)GNSS/(A)GPS
===============

disable in /etc/eg25-manager/pine64,pinephone-1.2.toml


initcpio/mkinitfs
=================

?


modem
=====

misc.desktop action ``[[modemreboot]]`` ::

   # text='reboot'
   M="$(mmcli -m any --messaging-create-sms="text='name',number='+223344556677'" | grep -Eo '/org/freedesktop/ModemManager1/SMS/[0-9]*')"
   mmcli -s "$M" --send -v

| (hover for definition in url)
| \
  . :wp:`IMS <IP Multimedia Subsystem>`
  . :wp:`SIP <Session Initiation Protocol>`
  . :wp:`UE <user equipment>`
  . :wp:`USSD code <Unstructured Supplementary Service Data>`
  . :wp:`MCC <mobile country code>` MNC

| (nearly) free custom firmware |rarr| `binary <https://github.com/the-modem-distro/pinephone_modem_sdk/releases>`__
| CU-VoLTE `included <https://github.com/the-modem-distro/pinephone_modem_sdk/issues/159#issuecomment-1295727305>`__

AT+QPRTPARA `factory reset <https://github.com/Biktorgj/quectel_eg25_recovery/issues/15#issuecomment-1133765547>`__  NVM

| `qadbkey-unlock <https://xnux.eu/devices/feature/modem-pp.html#toc-unlock-adb-access>`__
| ``~/pmos.pinephone/qadbkey-unlock.py <key>``
| disable ADB access to enable S3 sleep/suspend
|    ``AT+QCFG="usbcfg",0x2C7C,0x125,1,1,1,1,1,0,0``

`fcc unlock <https://modemmanager.org/docs/modemmanager/fcc-unlock/>`__

| `teit AT commands reference <https://www.sparkfun.com/datasheets/Cellular%20Modules/AT_Commands_Reference_Guide_r0.pdf>`__
| quectel `LTE EG25-G <https://www.quectel.com/product/lte-eg25-g>`__
|    Quectel ... AT Commands_Manual V2.0
|    `Quectel ... IMS Application Note V1.0 <https://www.quectel.com/wp-content/uploads/2021/09/Quectel_EC2xEG9xEG2x-GEM05_Series_IMS_Application_Note_V1.0.pdf>`__
| `xnux <https://xnux.eu/devices/feature/modem-pp.html>`__

| `AT command make LTE data call <https://m2msupport.net/m2msupport/data-call-at-commands-to-set-up-gprsedgeumtslte-data-call/>`__
| csdn/`10086 drop to 2G <https://blog.csdn.net/shij19/article/details/52946463>`__

| :pine64:`PinePhone#Firmware_update`
|    quectel_eg25_recovery/`branches/all <https://github.com/Biktorgj/quectel_eg25_recovery/branches/all>`__
|    `ADSP-CARRIERS <https://github.com/the-modem-distro/pinephone_modem_sdk/blob/kirkstone/docs/ADSP-CARRIERS.md#will-x-firmware-version-work-with-y-provider>`__
     - :el:`File Systems#UBI`
     - :el:`UBIFS`
     - `ubidump <https://github.com/nlitsme/ubidump>`__
     - `goflexhome <https://goflexhome.blogspot.com/2019/02/inspect-or-change-rootfs-ubi-image-file.html>`__
     - `infradead <http://www.linux-mtd.infradead.org/doc/general.html>`__
| :pine64:`PineModems`
| :pmos:`PINE64 PinePhone (pine64-pinephone)#VoLTE`
| megous/`modem.txt <https://megous.com/dl/tmp/modem.txt>`__



`eg25-manager <https://gitlab.com/mobian1/eg25-manager>`__ ::

   curl -s https://gitlab.com/mobian1/eg25-manager/-/raw/master/doc/eg25-manager.5.scd | scdoc | man -l -
   curl -s https://gitlab.com/mobian1/eg25-manager/-/raw/master/doc/eg25-manager.8.scd | scdoc | man -l -
   meld <(/bin/ssh user@pinephoneusb 'cat /usr/share/eg25-manager/pine64,pinephone-1.2.toml.pacnew') <(/bin/ssh user@pinephoneusb 'cat /usr/share/eg25-manager/pine64,pinephone-1.2.toml.pacsave') &
   rc-service eg25-manager stop; rm -fv /var/log/eg25-manager.err

AT ::

   # volte.query
   echo 'AT+QMBNCFG="autosel"' | atinout - /dev/EG25.AT -
   echo 'AT+QMBNCFG="list"'    | atinout - /dev/EG25.AT -
   echo 'AT+QMBNCFG="select"'  | atinout - /dev/EG25.AT -
   echo 'AT+QCFG="ims"'        | atinout - /dev/EG25.AT -
   echo 'AT+CLCC'              | atinout - /dev/EG25.AT -
   # volte.query
   echo 'AT+QMBNCFG="autosel",0'                 | atinout - /dev/EG25.AT -
   echo 'AT+QMBNCFG="select","ROW_Generic_3GPP"' | atinout - /dev/EG25.AT -
   echo 'AT+QCFG="ims",1'                        | atinout - /dev/EG25.AT -
   echo 'AT+CLCC'                                | atinout - /dev/EG25.AT -
   echo 'AT+CFUN=1,1'                            | atinout - /dev/EG25.AT -
   # wait for reboot /dev/ttyUSB2
   echo AT+CLCC'                                 | atinout - /dev/EG25.AT -

mmcli
`MMModemMode <https://www.freedesktop.org/software/ModemManager/api/latest/ModemManager-Flags-and-Enumerations.html#MMModemMode>`__
[#46004]_
::

   # list modem
   mmcli -L
   # internal bearer
   mmcli -m _ | grep bearer
   # manual bearer
   mmcli -m _ --create-bearer='apn=3gnet,user=blank,password=blank,allowed-auth=chap,allow-roaming=no'
   # network mode
   mmcli -m _ --set-allowed-modes=4G
   mmcli -m 0 --3gpp-scan
   #
   # 46000 GSM      CMCC 
   # 46001 GSM      UNICOM
   # 46002 TD-SCDMA CMCC
   # 46003 CDMA     CT
   # 46004 (CNSA)   CMCC
   # 46005 CDMA     CT
   # 46006 WCDMA    UNICOM
   # 46007 TD-SCDMA CMCC
   # 46008 ?        CMCC
   # 46009 ?        UNICOM
   # .     .        .
   # 46011 FDD-LTE   CT
   # .     .        .
   # 46020 ?        CMTIETONG

nmcli ::

   nmcli c add type gsm ifname cdc-wdm0 con-name UNICOM apn 3gnet user blank password blank
   nmcli c up UNICOM
   nmcli c down UNICOM

test ::

   busybox wget https://www.baidu.com/ -O-


TF/microSD
==========

| usbdev.ru/`urwtest <https://www.usbdev.ru/files/urwtest/>`__
| `f3 <https://github.com/AltraMayor/f3>`__

thermal
=======

:sunxi:`Thermal Sensor`

/sys/class/thermal
. `txt <https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-thermal>`__
. `html <https://docs.kernel.org/admin-guide/abi-testing.html#abi-file-testing-sysfs-class-thermal>`__


#footnotes#
===========

.. [#46004] 高德地圖 `中國航天 <https://mogua.co/view_file/?file=com/alipay/mobile/aompdevice/telephonyinfo/h5plugin/H5TelephonyInfoPlugin.java&md5=f01a631cc66654df04a2cd3f6c704327&type=apk&appname=%E9%AB%98%E5%BE%B7%E5%9C%B0%E5%9B%BE&lines=38>`__
