.. include:: include/substitution.txt

.. highlight:: text

======
CS:APP
======

Misc
====

`Slides <https://www.cs.cmu.edu/~213/schedule.html>`__

`Instructor Site <http://csapp.cs.cmu.edu/3e/instructors.html>`__

| CourseSite
| `CMU CS <https://csd.cmu.edu/cs-and-related-undergraduate-courses>`__
| `15-213/14-513/15-513 Introduction to Computer Systems (ICS) <https://www.cs.cmu.edu/~213/>`__
| `resources <https://www.cs.cmu.edu/~213/resources.html>`__

| prerequisites of 15-213
|  *(clear)*

| 15-213 is prerequisite of [#preqof]_
|    operating systems :emphasis:`- 15-410 Operating System Design and Implementation`
|    networking
|    compilers
|    computer graphics
|    computer architecture :emphasis:`- 18-447 Introduction to Computer Architecture`
|    embedded system design

:kbd:`/home/darren/csapp`

| BookSite
| `Code Examples <http://csapp.cs.cmu.edu/3e/code.html>`__
| `Errata <http://csapp.cs.cmu.edu/3e/errata.html>`__
| `Student Site <http://csapp.cs.cmu.edu/3e/students.html>`__ ... GDB ... x86-64 ISA doc ... Y86-64 tools ... simulator guide ... prof ... memperf ... proxy

| `about <http://csapp.cs.cmu.edu/3e/about.html>`__
| North American edition:
| ISBN-10: 013409266X
| ISBN-13: 978-0134092669

book page offset :kbd:`n(n+35)`


Chapter 0:
==========

`student site <http://csapp.cs.cmu.edu/3e/students.html>`__
|rarr| `labs for self-study students (without solutions) <http://csapp.cs.cmu.edu/3e/labs.html>`__

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ============================
    \                            Data Lab
    \                            Bomb Lab
    \                            Attack Lab
    \                            Buffer Lab
    \                            Architecture Lab
    |:heavy_minus_sign:|         Architecture Lab (Y86)
    \                            Cache Lab
    \                            Performance Lab
    \                            Shell Lab
    \                            Malloc Lab
    \                            Proxy Lab
   ============================ ============================

:raw-html:`</details>`

`web asides <http://csapp.cs.cmu.edu/3e/waside.html>`__

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ============================
    |:hourglass_flowing_sand:|   DATA\:BOOL
    \                            DATA\:TMIN
    \                            DATA\:TNEG
    \                            ASM\:IA32
    \                            ASM\:EASM
    \                            ARCH\:VLOG
    \                            ARCH\:HCL
    \                            OPT\:SIMD
    \                            MEM\:BLOCKING
   ============================ ============================

:raw-html:`</details>`

book

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ============================
    |:heavy_check_mark:|         Front Cover
    |:heavy_check_mark:|         Preface
    |:heavy_check_mark:|         Table of Contents
    \                            Appendix A: Error Handling
   ============================ ============================

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

|:heavy_check_mark:| 100%
:raw-html:`<details close><summary>tracker</summary>`

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


| byte ordering/:wp:`endianness`
| :abbr:`big-endian (store the MSB of a word at the smallest address and the LSB at the largest)`
| :abbr:`little-endian (stores the LSB at the smallest address and the MSB at the largest)`

::

   number 0x37EE93FA
   address of the number is  m

   MSB 0x37
   LSB 0xFA

   BE m+0  m+1  m+2  m+3
      0x37 0xEE 0x93 0xFA

   LE m+0  m+1  m+2  m+3
      0xFA 0x93 0xEE 0x37

| byte ordering/endianness becomes an issue
| 1\. when binary data are communicated over a network between different machines
| 2\. when looking at the byte sequences representing integer data (as a part of an instruction)
| 3\. when programs are written that circumvent the normal type system (C cast/union)

:raw-html:`<details close><summary>printf("%[FieldWidth][.Precision]&lt;d|s&gt;")</summary>`

::

   gcc -x c -std=gnu11 -g -O0 -Wextra -Wall -Winline -Wshadow -fanalyzer -o a.out - <<"EOF"
   #include <stdio.h>
   int main(){
      puts("");
      printf("#%5.3d#\n",1);
      printf("#%5.3d#\n",10);
      printf("#%5.3d#\n",100);
      printf("#%5.3d#\n",1000);
      printf("#%5.3d#\n",10000);
      printf("#%5.3d#\n",100000);
      printf("#%5.3d#\n",1000000);
      puts("");
      printf("#%5.3s#\n","1");
      printf("#%5.3s#\n","10");
      printf("#%5.3s#\n","100");
      printf("#%5.3s#\n","1000");
      printf("#%5.3s#\n","10000");
      printf("#%5.3s#\n","100000");
      printf("#%5.3s#\n","1000000");
      puts("");
      return 0;
   }
   EOF

:raw-html:`</details>`

::

   (BE)
   decimal        3510593   -> 0x00359141 ->   0000000000 1 101011001000101000001
   floating-point 3510593.0 -> 0x4A564504 ->     01001010 0 101011001000101000001 00

.. table::
   :align: left
   :widths: auto

   ========================== ======================= ====================== ===================== ===========================
    \                          NOT                     AND                    OR                    XOR
    boolean operator           :math:`\neg`            :math:`\land \wedge`   :math:`\lor \vee`     :math:`\oplus`
    logical/bitwise operator   :math:`\mathop{\sim}`   :math:`\mathbin{\&}`   :math:`\mathbin{|}`   :math:`\mathbin{^\wedge}`
   ========================== ======================= ====================== ===================== ===========================

:math:`a \mathbin{^\wedge} b = \mathop{\sim} (a\mathbin{\&}b) \mathbin{\&} (a\mathbin{|}b) = (\mathbin{\sim}a\mathbin{|}\mathbin{\sim}b) \mathbin{\&} (a\mathbin{|}b)`
[#latexBitwise]_

| *bit vector*
| strings of zeros and ones of some fixed length :math:`w`
| :math:`[a_{w-1},a_{w-2},\dotsc,a_0]` [#latexDots]_

| boolean algebra :math:`\thicksim` integer arithmetic
| *boolean ring*
| integer value :math:`x` has *additive inverse* :math:`-x` such that :math:`x+-x=0`
| :math:`a \mathbin{^\wedge} a = 0`
| :math:`(a \mathbin{^\wedge} b) \mathbin{^\wedge} a = b`
| encode subsets of a a finite set with bit vectors

.. include:: include/color.txt

.. table::
   :align: left
   :widths: auto

   ============ ============== =============== ============
    RGB          color          ~color          ~RGB       
   ============ ============== =============== ============
    :kbd:`000`   |BK| black      |WH| white     :kbd:`111` 
    :kbd:`001`   |BU| blue       |YE| yellow    :kbd:`110` 
    :kbd:`010`   |GN| green      |MG| magenta   :kbd:`101` 
    :kbd:`011`   |CY| cyan       |RD| red       :kbd:`100` 
    :kbd:`100`   |RD| red        |CY| cyan      :kbd:`011` 
    :kbd:`101`   |MG| magenta    |GN| green     :kbd:`010` 
    :kbd:`110`   |YE| yellow     |BU| blue      :kbd:`001` 
    :kbd:`111`   |WH| white      |BK| black     :kbd:`000` 
   ============ ============== =============== ============



----

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto
   
   ============================ ===============================================================
    |:heavy_check_mark:|         Part I: Program Structure and Execution Preface @ page 29(64)
    |:heavy_check_mark:|         TOC
    |:heavy_check_mark:|         before 2.1
    |:heavy_check_mark:|         2.1   Information Storage
    |:heavy_check_mark:|         |nbsp| - 2.1.1 Hexadecimal Notation
    |:heavy_check_mark:|         |nbsp| - 2.1.2 Data Sizes
    |:heavy_check_mark:|         |nbsp| - 2.1.3 Addressing and Byte Ordering
    |:heavy_check_mark:|         |nbsp| - 2.1.4 Representing Strings
    |:heavy_check_mark:|         |nbsp| - 2.1.5 Representing Code
    |:heavy_check_mark:|         |nbsp| - 2.1.6 Introduction to Boolean Algebra - page 50(85)
    |:hourglass_flowing_sand:|   |nbsp| - 2.1.7 Bit-Level Operations in C
    \                            |nbsp| - 2.1.8 Logical Operations in C
    \                            |nbsp| - 2.1.9 Shift Operations in C
    \                            2.2 Integer Representations
    \                            2.3 Integer Arithmetic
    \                            2.4 Floating Point
    \                            2.5 Summary
   ============================ ===============================================================

:raw-html:`</details>`


Chapter 3: Machine-Level Representation of Programs
===================================================


Footnotes
=========

.. [#preqof] `key points <http://csapp.cs.cmu.edu/3e/perspective.html#:~:text=At%20Carnegie%20Mellon%2C%20our%20Introduction%20to%20Computer%20Systems%20course%20has%20become%20a%20prequisite%20for%20courses%20in%20both%20CS%20and%20ECE%20covering%3A%20operating%20systems%2C%20networking%2C%20compilers%2C%20computer%20graphics%2C%20computer%20architecture%2C%20and%20embedded%20system%20design>`__

.. [#latexBitwise]
   | se/tex/
         `14227 <https://tex.stackexchange.com/questions/14227>`__
         `77646 <https://tex.stackexchange.com/questions/77646>`__
        `361862 <https://tex.stackexchange.com/questions/361862>`__
   | wikibooks/latex/`mathematics <https://en.wikibooks.org/wiki/LaTeX/Mathematics>`__
   | wikipedia/:wp:`list of logic symbols`
   | `oeis <https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols>`__

.. [#latexDots] se/tex/`1176 <https://tex.stackexchange.com/questions/1176>`__
