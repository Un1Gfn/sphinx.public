.. include:: include/substitution.txt

======
Router
======


Contacts
========

| `r/HomeNetworking <https://www.reddit.com/r/HomeNetworking/>`__
| `r/openwrt        <https://www.reddit.com/r/openwrt/>`__

| `t.me/ctcgfw_openwrt_discuss <https://t.me/ctcgfw_openwrt_discuss>`__
| `t.me/pdcn2                  <https://t.me/pdcn2>`__
| `t.me/Nas699                 <https://t.me/Nas699>`__


Misc
====

`Reverse Engineering a VxWorks OS Based Router <https://blog.quarkslab.com/reverse-engineering-a-vxworks-os-based-router.html>`__

| Wi-Fi 4 5 6
| |b| wp\:\ :wp:`Template:802.11_network_standards`
| |b| wp\:\ :wp:`IEEE_802.11`
| |b| `minim <https://www.minim.com/blog/wifi-4-vs-wifi-5-vs-wifi-6>`__
| |b| `rfwireless <https://www.rfwireless-world.com/Terminology/difference-between-wifi-6-and-wifi-5.html>`__

.. table::
   :align: left
   :widths: auto

   =============== ================================= ===========================================================================
    label           standard                          notable features introduced
   =============== ================================= ===========================================================================
         Wi-Fi 4         IEEE 802.11n-2009            :wp:`MIMO`
         Wi-Fi 5    :wp:`IEEE 802.11ac-2013` Wave 1   :wp:`5 GHz <list of WLAN channels#5_GHz_(802.11a/h/j/n/ac/ax)>` band
         Wi-Fi 5    :wp:`IEEE 802.11ac-2013` Wave 2   :wp:`MU-MIMO`
    :wp:`Wi-Fi 6`        IEEE 802.11ax-2021           :wp:`OFDMA`
   =============== ================================= ===========================================================================


Switch
======

.. table::
   :align: left
   :widths: auto

   ============== ========= ======  ======================================
    type           case      port    model                                
   ============== ========= ======  ======================================
    L2 unmanaged   metal     5GbE    TP-LINK TL-SG1005M |:moneybag:|\ 85  
    L2 unmanaged   plastic   5GbE    TP-LINK TL-SG1005D |:moneybag:|\ 100 
    L2 unmanaged   ?         5GbE    H3C S1G |:moneybag:|\ 120            
   ============== ========= ======  ======================================


The Brickable
=============

