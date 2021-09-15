.. include:: include/substitution.txt

========
GPU_hang
========

Readings
========

`The kernel’s command-line parameters`__

| linuxreviews
| |b| `Intel_graphics#Troubleshooting`__
|     ``ahci.mobile_lpm_policy=1``
|     ``i915.enable_dc=0``
|     ``intel_idle.max_cstate=1``
| |b| `Linux Kernel 5.5 Will Not Fix The Frequent Intel GPU Hangs In Recent Kernels`__\
      [*]_
|     ``i915.enable_dc=0``
|     ``intel_idle.max_cstate=1``

.. __: https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html
.. __: https://linuxreviews.org/Intel_graphics#Troubleshooting
.. __: https://linuxreviews.org/Linux_Kernel_5.5_Will_Not_Fix_The_Frequent_Intel_GPU_Hangs_In_Recent_Kernels

Issue Tracker
=============

`How to file i915 bugs <https://gitlab.freedesktop.org/drm/intel/-/wikis/How-to-file-i915-bugs>`__

| search ``85dffffb``
| |b| `priority   <https://gitlab.freedesktop.org/drm/intel/-/issues?scope=all&search=85dffffb&sort=priority&state=all>`__
| |b| `popularity <https://gitlab.freedesktop.org/drm/intel/-/issues?scope=all&search=85dffffb&sort=popularity&state=all>`__

| search ``gpu hang``
| |b| `priority   <https://gitlab.freedesktop.org/drm/intel/-/issues?scope=all&search=gpu+hang&sort=priority&state=all>`__
| |b| `popularity <https://gitlab.freedesktop.org/drm/intel/-/issues?scope=all&search=gpu+hang&sort=popularity&state=all>`__

| e.g.
| |b| `#548  <https://gitlab.freedesktop.org/drm/intel/-/issues/548>`__
| |b| `#673  <https://gitlab.freedesktop.org/drm/intel/-/issues/673>`__
| |b| `#1003 <https://gitlab.freedesktop.org/drm/intel/-/issues/1003>`__

My case
=======

| GPU hang ``ecode 9:1:85dffffb`` chromium
| |b| Intel HD 520 (i5-6200U) (`HP EliteBook 820 G3`__)
| |b| (Arch) Linux 5.13.7
| |b| xorg-server 1.20.13
| |b| xf86-video-intel is NOT installed
| |b| `picom`__ 8.2
| |b| chromium 92.0.4515.131-1

.. __: https://support.hp.com/us-en/document/c04913012
.. __: https://github.com/yshui/picom

.. code:: text

   Aug 05 00:03:34 820g3 kernel: i915 0000:00:02.0: [drm] Resetting rcs0 for preemption time out
   Aug 05 00:03:34 820g3 kernel: i915 0000:00:02.0: [drm] chromium[116021] context reset due to GPU hang
   Aug 05 00:03:34 820g3 kernel: i915 0000:00:02.0: [drm] GPU HANG: ecode 9:1:85dffffb, in chromium [116021]

Other kernel versions

.. :heavy_check_mark:
.. table::
   :align: left
   :widths: auto

   ============= =====================================
    5.13.7        |:x:| GPU hangs several times a day
    5.10.? LTS    |:x:| GPU hangs several times a day
    5.4.132 LTS   |:green_circle:| never
   ============= =====================================

Hunt That Bug!
==============

.. warning::

   | Hunt the bug in previous versions of ``linux``\ :superscript:`core`
   | ``linux-lts``\ :superscript:`core` and
     ``linux-lts``\ |lowast|\ :superscript:`AUR` make no sense.

| First of all, always use ``5.4.x lts`` for production.
| If it breaks, get an `even older lts`__.
| |b| ``4.19.x``
| |b| ``4.14.x``

.. __: https://www.kernel.org/

