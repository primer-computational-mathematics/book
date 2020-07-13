# Introduction

In complex analysis we are dealing with the set of complex numbers $\mathbb{C}$ which are ordered pairs of the form $(x, y)$, where $x$ and $y$ are real numbers. If we introduce the imaginary unit $i = \sqrt{-1}$ we can write it in its *rectangular form*:

$$ z = x + iy 
$$ (rectform)

Every complex number $z = x + iy$ has a **real part** Re$z = x$ and an **imaginary part** Im$z = y$. Sometimes $\mathfrak{R}(z)$ and $\mathfrak{I}(z)$ are used instead of Re and Im. Two complex numbers $z_1$ and $z_2$ are equal iff their real and imaginary parts are equal,

$$ z_1 = z_2 \iff \text{Re}(z_1) = \text{Re}(z_2) \wedge \text{Im}(z_1) = \text{Im}(z_2). $$

If Re$(z) = 0$ and Im$(z) \neq 0$ we say that $z$ is *pure imaginary*. On the other hand, if Im$(z) = 0$ and Re$(z) \neq 0$ we recover the *pure real* number $x$. Therefore, we identify real numbers as complex numbers whose imaginary part is equal to 0, so $\mathbb{R}$ is a subset of $\mathbb{C}$, i.e. $\mathbb{R} \subset \mathbb{C}$.

# Basic operations

## Addition and multiplication

Adding complex numbers is performed by adding real and imaginary parts separately:

$$ z_1 \pm z_2 = (x_1 + i y_1) \pm (x_2 + iy_2) = (x_1 \pm x_2) + i(y_1 \pm y_2) $$

Multiplying two complex numbers is done by expanding the brackets and grouping real and imaginary parts:

$$ \begin{align}
z_1 \cdot z_2 & = (x_1 + i y_1) \cdot (x_2 + iy_2) = x_1 x_2 + i^2 y_1 y_2 + i x_1 y_2 + i x_2 y_1 \\
& = (x_1 x_2 - y_1 y_2) + i(x_1 y_2 + x_2 y_1).
\end{align} $$

## Complex conjugate
```{index} Complex conjugate
```

For every complex number $z = x + iy$ we define its **complex conjugate** $z^*$ or $\overline{z}$ by changing the sign of its imaginary part:

$$ z^* \equiv x - iy $$

This is an [involutory operation](https://en.wikipedia.org/wiki/Involution_(mathematics)) since $ (z^*)^* = z $ with the following properties:

$$ (z_1 \pm z_2)^* = z_1^* \pm z_2^* \\
(z_1 \cdot z_2)^* = z_1^* \cdot z_2^* \\
(z^{-1})^* = (z^*)^{-1} $$

We can write the real and imaginary parts of $z$ using the complex conjugate:

$$ \text{Re}(z) = \frac{1}{2} (z + z^*), \quad \text{Im}(z) = \frac{1}{2i} (z - z^*) $$

## Modulus 

```{index} Modulus
```

To every complex number $z$ we assign a modulus (absolute value) $| z |$, a non-negative real number defined as:

$$ | z | \equiv \sqrt{x^2 + y^2} 
$$ (mdls)

Zero is the only complex number whose modulus is 0. 

```{admonition} Properties of a modulus
```

The modulus of a complex number satisfies the following properties:

$$ |z_1| \cdot |z_2| = |z_1 z_2|, \quad | z^{-1} | = |z|^{-1}, $$

$$|z^*| = |z|, \quad z^* \cdot z = |z|^2 $$

## Division

We divide a complex number $z_1$ by another complex number $z_2 \neq 0$ by expanding the fraction such that the denominator becomes a real number. We do this by multiplying both the numerator and the denominator by $z_2^*$ (see the last property of a modulus above).

$$ \begin{align}
\frac{z_1}{z_2} & = \frac{x_1 + iy_1}{x_2 + iy_2} = \frac{x_1 + iy_1}{x_2 + iy_2} \cdot \frac{x_2 - iy_2}{x_2 - iy_2} \\
& = \left ( \frac{x_1x_2 + y_1y_2}{x_2^2 + y_2^2} \right ) + i \left ( \frac{x_2y_1- x_1y_2}{x_2^2 + y_2^2} \right ) 
\end{align} $$

## Multiplicative inverse

Let us find the inverse of a complex number $z = x + iy$:

$$ \begin{align}
z^{-1} & = \frac{1}{z} = \frac{1}{x + iy} \cdot \frac{x - iy}{x -iy} = \frac{x - iy}{x^2 + y^2} \\ & = \frac{x}{x^2 + y^2} -i \frac{y}{x^2 + y^2}
\end{align} $$

