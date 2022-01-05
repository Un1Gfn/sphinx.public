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

decimal to hexadecimal

.. math::

   \begin{eqnarray}
      D_{10} \div 16 &=& q_1 \cdots r_1 \\
      q_1    \div 16 &=& q_2 \cdots r_2 \\
      q_2    \div 16 &=& q_3 \cdots r_3 \\
      q_3    \div 16 &=& q_4 \cdots r_4 \\
      q_4    \div 16 &=& 0   \cdots r_5 \\
      D_{10}         &=& \overline{r_5r_4r_3r_2r_1}_{16}
   \end{eqnarray}

----

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto
   
   ====================== ===============================================================
    |:heavy_check_mark:|   Part I: Program Structure and Execution Preface @ page 29(64)
    |:heavy_check_mark:|   TOC
    |:heavy_check_mark:|   before 2.1
    |:heavy_check_mark:|   2.1
    |:heavy_check_mark:|   2.1.1
    |:heavy_check_mark:|   2.1.2
    |:hourglass:|          2.1.3 Addressing and Byte Ordering
    \                      2.1.4
    \                      2.1.5
    \                      2.1.6
    \                      2.1.7
    \                      2.1.8
    \                      2.1.9
    \                      2.2
    \                      2.3
    \                      2.4
   ====================== ===============================================================

:raw-html:`</details>`


Chapter 3: Machine-Level Representation of Programs
===================================================