.. table::
   :align: left
   :widths: auto

   ============================================== ========== ========== ====================================================
    model                                          wi-fi      port       soc/radio                                          
   ============================================== ========== ========== ====================================================
    H3C R280 |:moneybag:|\ 145                     802.11ac   1WAN2LAN   \                                                  
    WNDR3800                                       802.11ac   5BgE       \                                                  
    TP-Link WDR4300                                                      AR9344_/AR9344_\ +AR9580                           
    Netgear WNDR4300 `v1`_                                               AR9344_/AR9344_\ +AR9580                           
    Netgear WNDR4300 `v2`_                                               QCA9563\ [#q63ds]_/QCA9563+AR9580                  
    Netgear R6220_                                                       MT7621ST\ [#mt21]_                                 
    Netgear R6260_                                                       MT7621AT\ [#mt21]_                                 
    Netgear R6400                                                        \                                                  
    Netgear R6850                                                        \                                                  
    Netgear R7450 (AC2600)                                               \                                                  
    Netgear R7800_ (XR500) (Nighthawk X4S AC2600)                        IPQ8065_/\ QCA9984_                                
    DomyWifi DW33D_                                                                                                         
   ============================================== ========== ========== ====================================================

`Padavan <http://en.techinfodepot.shoutwiki.com/wiki/List_of_Padavan_firmware_supported_devices>`__

| TP-LINK TL-WR886N
| |b| 2M+16M
| |b| `<http://en.techinfodepot.shoutwiki.com/wiki/TP-LINK_TL-WR886N_v1.x>`__
| |b| `<https://deviwiki.com/wiki/TP-LINK_TL-WR886N_v1.x>`__
| |b| `<https://thinkrouter.com/router/tp-link/tl-wr886n-v1x/>`__
| |b| `<https://www.router-reset.com/info/TP-LINK/TL-WR886N-v1x>`__

| `debricking <https://openwrt.org/docs/guide-user/troubleshooting/generic.debrick>`__
| |b| |:warning:| fatal hard brick with no software rescue if on-flash u-boot is broken
| |b| |:thinking:| solder an additional SPI flash, which takes precedence over NAND, and flash it with clips
|       |b| https://koolshare.cn/thread-124946-1-1.html
|       |b| https://www.right.com.cn/forum/thread-2606269-1-1.html


The Unbrickable
===============

:pr:`frrouting (we have one router and one switch only)`

| `FOM <https://www.versitron.com/blog/everything-you-need-to-know-about-fiber-optic-modems>`__
  |equiv| :wp:`fiber <fiber-optic communication>` optic :wp:`modem <modem#Optical_modem>`
| :wp:`fiber-optic cable`
| :wp:`optical fiber connector`

.. code:: text

   cable:                   |
   (f)=fiber-optic         -+-
   (e)=ethernet             |
                    +-------+-------+     +--------------+
        +-----+     |      wl0      |     |           p1-+---+-
   -(f)-+-FOM-+-(e)-+-eth0 SBC eth1-+-(e)-+-p0 switch    |
        +-----+     +---------------+     |           p2-+---+-
                                          +--------------+

| SBC
| |b| `NanoPi R2C <https://www.friendlyarm.com/index.php?route=product/product&product_id=285>`__ |:warning:| external USB wifi dongle required
| |b| `NanoPi R2S <https://www.friendlyarm.com/index.php?route=product/product&product_id=282>`__ |:warning:| external USB wifi dongle required
| |b| `NanoPi R4S <https://www.friendlyarm.com/index.php?route=product/product&product_id=284>`__ |:warning:| external USB wifi dongle required
| |b| :pr:`J4125 J6413` |:moneybag:|\ |:moneybag:|\ |:moneybag:|
| |b| `RouterBOARD <https://mikrotik.com/products/group/routerboard>`__
      - `toh <https://openwrt.org/toh/mikrotik/start>`__
      - `common procedures for mikrotik routerboard products <https://openwrt.org/toh/mikrotik/common>`__

| :wp:`nat <network address translation>`
| iptables - :wp:`wikipedia <iptables>` - :aw:`archwiki <iptables>`
| `netfilter <https://netfilter.org/>`__ - :wp:`wikipedia <netfilter>`
| http://linuxwireless.sipsolutions.net/en/developers/Documentation/cfg80211/
| https://alamot.github.io/nl80211/
| https://en.wikipedia.org/wiki/Comparison_of_open-source_wireless_drivers
| https://en.wikipedia.org/wiki/Wireless_network_interface_controller#FullMAC_and_SoftMAC_devices
| https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/uapi/linux/nl80211.h
| https://stackoverflow.com/questions/21456235/how-nl80211-library-cfg80211-work
| https://wireless.wiki.kernel.org/en/developers/documentation/glossary
| https://wireless.wiki.kernel.org/en/developers/documentation/nl80211
| https://wireless.wiki.kernel.org/en/users/documentation
| https://wireless.wiki.kernel.org/en/users/documentation/faq
| https://wireless.wiki.kernel.org/en/users/documentation/iw
| https://wireless.wiki.kernel.org/en/users/documentation/modes
| https://wireless.wiki.kernel.org/en/users/documentation/module-parameters
| https://wireless.wiki.kernel.org/en/users/documentation/rfkill
| https://wireless.wiki.kernel.org/en/users/documentation/wpa_supplicant


| gns3
| :pkg:`AUR/ubridge`

| :aw:`network bridge`
| |b| `redhat <https://developers.redhat.com/blog/2018/10/22/introduction-to-linux-interfaces-for-virtual-networking#>`__
| |b| :wp:`wikipedia <bridging (networking)>`
| |b| :dw:`debianwiki <BridgeNetworkConnections>`
| |b| `<https://geek-university.com/ccna/what-is-a-network-bridge/>`__
| |b| `<https://www.lifewire.com/how-network-bridges-work-816357>`__

Footnotes
=========

.. _AR9344: https://datasheetspdf.com/pdf-file/825113/Atheros/AR9344/1
.. _v1: https://openwrt.org/toh/netgear/wndr4300
.. _v2: https://openwrt.org/toh/netgear/wndr4300_v2
.. _R6220: https://openwrt.org/toh/netgear/r6220
.. _R6260: https://openwrt.org/toh/netgear/r6260
.. _R7800: https://openwrt.org/toh/netgear/r7800
.. _IPQ8065: https://www.qualcomm.com/products/ipq8065
.. _QCA9984: https://www.qualcomm.com/products/qca9984
.. _DW33D: https://openwrt.org/toh/hwdata/domywifi/domywifi_dw33d

.. [#q63ds] | https://forum.openwrt.org/t/qca9563-datasheet/6327
            | https://my-files.su/2mwodv

.. [#mt21] `MT7621 <https://www.mediatek.com/products/homeNetworking/mt7621>`__
           `MT7621ST <https://deviwiki.com/wiki/MediaTek_MT7621#MT7621ST>`__
           `MT7621ST <https://deviwiki.com/wiki/MediaTek_MT7621#MT7621AT>`__
