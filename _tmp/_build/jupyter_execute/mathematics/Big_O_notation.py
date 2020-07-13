<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Introduction-and-notation" data-toc-modified-id="Introduction-and-notation-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction and notation</a></span></li><li><span><a href="#Mathematical-explanation" data-toc-modified-id="Mathematical-explanation-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Mathematical explanation</a></span><ul class="toc-item"><li><span><a href="#Example" data-toc-modified-id="Example-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Example</a></span></li></ul></li><li><span><a href="#Use-in-Computer/Computational-Science" data-toc-modified-id="Use-in-Computer/Computational-Science-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Use in Computer/Computational Science</a></span></li></ul></div>

# Big O notation

## Introduction and notation

In the notebook on Taylor series we arrived at the infinite Taylor series *about (or around) the point $x_0$*:

$$f(x) = f(x_0) + (x - x_0) f'(x_0) + \frac{(x - x_0)^2}{2!} f''(x_0) + \frac{(x - x_0)^3}{3!} f'''(x_0) +
\frac{(x - x_0)^4}{4!} f^{(iv)}(x_0) + \ldots$$

and we pointed out that an equivalent way of writing this expansion is

$$ f(x_0+h)  = f(x_0) + hf'(x_0) + \frac{h^2}{2!}f''(x_0) + \frac{h^3}{3!}f'''(x_0) + \ldots $$

or replace $h$ by the notation $\Delta x$ or $\delta x$.

When talking about terms in infinite series (terms we will often be forces to truncate, i.e. throw away), or talking about errors, convergence, complexity, run times etc, so-called [Big-O](https://en.wikipedia.org/wiki/Big_O_notation) is very useful.

What this means is that mathematically we have some notation that allows us to write these infinite expansions in forms such as

$$f(x) = f(x_0) + (x - x_0) f'(x_0) + \frac{(x - x_0)^2}{2!} f''(x_0) + \frac{(x - x_0)^3}{3!} f'''(x_0) + \mathcal{O}((x - x_0)^4)$$

or

$$ f(x_0+h) = f(x_0) + hf'(x_0) + \frac{h^2}{2!}f''(x_0) + \frac{h^3}{3!}f'''(x_0) + \mathcal{O}(h^4) $$


But what does this mean?

## Mathematical explanation

Well simply $\mathcal{O}$ here means "order".

More formally it is used to signify (place bounds on) the limiting behaviour of the magnitude of a mathematical term (or an algorithm's runtime).

So based on the the example above we have simply replaced the terms 

$$ \frac{h^4}{4!} f^{(iv)}(x_0) +  \frac{h^5}{5!} f^{(v)}(x_0) + \ldots $$

with 

$$ \mathcal{O}(h^4) $$

"in the limit" (and implicitly for this use application we are interested in the limit as $h\rightarrow 0$)

i.e. we have written that

$$ \frac{h^4}{4!} f^{(iv)}(x_0) +  \frac{h^5}{5!} f^{(v)}(x_0) + \ldots  =  \mathcal{O}(h^4) $$

this is stating that as $h$ tends to zero the LHS can bounded in magnitude by a term of the form

$$ C h^4 $$

where $C$ is a constant, i.e. there exists a constant $C$ such that for all sufficiently small $h$

$$\left| \frac{h^4}{4!} f^{(iv)}(x_0) +  \frac{h^5}{5!} f^{(v)}(x_0) + \ldots \right| \le C h^4 $$

In our case the point is that, assuming $f$ is a well-behaved function, i.e. it's derivatives are bounded, then there will be a small enough $h$ such that the terms dependent on the 5th and higher powers or $h$ are very small relative to the first term 

They can't be ignored, but we can select a $C$ which is a bit larger than original factor ${h^4}/{4!}$ so that the above holds.

The point here isn't to actually find $C$, this is just notation to help convey a point.

It's important when analysing errors in algorithms.

Note that for this case we were considering the limit of small $h$ and so the lowest power eventually becomes dominant, the opposite situation would occur if we were considering the limit of large $h$.

With errors we are generally thinking about the former case, with run-times (where $h$ might be replaced with some measure of the size of the problem) we are in the latter case.

### Example

Consider

$$g(y) = 3y^2 - y^3 + 9y^4$$

in the limit as $y\rightarrow 0$.

We can show that

$$\left| 3y^2 - y^3 + 9y^4 \right| \le \left| 3y^2\right| + \left|y^3\right| + \left|9y^4 \right| \le 3y^2 + y^2 + 9y^2 \le 13 y^2$$

as we are considering the case as $y$ gets small. Hence we can write 

$$g(y) = 3y^2 - y^3 + 9y^4 = \mathcal{O}(y^2) \quad\text{as}\quad y\rightarrow 0$$


If we were considering the case of $y\rightarrow \infty$, then we would write instead

$$g(y) = \mathcal{O}(y^4) \quad\text{as}\quad y\rightarrow \infty$$


When dealing with numerical errors you may see things like

$$\text{error} \approx 10^{-5}\Delta t +  10^{5}\Delta t^2$$

For larger values of $\Delta t$ the second term will clearly dominate due to the relative size of the constant in front of it compared to the first term.

But when performing a convergence analysis, i.e. investigating how the error drops as $\Delta t$ is reduced, there will come a point for small enough $\Delta t$ that the first term starts to dominate, and from the point onwards the error will decay linearly rather than quadratically, i.e. halving $\Delta t$ leads to a reduction in the error by a factor of 2 rather than 4.

So we would say that 

$$\text{error} = \mathcal{O}(\Delta t)$$

even though at larger $\Delta t$ values the error would be observed to decay quadratically as we reduce $\Delta t$.

We use the expression "in the asymptotic limit" to refer to region of parameter space where the leading order behaviour dominates. For the above example if we observe something that looks like second order behaviour (when we expect first) we would explain this away by saying that we are not in the asymptotic limit. If we see very close to first order behaviour then we would say we are in the asymptotic limit.

## Use in Computer/Computational Science

For the cost of algorithms we use the notation in a similar manner.

An algorithm is said to have (*time* or *algorithmic* or *computational*) [complexity](https://en.wikipedia.org/wiki/Time_complexity) of $\mathcal{O}(n^2)$ for example,
if for large enough $n$, where $n$ is a measure of the problem size, the computational cost grows quadratically - for every doubling of the problem size the cost grows by a factor 4.

When it comes to complexity it's quite common to see things like $\mathcal{O}(n \log n)$, i.e. the algorithm scales worse than linearly, but not as bad as quadratically.

For some examples see <https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations>

