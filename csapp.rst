.. include:: include/substitution.txt

======
CS:APP
======

`CMU CS <https://csd.cmu.edu/cs-and-related-undergraduate-courses>`__ - 15-213/14-513/15-513 Introduction to Computer Systems (ICS)

textbook libgen.rs thepiratebay.org librarypirate

| `about <http://csapp.cs.cmu.edu/3e/about.html>`__
| North American edition:
| ISBN-10: 013409266X
| ISBN-13: 978-0134092669


Chapter 0:
==========

:raw-html:`<details><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ====================== ===================
    |:heavy_check_mark:|   Front Cover
    |:heavy_check_mark:|   Preface
    |:heavy_check_mark:|   Table of Contents
   ====================== ===================

:raw-html:`</details>`


Chapter 1: A Tour of Computer Systems
======================================

| *Bus interface* is a part of CPU.
| *System bus* connects *bus interface* to *I/O bridge*.
| *Memory bus* connects *I/O bridge* to RAM.

:abbr:`concurrency (The instructions of one process are interleaved with the instructions of another process.)`

:wp:`Amdahl's law`

.. math::

   \begin{eqnarray}
           T_{new} &=& (1-\alpha) T_{old} + \alpha \frac{T_{old}}{k} \\
                   &=& T_{old}[(1-\alpha)+\alpha/k]                  \\
      speed\ up\ S &=& \frac{1}{(1-q)+\frac{\alpha}{k}}
   \end{eqnarray}

| :wp:`SMT <simultaneous multithreading>`
| |b| multiple copies of some of the CPU hardware (ProgramCounter/RegisterFile/...) in one CPU
| |b| only single copies of other parts of the hardware (FPU/...) in one CPU

----

:raw-html:`<details><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ====================== ======
    |:heavy_check_mark:|   TOC
    |:heavy_check_mark:|   1.1
    |:heavy_check_mark:|   1.2
    |:heavy_check_mark:|   1.3
    |:heavy_check_mark:|   1.4
    |:heavy_check_mark:|   1.5
    |:heavy_check_mark:|   1.6
    |:heavy_check_mark:|   1.7
    |:heavy_check_mark:|   1.8
    |:heavy_check_mark:|   1.9
    |:heavy_check_mark:|   1.9.1
    |:heavy_check_mark:|   1.9.2
    |:heavy_check_mark:|   1.9.3
    |:heavy_check_mark:|   1.10
   ====================== ======

:raw-html:`</details>`


Chapter 2: Representing and Manipulating Information
====================================================

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto
   
   ====================== ===============================================================
    |:heavy_check_mark:|   Part I: Program Structure and Execution Preface @ page 29(64)
    |:heavy_check_mark:|   TOC
    |:hourglass:|          before 2.1
    \                      2.1
    \                      2.2
    \                      2.3
    \                      2.4
   ====================== ===============================================================

:raw-html:`</details>`


Chapter 3: Machine-Level Representation of Programs
===================================================
