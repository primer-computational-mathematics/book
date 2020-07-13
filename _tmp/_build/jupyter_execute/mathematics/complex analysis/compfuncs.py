# Complex functions

A complex function is a function that has a subset of the complex numbers as a domain and the complex numbers as a codomain:

$$ f : D \to \mathbb{C}, \quad D \subset \mathbb{C}. $$

We say that $f$ is a function of a complex variable. A complex function $f(z)$ may also be resolved into its real part $u(x, y)$ and imaginary part $v(x, y)$:

$$ f(z) = f(x + iy) = u(x, y) + iv(x, y), $$

where $u$ and $v$ are functions of two real variables.

## Polynomials

A complex polynomial of $n$-th degree is a function $p : \mathbb{C} \to \mathbb{C}$ of the form

$$ p_n (z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_1 z + a_0 $$

where $a_0, \dots, a_n \in \mathbb{C}$ are the coefficients of the polynomial and $a_n \neq 0$. A polynomial of $n$-th degree has exactly $n$ roots, but some of them may be equal.

For example, the function $p(z) = 2z^4 + (2-3i)z^2 + 1$ is a third degree (complex) polynomial.

## Rational functions

A rational function is a function of the form

$$ r(z) = \frac{p(z)}{q(z)}, $$

where $p$ and $q$ are polynomials. The natural domain of $r$ is the set of all complex numbers such that $q$ is not a null-polynomial,

$$ D = \{ z \in \mathbb{C} : q(z) \neq 0 \}. $$

For example, the function

$$ r(z) = \frac{z^4 + 2z - 3}{z^2 + 3} $$

has a domain $D = \{ z \in \mathbb{C} : z^2 + 3 \neq 0 \} = \mathbb{C} \setminus \{ \pm i \sqrt{3} \}$.

## Exponential function

The complex exponential function $\exp : \mathbb{C} \to \mathbb{C}$ is defined by extending the Taylor series of the real exponential to complex numbers. TODO: put this example somewhere?

$$ exp(z) \equiv e^x (\cos y + i \sin y) = e^x e^{iy}$$

This is what allows us to represent complex numbers in polar form. The usual properties of an exponential function still apply:

$$ e^{z_1 + z_2} = e^{z_1} e^{z_2}, \quad \frac{1}{e^z} = e^{-z}, \quad e^{z_1 - z_2} = \frac{e^{z_1}}{e^{z_2}}. $$

It is easy to separate $e^z$ into its real $u(x, y)$ and imaginary $v(x, y)$ part: $ \text{Re}(e^z) = e^x \cos y$, $\text{Im}(e^z) = e^x \sin y$.

```{margin} This is an interactive figure!
Make sure to rotate and move around the figure.
```

import numpy as np
import plotly.offline
import plotly.graph_objects as go


x = np.linspace(-2, 2, 101)
y = np.linspace(-10, 10, 501)
X, Y = np.meshgrid(x, y)
f = np.exp(X) * np.exp(1j*Y)

fig = go.Figure(data=[go.Surface(z=f.real, x=x, y=y)])
fig.update_layout(title='Real part of exp(z)', autosize=True)
fig

Or both the real and imaginary part as a heat map:

import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 2, figsize=(8, 8), sharey=True)

im = ax[0].contourf(f.real, levels=12, cmap='inferno', extent=[-2, 2, -10, 10])
ax[0].contour(f.real, levels=12, colors='k', extent=[-2, 2, -10, 10], linewidths=1.)
fig.colorbar(im, ax=ax[0])
ax[0].set_title('Real')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

im = ax[1].contourf(f.imag, levels=12, cmap='inferno', extent=[-2, 2, -10, 10])
ax[1].contour(f.imag, levels=12, colors='k', extent=[-2, 2, -10, 10], linewidths=1.)
fig.colorbar(im, ax=ax[1])
ax[1].set_title('Imaginary')
ax[1].set_xlabel('x')

plt.tight_layout()
plt.show()

Notice that a complex exponential function consists of a growing/decaying part $e^x$ and a periodic/oscillating part $\cos y + i \sin y$. Therefore, the complex exponential function is also periodic with a period $2\pi i$:

$$ e^{z + 2\pi i} = e^z. $$

Whether $e^x$ will grow or decay depends on the sign of $x$; it will grow if $x > 0$ and it will decay if $x < 0$. If $x=0$ it will just oscillate with unit amplitude, it will neither grow nor decay. Let us calculate the magnitude and phase of $e^z$:

$$ |e^z| = |e^x (\cos y + i \sin y) | = e^x (\cos^2y + \sin^2y) = e^x \\
\text{arg}(e^z) = \text{arg}(e^x) + \text{arg}(e^{iy}) = 0 + y = y$$

Since $e^x > 0$ for all $x$, we conclude that $e^z \neq 0$ for all $z \in \mathbb{C}$. So $0$ is not in the image of the exponential function, but all other complex numbers are.

Remember that the argument is periodic.

fig, ax = plt.subplots(1, 2, figsize=(8, 8), sharey=True)

im = ax[0].contourf(np.abs(f), levels=12, cmap='inferno', extent=[-2, 2, -10, 10])
ax[0].contour(np.abs(f), levels=12, colors='k', extent=[-2, 2, -10, 10], linewidths=1.)
fig.colorbar(im, ax=ax[0])
ax[0].set_title('abs')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

# We could have imported cmath and then cmath.phase(f)

im = ax[1].contourf(np.arctan2(f.imag, f.real), levels=12, cmap='inferno', extent=[-2, 2, -10, 10])
ax[1].contour(np.arctan2(f.imag, f.real), levels=12, colors='k', extent=[-2, 2, -10, 10], linewidths=1.)
fig.colorbar(im, ax=ax[1])
ax[1].set_title('phase')
ax[1].set_xlabel('x')

plt.tight_layout()
plt.show()

## Logarithm

We would like to extend the idea of a logarithm being the inverse of the exponential function, but since the complex exponential function is not bijective, the inverse function does not exist. What we mean is that the logarithm cannot be a single-valued function since $z = |z| e^{i(arg(z) + 2n \pi)}$ has the same value of the logarithm for all integers $n$ since it is periodic. However, as we saw above, the complex exponential function is injective on an interval of length $2 \pi$ so we can define an inverse on that interval.

Since the exponential function maps a sum to a product (i.e. $ e^{a+b} = e^a e^b $), the logarithm of a product must be equal to the sum of their logarithms (i.e. $ \ln(z_1 z_2) = \ln(z_1) + \ln(z_2) $):

$$ \begin{align}
Ln(z) & = Ln(|z|e^{i Arg(z)}) =  \ln(|z|) + \ln(e^{i Arg(z)}) \\
&:= \ln(|z|) + i(arg(z) + 2n \pi), \qquad n \in \mathbb{Z},
\end{align}$$

As with the argument (note the capital $Arg$ and $Ln$), we define the principal value of a logarithm for $n = 0$:

$$ \ln(z) = \ln(|z|) + i arg(z) $$

```{admoniton} Examples

$$ Ln(1) = \ln(1) + i(arg(1) + 2n \pi) = 2n \pi i, \quad \ln(1) = 0 $$

$$ Ln(i) = i \left (\frac{\pi}{2} + 2n \pi \right ), \quad \ln(i) = \frac{\pi i}{2}$$

$$ Ln(-i) = i \left ( -\frac{\pi}{2} + 2n \pi \right ), \quad \ln(-i) = - \frac{\pi i}{2} $$
```

## Trigonometric and hyperbolic functions

Trigonometric and hyperbolic functions of a complex variable are defined with the exponential function:

$$ 
\begin{aligned}
\sin z & \equiv \frac{e^{iz} - e^{-iz}}{2i} \\
\cos z & \equiv \frac{e^{iz} + e^{-iz}}{2} \\
\tan z & \equiv \frac{\sin z}{\cos z} \\
\cot z & \equiv \frac{\cos z}{\sin z}
\end{aligned} \qquad
\begin{aligned}
\sinh & \equiv \frac{e^{z} - e^{-z}}{2} \\
\cosh & \equiv \frac{e^{z} + e^{-z}}{2} \\
\tanh z & \equiv \frac{\sinh z}{\cosh z} \\
\coth z & \equiv \frac{\cosh z}{\sinh z}
\end{aligned}$$

```{admonition} Properties
We can check directly that the following is valid:

$$ e^{1z} = \cos z + i \sin z, \quad \forall z \in \mathbb{C}. $$

Addition formulae are valid:

$$ \sin (z_1 + z_2 ) = \sin z_1 \cos z_2 + \cos z_1 \sin z_2 \\
\cos (z_1 + z_2) = \cos z_1 \cos z_2 - \sin z_1 \sin z_2 $$

and

$$ \sin^2 z + \cos^2 z = 1, \quad \sin(z + 2\pi) = \sin z, \quad \cos (z + 2\pi) = \cos z $$

```

