.. include:: include/substitution.txt

===
CG
===

Misc
====

:wp:`James Stewart <James Stewart (mathematician)>`

`CMU CS <https://csd.cmu.edu/cs-and-related-undergraduate-courses>`__

`15-462/662 Fall 2021 <http://15462.courses.cs.cmu.edu/>`__

| preqs
| 15-213/18-213/18-613 - CSAPP
| :pr:`21-240`
| :pr:`21-241`
| :pr:`18-202`

`21-259 Calculus in Three Dimensions <https://www.math.cmu.edu/~handron/21_259/index.html>`__

`youtube <https://www.youtube.com/playlist?list=PL9_jI1bdZmz2emSh0UQ5iOdT2xRHFHL7E>`__

| `Stewart Calculus Textbooks and Online Course Materials <https://www.stewartcalculus.com/>`__
| ch12 - Vectors Geometry and of the Space

`Pauls Online Math Notes <https://tutorial.math.lamar.edu/>`__

`r/calculus <https://www.reddit.com/r/calculus/>`__

amazon set delivery to US zip code for US edition

ISBN-10 `1285741552 <https://www.amazon.com/dp/1285741552/>`__

::

   page n(n+32)

`linux function plotting tools <https://www.ubuntupit.com/best-plotting-tools-for-linux-for-creating-scientific-graphs/>`__

| :kbd:`rlwrap -a /usr/bin/bc -l`
| :math:`\pi` is ``4*a(1)`` (arctan)
| :math:`\tan x` is ``s(x)/c(x)``

| :wp:`PGF/TikZ` (`github <https://github.com/pgf-tikz/pgf>`__)
| :pkg:`community/qtikz`
| :pkg:`AUR/tikzit`

:doc:`tex.rst <tex>`

`sphinxcontrib.programoutput <https://sphinxcontrib-programoutput.readthedocs.io/>`__
track exercises - ``$ ./cg.py <SUBSECTION>``


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
| :math:`\tan^2\theta+1=\sec^2\theta`
| :math:`1+\cot^2\theta=\csc^2\theta`
| :math:`\sin(-\theta)=-\sin\theta` |nbsp| (sine   is an odd function)
| :math:`\cos(-\theta)= \cos\theta` |nbsp| (cosine is an even function)
| periodic with period :math:`2\pi`

.. program-output:: /usr/bin/python3 ./cg.py appendixD

| addition formulas
|    :math:`x`
|    :math:`x`
| subtraction formulas
|    :math:`x`
|    :math:`x`
| double-angle formulas
|    :math:`x`
|    :math:`x`
| half-angle formulas
|    :math:`x`
|    :math:`x`
| product formulas
|    :math:`x`
|    :math:`x`

trackers
--------

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

book preface

:raw-html:`<details open><summary>tracker</summary>`

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
    |:hourglass_flowing_sand:|   D Diagnostic Test: Trigonometry
    \                            A Preview of Calculus
   ============================ ====================================================

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
    |:hourglass_flowing_sand:|   D\. Trigonometry - [A28(1242)]
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

trackers
--------

:raw-html:`<details><summary>tracker</summary>`

.. table::
   :align: left
   :widths: auto

   ============================ ====================================================
    \                            1.1
    \                            1.2
    \                            1.3
    \                            1.4
    \                            1.5
    \                            Review
   ============================ ====================================================

:raw-html:`</details>`


2. Limits and Derivatives
=========================

notes
-----

:wp:`asymptote` /**a**·suhm·towt/
