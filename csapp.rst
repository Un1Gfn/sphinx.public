.. include:: include/substitution.txt

.. highlight:: text

======
CS:APP
======

Misc
====

.. note::

   |:pencil:| squeeze :kbd:`/home/darren/csapp` !

| list of CMU CS `courses <https://csd.cmu.edu/cs-and-related-undergraduate-courses>`__
|    `15-213/14-513/15-513 Introduction to Computer Systems (ICS) <https://www.cs.cmu.edu/~213/>`__
|       `resources <https://www.cs.cmu.edu/~213/resources.html>`__
|       `slides <https://www.cs.cmu.edu/~213/schedule.html>`__

| prerequisites of 15-213
|  *(clear)*

| 15-213 is prerequisite of [#preqof]_
|    compilers
|    computer architecture :emphasis:`- 18-447 Introduction to Computer Architecture`
|    computer graphics
|    embedded system design
|    networking
|    operating systems :emphasis:`- 15-410 Operating System Design and Implementation`

| BookSite
|    `Instructor Site <http://csapp.cs.cmu.edu/3e/instructors.html>`__
|    `Code Examples <http://csapp.cs.cmu.edu/3e/code.html>`__
|    `Errata <http://csapp.cs.cmu.edu/3e/errata.html>`__
|    `Student Site <http://csapp.cs.cmu.edu/3e/students.html>`__ ... GDB ... x86-64 ISA doc ... Y86-64 tools ... simulator guide ... prof ... memperf ... proxy
|       Online GDB Materials - Quick Guide to GDB
|       Chapter 4: Processor Architecture - Y86-64 tools and documentation - Source distribution - hcl2v
|       `Implicit Variables <https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html#Implicit-Variables>`__
|       `Implicit Rules <https://www.gnu.org/software/make/manual/html_node/Catalogue-of-Rules.html#Catalogue-of-Rules>`__
|    `about <http://csapp.cs.cmu.edu/3e/about.html>`__
|       North American edition:
|       ISBN-10: 013409266X
|       ISBN-13: 978-0134092669
|       libgen.rs md5 ``33DC73067D7512A7D970CEC5FE8870DB``

book page offset :kbd:`n(n+35)`

`Shared Libraries: Understanding Dynamic Loading <https://amir.rachum.com/blog/2016/09/17/shared-libraries/>`__

::

   sh -c 'exec busybox pmap $$'\
   ldd $(which pmap) - `libprocps.so.8 => /usr/lib/libprocps.so.8 (0x00007fabcfe99000)`\
   /usr/include/proc/


Chapter 0:
==========

notes
-----

| addative /**a**·duh·tiv/
| commutative /kuh·**myoo**·tuh·tuhv/
| multiplicative /muhl·tuh·**pli**·kuh·tuhv/
| addition /uh·**di**·shn/

| the set of :wp:`integers <integer>` form an integer :wp:`ring <ring (mathematics)#Illustration>`
  :math:`\langle Z,+,\times,-,0,1 \rangle`
| :math:`+,\times` are :wp:`associative <associative property>` and :wp:`commutative <commutative property>`
| :math:`\times` is :wp:`distributive <distributive property>` over :math:`+`
| :math:`0` is the additive :wp:`identity element` (:wp:`additive identity`)
| :math:`1` is the multiplicative :wp:`identity element`
| integer value :math:`x` has :wp:`additive inverse` :math:`-x` such that :math:`x+-x=0`

| xor /**sor**/

| boolean *algebra* denoted :math:`\langle \{0,1\}, \mathbin{|}, \mathbin{\&}, \mathop{^\sim}, 0, 1 \rangle`
  :sub:`not to be confused with boolean ring`
| :math:`a \mathbin{^\wedge} a = 0`
| :math:`(a \mathbin{^\wedge} b) \mathbin{^\wedge} a = b`
| :math:`a \mathbin{\&} (b \mathbin{|}  c) = (a \mathbin{\&} b) \mathbin{|}  (a \mathbin{\&} c)` |nbsp|\ |nbsp|
     :math:`\mathbin{\&}` is :wp:`distributive <distributive property>` over :math:`\mathbin{|}`
| properties unique to *rings* without *boolean algebra* counterpart
|   additive inverse:|nbsp| :math:`a+-a=0`
| properties unique to *boolean algebra* without *ring* counterpart
|   \
    :math:`\mathbin{\&}` and :math:`\mathbin{|}` mutually distributive
    ( :math:`\mathbin{|}` is :wp:`distributive <distributive property>` over :math:`\mathbin{\&}` as well )
|      :math:`a \mathbin{|}  (b \mathbin{\&} c) = (a \mathbin{|}  b) \mathbin{\&} (a \mathbin{|}  c)`
|   complement
|      :math:`a \mathbin{|}  \mathop{^\sim}a = 1`
|      :math:`a \mathbin{\&} \mathop{^\sim}a = 0`
|   :wp:`idempotent <idempotent relation>` /ai·duhm·**pow**·tnt/
|      :math:`a \mathbin{\&} a = a`
|      :math:`a \mathbin{|}  a = a`
|   absorbtion
|      :math:`a \mathbin{\&} (a \mathbin{|}  b) = a`
|      :math:`a \mathbin{|}  (a \mathbin{\&} b) = a`
|   De Morgan's laws
|      :math:`\mathop{^\sim} (a \mathbin{\&} b) = \mathop{^\sim} a \mathbin{|}  \mathop{^\sim} b`
|      :math:`\mathop{^\sim} (a \mathbin{|}  b) = \mathop{^\sim} a \mathbin{\&} \mathop{^\sim} b`

| boolean /**boo**·lee·uhn/
| modular /**maa**·juh·lr/
| modulo /**maa**·duh·low/

| boolean *ring* denoted :math:`\langle \{0,1\}, \mathbin{^\wedge}, \mathbin{\&}, I, 0, 1 \rangle`
  :sub:`not to be confused with boolean algebra`
|    where :math:`I` is the identity operation :math:`I(a)=a`
| equivalent to a modular arithmetic ring with modulo :math:`n=2`
| additive inverse:|nbsp| :math:`a \mathop{^\wedge} I(a) = a \mathop{^\wedge} a = 0`
| mathematical basis of :wp:`ECC <error correction code>` is a linear algebra based on *boolean rings*

|:dart:|

| general :wp:`modular arithmetic` ring for modulus :math:`n` with its algebra denoted
  :math:`\langle Z_n, \mathbf{\color{blue}+_n}, \mathbf{\color{green}\times_n}, \mathbf{\color{magenta}-_n}, 0, 1 \rangle`
| where components are defined as follows [#latexModSpace]_

.. math::

   \begin{eqnarray}
      Z_n &=& \{0,1,\dotsc\} \\
      a \mathbin{\mathbf{\color{blue}        +_n}} b &=& ( a +      b ) \;\bmod\; n \\
      a \mathbin{\mathbf{\color{green}  \times_n}} b &=& ( a \times b ) \;\bmod\; n \\
      \mathop   {\mathbf{\color{magenta}     -_n}} a &=& \begin{cases}
         0,&   a = 0 \\
         n-a,& a > 0
      \end{cases}
   \end{eqnarray}

| for each value of :math:`w`, there is
|    a bit vector boolean algebras :math:`\langle \{0,1\}^w, \mathbin{|},       \mathbin{\&}, \mathop{^\sim}, 0^w, 1^w \rangle`
|    a bit vector boolean rings    :math:`\langle \{0,1\}^w, \mathbin{^\wedge}, \mathbin{\&}, I,              0^w, 1^w \rangle`
| where :math:`\{0,1\}^w: \overline{x_1x_2 \dots x_w} \left( x_1,x_2,\dots,x_w \in \{0,1\} \right)` [#latexSpace]_
| and :math:`a^w: \underbrace{\overline{aaa \dots a}}_{w \  a\text{'s} }` |nbsp| [#latexHCB]_
| with :math:`w = 1`, bit vector boolean ring
     :math:`\langle \{0,1\}, \mathbin{^\wedge}, \mathbin{\&}, I, 0, 1 \rangle`
  is identical to ring of integers modulo two
     :math:`\langle Z_2, \mathbf{\color{blue}+_2}, \mathbf{\color{green}\times_2}, \mathbf{\color{magenta}-_2}, 0, 1 \rangle`
| but :math:`w \ge 2` yields rings very different from modular arithmetic

| :math:`\langle \mathcal{P}(S), \cup, \cap, \overline{\phantom{A}}, \varnothing, S \rangle`\ [#latexFont]_ forms a boolean algebra
|    :math:`S` is a set
|    :math:`\mathcal{P}(S)` denotes the set of all subsets of :math:`S`

*algebra* summary

.. table::
   :align: left
   :widths: auto

   ================= ======================== ===================== ====================== ================================ ============================================= =================================================== =================
    \                 set                      add                   multiply               complement                       :wp:`ID ele <identity element>` of addition   :wp:`ID ele <identity element>` of multiplication
    :math:`\langle`   :math:`\{0,1\}`          :math:`\mathbin{|}`   :math:`\mathbin{\&}`   :math:`\mathop{^\sim}`           :math:`0`                                     :math:`1`                                           :math:`\rangle`
    :math:`\langle`   :math:`\mathcal{P}(S)`   :math:`\cup`          :math:`\cap`           :math:`\overline{\phantom{A}}`   :math:`\varnothing`                           :math:`S`                                           :math:`\rangle`
   ================= ======================== ===================== ====================== ================================ ============================================= =================================================== =================

trackers
--------

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

`web asides <http://csapp.cs.cmu.edu/3e/waside.html>`__

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ===========================
    |:heavy_check_mark:|         :kbd:`DATA:BOOL`
    \                            :kbd:`DATA:TMIN`
    \                            :kbd:`DATA:TNEG`
    \                            :kbd:`ASM:IA32`
    \                            :kbd:`ASM:EASM`
    \                            :kbd:`ARCH:VLOG` [#vlog]_
    \                            :kbd:`ARCH:HCL`
    \                            :kbd:`OPT:SIMD`
    \                            :kbd:`MEM:BLOCKING`
   ============================ ===========================

:raw-html:`</details>`

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


Chapter 1: A Tour of Computer Systems
======================================

notes
-----

::

  +-------------------+
  |        CPU        |
  | +---------------+ |  System bus  +------------+  Memory bus  +-----+
  | | Bus Interface +-+--------------+ I/O Bridge +--------------+ RAM |
  | +---------------+ |              +------------+              +-----+
  +-------------------+

:abbr:`concurrency (The instructions of one process are interleaved with the instructions of another process.)`

| |sect|\ 1.9.1 :wp:`Amdahl's Law`
| |b| original execution time :math:`T_{old}`
| |b| part requires a fraction :math:`\alpha` of time
| |b| improve part's performance by a factor of :math:`k`

.. math::

   \displaystyle
   \begin{eqnarray}
                T_{new} &=& (1-\alpha) T_{old} + \alpha \frac{T_{old}}{k} \\
                        &=& T_{old}[(1-\alpha)+\alpha/k]                  \\
      \text{speedup } S &=& \frac{T_{old}}{T_{new}} = \frac{1}{(1-\alpha)+\frac{\alpha}{k}}
   \end{eqnarray}

| :wp:`wp <simultaneous multithreading>`:\ :abbr:`SMT (Simultaneous MultiThreading)`
| |b| multiple copies of some of the CPU hardware (ProgramCounter/RegisterFile/...) in one CPU
| |b| only a single copy of other parts of the hardware (FPU/...) in one CPU

trackers
--------

:raw-html:`<details close><summary>tracker (100% completed)</summary>`

.. table::
   :align: left
   :widths: auto

   ====================== =======
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
   ====================== =======

:raw-html:`</details>`


Chapter 2: Representing and Manipulating Information
====================================================

notes
-----

decimal to hexadecimal

.. math::

   \begin{eqnarray}
      D_{10} \div 16 &=& q_1 \cdots r_1 \\
      q_1    \div 16 &=& q_2 \cdots r_2 \\
      q_2    \div 16 &=& q_3 \cdots r_3 \\
      q_3    \div 16 &=& q_4 \cdots r_4 \\
      q_4    \div 16 &=& 0   \cdots r_5 \\
      D_{10}         &=& \left(\overline{r_5r_4r_3r_2r_1}\right)_{16}
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

   gcc -x c -std=gnu11 -g -O0 -Wextra -Wall -Winline -Wshadow -fanalyzer -o /tmp/a.out - <<"EOF" && /tmp/a.out
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

::

   #  001#
   #  010#
   #  100#
   # 1000#
   #10000#
   #100000#
   #1000000#

   #    1#
   #   10#
   #  100#
   #  100#
   #  100#
   #  100#
   #  100#

:raw-html:`</details>`

::

   (BE)                                                     |<--   overlap   -->|
   decimal        3510593   -> 0x00359141 ->   0000000000 1 101011001000101000001
   floating-point 3510593.0 -> 0x4A564504 ->     01001010 0 101011001000101000001 00

.. table::
   :align: left
   :widths: auto

   ========================== ====================================== ====================== ===================== ===========================
    [#latexBitwise]_           NOT                                    AND                    OR                    XOR (exclusive-OR)
    boolean operator           :math:`\neg`                           :math:`\land \wedge`   :math:`\lor \vee`     :math:`\oplus`
    logical/bitwise operator   :math:`\mathop{^\sim} \mathop{\sim}`   :math:`\mathbin{\&}`   :math:`\mathbin{|}`   :math:`\mathbin{^\wedge}`
   ========================== ====================================== ====================== ===================== ===========================

xor in and/or form

.. math::

   \displaystyle
   \begin{eqnarray}
      a \mathbin{^\wedge} b &=& (\mathop{\sim}(a\mathbin{\&}b)) \mathbin{\&} (a\mathbin{|}b) \\
                            &=& (\mathbin{\sim}a\mathbin{|}\mathbin{\sim}b) \mathbin{\&} (a\mathbin{|}b) \\
                            &=& ( x \mathbin{\&} \mathop{\sim}y ) \mathbin{|} ( \mathop{\sim}x \mathbin{\&} y ) \\
   \end{eqnarray}

| *bit vector*
| strings of zeros and ones of some fixed length :math:`w`
| :math:`[a_{w-1},a_{w-2},\dotsc,a_0]` [#latexDots]_
| subsets of a a finite set can be encoded with bit vectors

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

**in**\ tegral

:wp:`XOR swap algorithm`

| the expression ``~0`` will yield a mask of all ones
|    regardless of the size of the data representation
| the expression ``~0xFF`` creates a mask where the 8 least-significant bits equal 0 and the rest equal 1
|    also, such a mask will be generated regardless of the word size

| \
  ``|`` NOT
| \
  ``~`` bitwise-NOT

trackers
--------

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ===============================================================
    |:heavy_check_mark:|         Part I: Program Structure and Execution Preface @ page 29(64)
    |:heavy_check_mark:|         TOC
    |:heavy_check_mark:|         before 2.1
    |:hourglass_flowing_sand:|   2.1 Information Storage [58(93)]
    \                            2.2 Integer Representations
    \                            2.3 Integer Arithmetic
    \                            2.4 Floating Point
    \                            2.5 Summary
   ============================ ===============================================================

:raw-html:`</details>`


Chapter 3: Machine-Level Representation of Programs
===================================================

notes
-----

trackers
--------

Footnotes
=========

latex
-----

.. [#preqof] `key points <http://csapp.cs.cmu.edu/3e/perspective.html#:~:text=At%20Carnegie%20Mellon%2C%20our%20Introduction%20to%20Computer%20Systems%20course%20has%20become%20a%20prequisite%20for%20courses%20in%20both%20CS%20and%20ECE%20covering%3A%20operating%20systems%2C%20networking%2C%20compilers%2C%20computer%20graphics%2C%20computer%20architecture%2C%20and%20embedded%20system%20design>`__

.. [#latexBitwise]
   | SE/
     `14227  <https://tex.stackexchange.com/questions/14227>`__
     `77646  <https://tex.stackexchange.com/questions/77646>`__
     `361862 <https://tex.stackexchange.com/questions/361862>`__
   | wikibooks/`mathematics <https://en.wikibooks.org/wiki/LaTeX/Mathematics>`__
   | wikipedia/:wp:`list of logic symbols`
   | `oeis <https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols>`__

.. [#latexDots] SE/`1176 <https://tex.stackexchange.com/questions/1176>`__

.. [#latexModSpace] `mod spacing <https://tex.stackexchange.com/questions/137073>`__

.. [#latexHCB] `horizontal curly braces <https://tex.stackexchange.com/questions/46268>`__

.. [#latexSpace] `math spacing <https://www.overleaf.com/learn/latex/Spacing_in_math_mode>`__

.. [#latexFont] /ka·luh·**gra**·fuhk/ calligraphic `fonts <https://www.overleaf.com/learn/latex/Mathematical_fonts>`__

.. [#vlog] | no FPGA
           | simulation only
           | frontend - ncurses/motif/gtk
           | backend  - C simulator
           | backend  - iverilog+vpi
