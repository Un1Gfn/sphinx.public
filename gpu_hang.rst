.. include:: include/substitution.txt

========
GPU_hang
========

::

   modinfo -p ahci
   modinfo -p i915
   modinfo -p intel_idle

`The kernel’s command-line parameters <https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html>`__

| linuxreviews
| |b| `Intel_graphics#Troubleshooting`__
|     ``ahci.mobile_lpm_policy=1``
|     ``i915.enable_dc=0``
|     ``intel_idle.max_cstate=1``
| |b| `Linux Kernel 5.5 Will Not Fix The Frequent Intel GPU Hangs In Recent Kernels`__
|     ``i915.enable_dc=0``
|     ``intel_idle.max_cstate=1``

.. __: https://linuxreviews.org/Intel_graphics#Troubleshooting
.. __: https://linuxreviews.org/Linux_Kernel_5.5_Will_Not_Fix_The_Frequent_Intel_GPU_Hangs_In_Recent_Kernels
