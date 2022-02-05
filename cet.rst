.. include:: include/substitution.txt

==========================================
CALCULUS Early Transcendentals 8th Edition
==========================================

Misc
====

repo ``~/cet``


| CMU CS `courses <https://csd.cmu.edu/cs-and-related-undergraduate-courses>`__
  |rarr| `15-462/662 <http://15462.courses.cs.cmu.edu/>`__ Computer Graphics Spring 2022
  |rarr| prerequisites
|    :pr:`21-240`
|    :pr:`21-241`
|    :pr:`18-202`
|    `15-213/14-513/15-513 <https://www.cs.cmu.edu/~213/>`__ Introduction to Computer Systems (ICS)
|    `21-259 <https://www.math.cmu.edu/~handron/21_259/index.html>`__ Calculus in Three Dimensions

15-462/662 `youtube <https://www.youtube.com/playlist?list=PL9_jI1bdZmz2emSh0UQ5iOdT2xRHFHL7E>`__

| book site - `Stewart Calculus Textbooks and Online Course Materials <https://www.stewartcalculus.com/>`__
| ISBN-10 `1285741552 <https://www.amazon.com/dp/1285741552/>`__ [#amazonus]_
| libgen md5 ``7D475D8B3A0A1A8F1002A68EF2E8FAD7``
| ch12 - Vectors Geometry and of the Space

::

   page n(n+32)

`Pauls Online Math Notes <https://tutorial.math.lamar.edu/>`__

:r:`calculus`

`linux function plotting tools <https://www.ubuntupit.com/best-plotting-tools-for-linux-for-creating-scientific-graphs/>`__

| :kbd:`rlwrap -a /usr/bin/bc -l`
| :math:`\pi` is ``4*a(1)`` (arctan)
| :math:`\tan x` is ``s(x)/c(x)``

| :wp:`PGF/TikZ` (`github <https://github.com/pgf-tikz/pgf>`__)
| :pkg:`community/qtikz`
| :pkg:`AUR/tikzit`

:doc:`tex.rst <tex>`

.. `sphinxcontrib.programoutput <https://sphinxcontrib-programoutput.readthedocs.io/>`__
.. track exercises - ``$ ./cg.py <SUBSECTION>``

`<https://learnopengl.com/>`__


CAS
===

| :wp:`CAS <computer algebra system>` (:wp:`list <list of computer algebra systems>`)
| :aw:`list of applications#Mathematics`

| `WolframAlpha <https://www.wolframalpha.com/>`__
| `Symbolab <https://www.symbolab.com/>`__
| `Mathway <https://www.mathway.com/Algebra>`__

::

   /usr/bin/calc <<<'cot(pi()/6);exit;'
   /usr/bin/qalc <<<$'cot(pi/6)\nexit'
   /usr/bin/qalc <<<'cot(pi/6)'


0. Web, Preface and Appendices
==============================

notes
-----

:wp:`asymptote` /**a**·suhm·towt/

| ancillaries /an·**si**·lr·eez/
| logarithmic /laa·guh·**rith**·mik/
| logarithm /**laa**·gr·i·thm/

representations |vv| verbal |vv| numerical |vv| visual |vv| algebraic

| :math:`\text{heat index: } T_{perceived} = f(T_{actual},RH)`
| \
  :wp:`HI <heat index>`
  |vv| :wp:`WBT <wet-bulb temperature>`
  |vv| :wp:`DBT <dry-bulb temperature>`
  |vv| :wp:`RH <humidity#Relative_humidity>`

| Some exercise numbers are printed in red (pink):
  :raw-html:`<span style="color:red;">5.</span>`
| This indicates that :emlink:`Homework Hints <https://www.stewartcalculus.com/media/17_inside_homework_hints.php>`
  are available for the exercise

:wp:`completing the square` :math:`\displaystyle{x^2+bx+c\,=\, \left(x+{\tfrac b 2 }\right)^2 + c - \tfrac{b^2}4 }`

/kwaa·**dra**·tuhk/ :wp:`quadratic formula` :math:`\displaystyle{ x=\frac{-b\pm\sqrt{b^2-4ac}}{2a} }`

| :math:`\displaystyle { a^3-b^3=(a-b)(a^2+ab+b^2) }`
| :math:`\displaystyle { a^3+b^3=(a+b)(a^2-ab+b^2) }`

| :math:`({\color{red}x_1},{\color{blue}y_1})` and :math:`({\color{blue}x_2},{\color{red}y_2})`
| equation of the line that passes through is
  :math:`\displaystyle (x-{\color{red}x_1}) (y-{\color{red}y_2}) = (y-{\color{blue}y_1}) (x-{\color{blue}x_2})`

:abbr:`perpendicular bisector (a line which meets a segment at its midpoint perpendicularly)`

:abbr:`y-intercept (a point where the graph intersects the y-axis of the coordinate system)`

trigonometry /tri·guh·**naa**·muh·tree/

:math:`-f(x)`
   reflect about the :math:`x`-axis

:math:`\mu f(x)`
   stretch vertically by a factor of :math:`\mu`

:math:`f(x)+h`
   shift :math:`h` unit(s) upward

:math:`f(x+\phi)+h`
   shift :math:`\phi` unit(s) to the left

| `mathjax units <https://math.meta.stackexchange.com/a/27212/>`__
| :math:`360^\circ = 2\pi` :abbr:`rad (radian(s))`
| :math:`1\ \mathrm{rad} \approx 57.3^\circ` |nbsp| :math:`1^\circ \approx 0.017\ \mathrm{rad}`

| :wp:`perimeter` /pr·**i**·muh·tr/
| :wp:`circumference` /sr·**kuhm**·fr·uhns/ (:math:`2 \pi r`)

| standard position of an angle
| place its *vertex* at the origin of a coordinate system (:math:`O`)
| place its *initial side* on the positive :math:`x`-axis
| different angles can have the same *terminal side*

| or\ **tho**\ gonal /or·**thaa**·guh·nuhl/
| perpen\ **di**\ cular /pur·puhn·**di**·kyuh·lr/

.. table::
   :align: left
   :widths: auto

   ======================================================================= ========================================================================================================
                    :math:`\displaystyle \theta = 0`                        zero :wp:`angle <angle#Individual_angles>`
                :math:`\displaystyle 0 < \theta < \frac \pi 2`              acute (sharp) angle
                    :math:`\displaystyle \theta = \frac \pi 2`              right angle / :wp:`normal <normal (geometry)>` / :wp:`orthogonal <rthogonality>` / :wp:`perpendicular`
    :math:`\displaystyle \frac{\pi}{2} < \theta < \pi`                      obtuse (blunt) angle
                    :math:`\displaystyle \theta = \pi`                      straight angle
              :math:`\displaystyle \pi < \theta < 2\pi`                     reflex angle
                    :math:`\displaystyle \theta = 2\pi`                     full/complete/round angle, perigon
                    :math:`\displaystyle \theta \neq k\cdot{\frac \pi 2}`   oblique angle
   ======================================================================= ========================================================================================================

| :wp:`trigonometric functions`
| hypotenuse/hai·**paa**·tuh·noos/
| cosine/**kow**·sine/
| cosecant/kow·**see**·knt/ secant/**see**·kant/ cotangent/kow·**tan**·jnt/

acute :math:`\displaystyle 0 < \theta < \frac \pi 2` only:

.. math::

   \displaystyle\begin{array}{rlrl}
         \text{sine:} & \sin\theta=\frac{\mathrm{opposite}}{\mathrm{hypotenuse}} \qquad &  \text{cosecant:} & \csc\theta=\frac{\mathrm{hypotenuse}}{\mathrm{opposite}} \\
       \text{cosine:} & \cos\theta=\frac{\mathrm{adjacent}}{\mathrm{hypotenuse}} \qquad &    \text{secant:} & \sec\theta=\frac{\mathrm{hypotenuse}}{\mathrm{adjacent}} \\
      \text{tangent:} & \tan\theta=\frac{\mathrm{opposite}}{\mathrm{adjacent}}   \qquad & \text{cotangent:} & \cot\theta=\frac{\mathrm{adjacent}}{\mathrm{opposite}}
   \end{array}

| generic :math:`\theta\in\mathbb{R}`, including obtuse and negative:
| let :math:`P(x,y)` be any point on the terminal side of :math:`\theta`
| let :math:`r` be the distance :math:`|OP|`
|    *unit circle\:* put :math:`r=1` and the coordinates of :math:`P` becomes :math:`(\cos\theta,\sin\theta)`

.. math::

   \displaystyle\begin{array}{rlrl}
      %%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
          \text{sine:} & \sin\theta = \frac y r                           \qquad &  \text{cosecant:} & \csc\theta=\frac r y \; {\color{green}(y\neq0)} \\
        \text{cosine:} & \cos\theta = \frac x r                           \qquad &    \text{secant:} & \sec\theta=\frac r x \; {\color{blue} (x\neq0)} \\
       \text{tangent:} & \tan\theta = \frac y x \; {\color{blue}(x\neq0)} \qquad & \text{cotangent:} & \cot\theta=\frac x y \; {\color{green}(y\neq0)}
   \end{array}

| py\ **tha**\ gorean :wp:`theorem <pythagorean theorem>` /pai·**tha**·gr·ee·uhn/
| :math:`\displaystyle \mathrm{adjacent}^2+\mathrm{opposite}^2=\mathrm{hypotenuse}^2`

| :abbr:`trigonometric identity (relationship among the trigonometric functions)`
|    :math:`\tan^2\theta+1=\sec^2\theta` :guilabel:`8`
|    :math:`1+\cot^2\theta=\csc^2\theta` :guilabel:`9`
|    :math:`\sin(-\theta)=-\sin\theta` |nbsp| (sine   is an odd function)  :guilabel:`10a`
|    :math:`\cos(-\theta)= \cos\theta` |nbsp| (cosine is an even function) :guilabel:`10b`
| periodic with period :math:`2\pi`

.. \.. program-output:: /usr/bin/python3 ./cg.py appendixD

| addition formulas - all of identities 13-18 can be deduced from these two
|    :math:`\sin(x+y)=\sin{x}\cos{y}+\cos{x}\sin{y}` :guilabel:`12a`
|    :math:`\cos(x+y)=\cos{x}\cos{y}-\sin{x}\sin{y}` :guilabel:`12b`
| subtraction formulas
|    :math:`\sin(x-y)=\sin{x}\cos{y}-\cos{x}\sin{y}` :guilabel:`13a`
|    :math:`\cos(x-y)=\cos{x}\cos{y}+\sin{x}\sin{y}` :guilabel:`13b`
| :math:`\Rightarrow`
|    :math:`\displaystyle \tan(x\mathbf{\color{blue}   +}y)=\frac{\tan{x}\mathbf{\color{blue}   +}\tan{y}}{1\mathbf{\color{magenta}-}\tan{x}\tan{y}} \quad \textit{where } (x\mathbf{\color{blue}   +}y)\notin\set{ k\pi+\pi/2 \mid k\in\mathbb{Z} }` :guilabel:`14a`
|    :math:`\displaystyle \tan(x\mathbf{\color{magenta}-}y)=\frac{\tan{x}\mathbf{\color{magenta}-}\tan{y}}{1\mathbf{\color{blue}   +}\tan{x}\tan{y}} \quad \textit{where } (x\mathbf{\color{magenta}-}y)\notin\set{ k\pi+\pi/2 \mid k\in\mathbb{Z} }` :guilabel:`14b`
| double-angle formulas
|    :math:`\color{gray}  \sin{2x} =           2\sin{x}\cos{x}` :guilabel:`15a`
|    :math:`\color{gray}  \csc{2t} = \frac{1}{2}\sec{t}\csc{t}` :guilabel:`exercise50`
|    :math:`\cos{2x} = \cos^2{x}-\sin^2{x}` :guilabel:`15b`
|    :math:`\cos{2x} = 2\cos^2{x}-1` :guilabel:`16a`
|    :math:`\cos{2x} = 1-2\sin^2{x}` :guilabel:`16b`
|    :math:`\displaystyle \tan{2\theta}=\frac{2\tan\theta}{1-\tan^2\theta}` :guilabel:`exercise51`
| :math:`\Rightarrow` triple
|    :math:`\sin{3\theta}=3\sin\theta-4\sin^3\theta` :guilabel:`exercise57`
|    :math:`\cos{3\theta}=4\cos^3\theta-3\cos\theta`          :guilabel:`exercise58`
| half-angle formulas
|    :math:`\displaystyle \cos^2{x} = \frac{1\mathbf{\color{blue}   +}\cos{2x}}{2}` :guilabel:`17a`
|    :math:`\displaystyle \sin^2{x} = \frac{1\mathbf{\color{magenta}-}\cos{2x}}{2}` :guilabel:`17b`
| product formulas
|    :math:`{} {\color{Emerald}\sin x \color{purple}\cos y}=\frac{1}{2}[{\color{Emerald}\sin(x-y)}+{\color{Emerald}\sin(x+y)}] \; _{\mathcal{\frac{1}{2}[13a+12a]}}` :guilabel:`18a`
|    :math:`{} {\color{purple} \cos x \color{purple}\cos y}=\frac{1}{2}[{\color{purple} \cos(x-y)}+{\color{purple} \cos(x+y)}] \; _{\mathcal{\frac{1}{2}[13b+12b]}}` :guilabel:`18b`
|    :math:`{}  \color{gray}   \sin x               \sin y=\frac{1}{2}[\cos(x-y)-\cos(x+y)]                                    \; _{\mathcal{\frac{1}{2}[13b-12b]}}` :guilabel:`18c`

| :math:`\sin(x+k\pi)=-\sin{x} \quad k\in\mathbb{Z}`
| :math:`\cos(x+k\pi)=-\cos{x} \quad k\in\mathbb{Z}`

| :math:`{}                                  \sin    (x                                +   \frac{\pi}{2}) = \phantom{+} \cos x \quad _{\textcolor{magenta}{0}\text{ change}}`
| :math:`{}                                  \sin    (x \mathop{\mathbf{\color{magenta}-}} \frac{\pi}{2}) =          -  \cos x \quad _{\textcolor{magenta}{1}\text{ change, negate}}`
| :math:`\mathop{\mathbf{\textcolor{magenta}{\cos}}} (x                                +   \frac{\pi}{2}) =          -  \sin x \quad _{\textcolor{magenta}{1}\text{ change, negate}}`
| :math:`\mathop{\mathbf{\textcolor{magenta}{\cos}}} (x \mathop{\mathbf{\color{magenta}-}} \frac{\pi}{2}) = \phantom{+} \sin x \quad _{\textcolor{magenta}{2}\text{ changes}}`

`graphs of the trigonometric functions <https://www.desmos.com/calculator/nlfjfdf3kp>`__

:math:`\cot(\frac{\pi}{2}-x)=\tan{x}`

| graphs of :math:`\csc{x}` and :math:`\sec{x}`
|    let :math:`f(x)=\sin{x},\ g(x)=\csc{x}`
|    or  :math:`f(x)=\cos{x},\ g(x)=\sec{x}`
| :wp:`contacts <contact (mathematics)>` between :math:`f(x)` and :math:`g(x)` are :math:`\set{ (x,y) \mid (y=1 \vee y=-1) \wedge f(x)=y}`
| asymptotes of :math:`g(x)` are :math:`\set{ x=\varphi \mid f(\varphi)=0}`
| range of :math:`g(x)` is :math:`(-\inf,-1]\cup[1,+\inf)`

| :math:`(\sin{x}+\cos{x})^2=1+\sin{2x}` :guilabel:`exercise44`

.. tip::

   | For proof of trigonometric equations,
   | try eliminating :pr:`tan()` :pr:`csc()` :pr:`set()` :pr:`cot()` and converting to :kbd:`sin(),cos()`-only,
   | which makes :math:`\sin^2+cos^2` easy to find or construct.

.. tip:: To sketch :math:`f(x)={A}sin(\omega{x}+\varphi)+h` with the least repeat work

   1. Draw (dotted) auxiliary lines :math:`y=h`, :math:`y=h+A` and :math:`y=h-A`
   #. Draw the :math:`x`-axis
   #. Sketch 2 :math:`\sin` curves, one in between the auxiliary lines and one standalone
   #. Label :math:`x`-coordinates of key points of the standalone curve as raw :math:`y=sin(x)`
   #. Label :math:`x`-coordinates of key points of the auxed curve onto the :math:`x`-axis, applying :math:`-\varphi` offset
   #. Calculate :math:`f(0)`, draw the :math:`y`-axis and :math:`O`
   #. Done

| :wp:`law of cosines`
|    :math:`|BC|^2 = |AB|^2 + |AC|^2 - 2\cdot|AB|\cdot|AC|\cdot\cos\angle{ABC}` :guilabel:`exercise83`

| :wp:`tangential polygon` /tan·**jen**·chl/
| :wp:`circumscribed circle` /**sur**·kuhm·skribed/

| calculus
|    integral calculus (ancient Greeks)
|    differential calculus (17\ :sup:`th` century)

trackers
--------

book preface

:raw-html:`<details close><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ====================================================
    |:heavy_check_mark:|         Front Cover
    |:heavy_check_mark:|         Title Page
    |:heavy_check_mark:|         Copyright Page
    |:heavy_check_mark:|         CONTENTS
    |:heavy_check_mark:|         Preface.P..A..W..F..C..A..A..A..
    |:heavy_check_mark:|         To the Student
    |:heavy_check_mark:|         Calculators, Computers, and Other Graphing Devices
    |:heavy_check_mark:|         A Diagnostic Test: Algebra
    |:heavy_check_mark:|         B Diagnostic Test: Analytic Geometry
    |:heavy_check_mark:|         C Diagnostic Test: Functions
    |:heavy_check_mark:|         D Diagnostic Test: Trigonometry
    |:heavy_check_mark:|         A Preview of Calculus [3(35)]
   ============================ ====================================================

:raw-html:`</details>`

web `home <https://www.stewartcalculus.com/media/17_home.php>`__

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ===========================================================================
    |:heavy_minus_sign:|         Review - Algebra (passed *A Diagnostic Test: Algebra*, no need to review)
    \                            Review - Analytic Geometry
    \                            Lies My Calculator and Computer Told Me
    \                            Challenge Problems
   ============================ ===========================================================================

:raw-html:`</details>`

web `additional topics <https://www.stewartcalculus.com/media/17_inside_topics.php>`__

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ==================================================
    \                            Fourier Series
    \                            Formulas for the Remainder Term in Taylor Series
    \                            Rotation of Axes
   ============================ ==================================================

:raw-html:`</details>`

book appendices

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ =================================================
    \                            A\. Numbers, Inequalities, and Absolute Numbers
    \                            B\. Coordinate Geometry and Lines
    \                            C\. Graphs of Second-Degree Equations
    |:heavy_check_mark:|         D\. Trigonometry - [A28(1242)]
    \                            E\. Sigma Notation
    \                            F\. Proofs of Theorems
    \                            G\. The Logarithm Defined as an Integral
    \                            H\. Complex Numbers
    \                            I\. ANSWERS to Odd-Numbered Exercises
   ============================ =================================================

:raw-html:`</details>`


1. Functions and Models
=======================

notes
-----

| :math:`f: x \rightarrow f(x),\; x \in D,\; f(x) \in E\; ( D\in\mathbb{R} \wedge E\in\mathbb{R} )`
| :math:`y=f(x)`
| :math:`x` is an independent variable
| :math:`y` is a  dependent   variable

| difference quotient :math:`\displaystyle \frac{f(a+h)-f(a)}{h}`
| the average rate of change of :math:`f(x)` between :math:`x=a` and :math:`x=a+h`

4 possible ways to represent functions

.. table::
   :align: left
   :widths: auto

   ===================== ===========================
    **ver**\ bally         by a description in words
    **num**\ erically      by a table of values
    **vis**\ ually         by a graph
    **alg**\ ebraically    by an explicit formula
   ===================== ===========================

mathematical model is a function with an explicit formula that approximates the behavior of a given function

:wp:`amplitude`

faucet /**faa**·suht/

parabola /pr·**a**·buh·luh/





trackers
--------

:raw-html:`<details open><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ====================================================
    |:heavy_check_mark:|         1.1
    |:hourglass_flowing_sand:|   1.1 EXERCISES
    \                            1.2
    \                            1.2 EXERCISES
    \                            1.3
    \                            1.3 EXERCISES
    \                            1.4
    \                            1.4 EXERCISES
    \                            1.5
    \                            1.5 EXERCISES
    \                            Review
    \                            Princibles of Problem Solving
   ============================ ====================================================

:raw-html:`</details>`


2. Limits and Derivatives
=========================

notes
-----

trackers
--------


Footnotes
=========

.. [#amazonus] To reveal US edition books, use US-based IP address, and set Amazon delivery to US zip code.