| Download older versions of linux\ :superscript:`core` from :aw:`Arch Linux Archive` instead.
| versions of linux\ :superscript:`core` PKGBUILDs on `GitHub`__
| |b| Is the bug introduced after ``5.10.1`` or before ``5.9.14``?

.. __: https://github.com/archlinux/svntogit-packages/commits/packages/linux?after=65021922842cea417aad89ed4f094b5c8cbd9b5a+90&branch=packages%2Flinux&path%5B%5D=trunk

It there any program which tortures the GPU & reproduces the bug instantly,
thus we don't have to play 3D game or abuse browser and wait till it hangs?
(chromium WebGL stress test?)

Footnotes
=========

.. [*] Warning: the author may be a racist.


Journalctl
==========

.. code:: shell-session

   $ sudo env SYSTEMD_COLORS=1 journalctl --no-pager -S '2021-04-20 22:09:50' -U '2021-04-20 22:12:07'
   -- Journal begins at Wed 2020-09-30 23:45:24 WITA, ends at Mon 2021-06-14 18:11:14 WITA. --
   Apr 20 22:11:17 820g3 kernel: i915 0000:00:02.0: [drm] Resetting rcs0 for preemption time out
   Apr 20 22:11:17 820g3 kernel: i915 0000:00:02.0: [drm] Renderer[84279] context reset due to GPU hang
   Apr 20 22:11:17 820g3 kernel: i915 0000:00:02.0: [drm] GPU HANG: ecode 9:1:85df9fff, in Renderer [84279]
   Apr 20 22:11:17 820g3 kernel: GPU hangs can indicate a bug anywhere in the entire gfx stack, including userspace.
   Apr 20 22:11:17 820g3 kernel: Please file a _new_ bug report at https://gitlab.freedesktop.org/drm/intel/issues/new.
   Apr 20 22:11:17 820g3 kernel: Please see https://gitlab.freedesktop.org/drm/intel/-/wikis/How-to-file-i915-bugs for details.
   Apr 20 22:11:17 820g3 kernel: drm/i915 developers can then reassign to the right component if it's not a kernel issue.
   Apr 20 22:11:17 820g3 kernel: The GPU crash dump is required to analyze GPU hangs, so please always attach it.
   Apr 20 22:11:17 820g3 kernel: GPU crash dump saved to /sys/class/drm/card0/error

.. code:: shell-session

   $ sudo env SYSTEMD_COLORS=1 journalctl --no-pager -S '2021-06-14 17:03:35' -U '2021-06-14 17:04:49' | grep -i audit -v
   -- Journal begins at Wed 2020-09-30 23:45:24 WITA, ends at Mon 2021-06-14 18:14:36 WITA. --
   Jun 14 17:03:35 820g3 kernel: Asynchronous wait on fence 0000:00:02.0:picom[4515]:36f6a timed out (hint:intel_atomic_commit_ready [i915])
   Jun 14 17:03:36 820g3 kernel: i915 0000:00:02.0: [drm] Resetting rcs0 for preemption time out
   Jun 14 17:03:36 820g3 kernel: i915 0000:00:02.0: [drm] MTGS[4653] context reset due to GPU hang
   Jun 14 17:03:36 820g3 kernel: i915 0000:00:02.0: [drm] GPU HANG: ecode 9:1:859ffffb, in MTGS [4653]
   Jun 14 17:04:18 820g3 kernel: i915 0000:00:02.0: [drm] Resetting rcs0 for preemption time out
   Jun 14 17:04:18 820g3 kernel: i915 0000:00:02.0: [drm] PCSX2:gdrv0[4658] context reset due to GPU hang
   Jun 14 17:04:19 820g3 kernel: i915 0000:00:02.0: [drm] GPU HANG: ecode 9:1:85dfffff, in PCSX2:gdrv0 [4658]
   Jun 14 17:04:46 820g3 kernel: Asynchronous wait on fence 0000:00:02.0:picom[4515]:3771a timed out (hint:intel_atomic_commit_ready [i915])
   Jun 14 17:04:48 820g3 kernel: i915 0000:00:02.0: [drm] Resetting rcs0 for preemption time out
   Jun 14 17:04:48 820g3 kernel: i915 0000:00:02.0: [drm] PCSX2:gdrv0[4658] context reset due to GPU hang
   Jun 14 17:04:48 820g3 kernel: i915 0000:00:02.0: [drm] GPU HANG: ecode 9:1:85dfbfff, in PCSX2:gdrv0 [4658]
   Jun 14 17:04:48 820g3 systemd[1]: Created slice system-systemd\x2dcoredump.slice.
   Jun 14 17:04:48 820g3 systemd[1]: Started Process Core Dump (PID 4692/UID 0).
   Jun 14 17:04:48 820g3 systemd-coredump[4693]: Resource limits disable core dumping for process 4556 (PCSX2).
   Jun 14 17:04:48 820g3 systemd-coredump[4693]: [🡕] Process 4556 (PCSX2) of user 1000 dumped core.
   Jun 14 17:04:48 820g3 systemd[1]: systemd-coredump@0-4692-0.service: Deactivated successfully.

