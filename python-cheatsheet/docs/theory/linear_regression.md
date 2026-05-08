# Linear regression

The core idea:

an **input variable** (independent variable, `x`)
an **output variable** (dependent variable, `y`)

> Linear regression tries to find the best straight line that predicts `y` from `x`.

## Score function $f_{score}$

$y=mx+b$ where

Where:

* $m$ = slope (how much y changes when x changes)
* $b$ = intercept (value of $y$ when $x=0$)

## Fit -  Least square

The algorithm chooses `m` and `b` to minimize the error between:

* **actual values** (real data)
* **predicted values** (line)

This is usually done using **least squares**, which minimizes:

$KaTeX$ https://katex.org/

$f_{fit}=\sum(y_{actual}−y_{predicted})^2$

## Example

Input:

`x` = hours studied

`y` = exam score

Linear regression finds a line like:

“_each extra hour studied increases the score by 5 points_”

So if:

slope $m=5$
intercept $b=50$

Then the score function is:

$f_{score}=5x+50$

2 hours → score = 60

5 hours → score = 75

### Multiple linear regression

In case of multuple variables (dimensions):
 
* hours studied $x_1$
* sleep $x_2$
* attendance $x_3$

The model becomes:

$f_{score}=x_1*m_1 + x_2*m_3 + ... + x_n*m_n + b$


Still linear—just in more dimensions.