.. code:: shell-session
   
   $ sudo env SYSTEMD_COLORS=1 journalctl --no-pager -S '2021-06-14 17:03:35' -U '2021-06-14 17:04:49' | grep -i audit
   Jun 14 17:04:48 820g3 audit[4556]: ANOM_ABEND auid=1000 uid=1000 gid=1000 ses=1 pid=4556 comm="PCSX2:gdrv0" exe="/usr/bin/PCSX2" sig=6 res=1
   Jun 14 17:04:48 820g3 kernel: audit: type=1701 audit(1623661488.019:140): auid=1000 uid=1000 gid=1000 ses=1 pid=4556 comm="PCSX2:gdrv0" exe="/usr/bin/PCSX2" sig=6 res=1
   Jun 14 17:04:48 820g3 audit: BPF prog-id=34 op=LOAD
   Jun 14 17:04:48 820g3 audit: BPF prog-id=35 op=LOAD
   Jun 14 17:04:48 820g3 audit: BPF prog-id=36 op=LOAD
   Jun 14 17:04:48 820g3 kernel: audit: type=1334 audit(1623661488.089:141): prog-id=34 op=LOAD
   Jun 14 17:04:48 820g3 kernel: audit: type=1334 audit(1623661488.089:142): prog-id=35 op=LOAD
   Jun 14 17:04:48 820g3 kernel: audit: type=1334 audit(1623661488.089:143): prog-id=36 op=LOAD
   Jun 14 17:04:48 820g3 audit[1]: SERVICE_START pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=systemd-coredump@0-4692-0 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
   Jun 14 17:04:48 820g3 kernel: audit: type=1130 audit(1623661488.093:144): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=systemd-coredump@0-4692-0 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
   Jun 14 17:04:48 820g3 kernel: audit: type=1131 audit(1623661488.139:145): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=systemd-coredump@0-4692-0 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
   Jun 14 17:04:48 820g3 audit[1]: SERVICE_STOP pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=systemd-coredump@0-4692-0 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
   Jun 14 17:04:48 820g3 audit: BPF prog-id=36 op=UNLOAD
   Jun 14 17:04:48 820g3 audit: BPF prog-id=35 op=UNLOAD
   Jun 14 17:04:48 820g3 audit: BPF prog-id=34 op=UNLOAD
   Jun 14 17:04:48 820g3 kernel: audit: type=1334 audit(1623661488.236:146): prog-id=36 op=UNLOAD
   Jun 14 17:04:48 820g3 kernel: audit: type=1334 audit(1623661488.236:147): prog-id=35 op=UNLOAD
   Jun 14 17:04:48 820g3 kernel: audit: type=1334 audit(1623661488.236:148): prog-id=34 op=UNLOAD
