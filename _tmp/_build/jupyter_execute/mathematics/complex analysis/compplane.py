# Complex plane

```{index} Complex plane
```

From the definition of complex numbers it is clear that there is a natural correspondence between a set of complex numbers $\mathbb{C}$ and points in a plane: to every complex number $z = x +iy$ we can *uniquely* assign a point $P(x, y)$ in the $\mathbb{R}^2$ plane. We call a plane in which every point has a corresponding complex number assigned to it a **complex plane** (or Argand plane). However, for simplicity we would normally simply say "in a point $z$" when we mean "in a point (of a complex plane) assigned a complex number $z$."

z = complex(3, 2)

fig = plt.figure()
ax = fig.add_subplot(111)
    
plt.plot(z.real, z.imag, 'o', zorder=10)
plt.plot([3, 3], [0, 2], '--k', alpha=0.8)
plt.plot([0, 3], [2, 2], '--k', alpha=0.8)

ax.text(2.7, -0.25, "$Re(z)$", fontsize=12)
ax.text(-0.7, 1.95, "$Im(z)$", fontsize=12)

ax.arrow(-1., 0, 4.5, 0, shape='full', head_width=0.1, head_length=0.2)
ax.arrow(0, -1.5, 0, 4, shape='full', head_width=0.1, head_length=0.2)

ax.axis('equal')
ax.set_xlim(-2, 4)
ax.set_ylim(-2, 4)
ax.axis('off')

plt.show()

Having represented complex numbers geometrically, let us revisit the terms we introduced in the first notebook.

- Re $z$ is equal to the abscissa and Im $z$ to the ordinate of a point $P$. We therefore call x-axis the *real axis* and y-axis the *imaginary axis*.

- The modulus of a complex number $|z|$ is equal to the distance between the corresponding point $P$ and the origin of the complex plane. In general, the distance between points $P_1$ and $P_2$ assigned to numbers $z_1$ and $z_2$ is equal to the modulus of the difference of those two points:

$$ d(T_1, T_2) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} = | z_1 - z_2 |$$

- If a number $z$ is assigned a point $P(x, y)$, then the complex conjugate $z^*$ is assigned a point $P^*(x, -y)$, which is just a reflection of $P$ with respect to the real axis.

- Every point $P(x, y)$ has a corresponding vector $\vec{OP}$ from the origin to $P$. The sum $z_1 + z_2$ therefore represents vector addition $ \overrightarrow{OP_1} + \overrightarrow{OP_2} $.

Because of the vector analogy, we can also say that complex numbers satisfy the *triangle inequalities*:

$$ | z_1| - |z_2| \leq |z_1 + z_2| \leq |z_1| + |z_2| $$

# Trigonometric form

```{sidebar} Complex plane - Argand diagram
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Complex_conjugate_picture.svg/800px-Complex_conjugate_picture.svg.png" height="300">

Source: [Wikipedia](https://en.wikipedia.org/wiki/Complex_plane)
```

We can also observe the complex plane in polar coordinates $(r, \phi)$ which are related to the Cartesian coordinates $(x, y)$ through:

$$ x = r \cos \varphi, \quad y = r \sin \varphi $$

This leads to the *trigonometric form* of a complex number $z$:

$$ z = r(\cos \varphi + i \sin \varphi), $$

where $r$ is the **modulus** (or magnitude), equal to the absolute value of the complex number, a direct consequence of Pythagora's theorem:

$$ r = \sqrt{x^2 + y^2} = |z| $$

and the polar angle $\varphi$ is defined (to a multiply $2\pi$ by:

$$ \tan (\varphi + 2n \pi) = \frac{y}{x}, \quad n \in \mathbb{R}, x \neq 0. $$

The angle $\varphi$ is called the **argument** (or phase) of a complex number $z$ and we write $\text{Arg}(z) = \varphi$. A special case is the complex number $z=0$ for which $r = 0$ and its argument is not defined. 

Finding $\varphi$ is delicate because $\tan$ is a multivalued function. To avoid ambiguity, the simplest choice is $n = 0$ so that the interval is of length $2\pi$ and $ - \pi < \text{arg}(z) \leq \pi $. The value of $\text{Arg}(z)$ with $n=0$ is called the **principal value** of the argument. With this:

$$ \text{arg}(1) = 0, \quad \text{arg}(i) = \frac{\pi}{2}, \quad \text{arg}(-1) = \pi, \quad \text{arg}(-i) = -\frac{\pi}{2}, \quad \text{etc.} $$

THe relationship between $\text{Arg}(z)$ and $\text{arg}(z)$ is therefore:

$$ \text{Arg}(z) = \text{arg}(z) + 2n \pi, \quad n \in \mathbb{Z}.$$

Multiplying two complex numbers results in their absolute values being multiplied and the arguments being added:

```{margin} Angle addition formulae
$$ \sin(\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta \\
\cos (\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta$$
```

$$ \begin{align}
z_1 \cdot z_2 & = r_1(\cos \varphi_1 + i \sin \varphi_1) \cdot r_2(\cos \varphi_2 + i \sin \varphi_2) \\
& = r_1 r_2 (\cos (\varphi_1 + \varphi_2) + i \sin(\varphi_1 + \varphi_2))
\end{align} $$

For the multiplicative inverse we have

$$ \begin{align}
z^{-1} & = \frac{1}{r(\cos \varphi + i \sin \varphi)} \cdot \frac{cos \varphi - i \sin \varphi}{cos \varphi - i \sin \varphi} = \frac{\cos \varphi - i \sin \varphi}{r( \cos^2 \varphi + \sin^2 \varphi)} \\
& = \frac{1}{r} (\cos \varphi - i \sin \varphi) \end{align} $$

```{admonition} Properties of $|z|$ and arg($z$)
Let us summarise our findings in the form of the following equalities:

$$ | z_1 \cdot z_2 | = |z_1| \cdot |z_2| = r_1 r_2, \quad \text{arg}(z_1 \cdot z_2) = \text{arg}(z_1) + \text{arg}(z_2), $$

$$|z^{-1}| = |z|^{-1} = r^{-1}, \quad \text{arg}(z^{-1}) = -\text{arg}(z) $$

where $z_1, z_2 \neq 0$. By induction we get:

$$ |z^n| = |z|^n, \quad \text{arg}(z^n) = n\text{arg}(z), \quad \forall n \in \mathbb{Z}. $$
```

# Polar form

```{index} Polar form of complex numbers
```

The property $ \text{arg}(z_1 \cdot z_2) = \text{arg}(z_1) + \text{arg}(z_2) $ might remind us of logarithms, where $\log (a \cdot b) = \log a + \log b$. This is not a coincidence! 

The exponential function, which we will look at in the next chapter, allows us to write complex numbers in a *polar form*:

$$ z = r e^{i \varphi} $$

```{margin} [Euler's identity](https://en.wikipedia.org/wiki/Euler%27s_identity)
For a special angle $\varphi = \pi$ the Euler formula gives the Euler's identity:

$$ e^{i \pi} + 1 = 0 $$

It is considered to be one of the most beautiful equations in mathematics.
```

where we have used the **Euler's formula**:

$$ e^{i \varphi} = \cos(\varphi) + i \sin (\varphi). $$

In this representation, certain operations become much easier. For example,

$$ z_1 \cdot z_2 = r_1 r_2 e^{i(\varphi_1 + \varphi_2)}, \quad z^n = r^n e^{in \varphi} $$

```{index} De Moivre's formula
```

for all powers $n \in \mathbb{N}$. If we write this using a complex number with unit modulus we recover **de Moivre's formula**:

$$ (\cos \varphi + i \sin \varphi)^n = (e^{i \varphi})^n = e^{in \varphi} = \cos (n \varphi) + i \sin (n \varphi). $$

```{tip}
Trigonometric identities are also much easier to be recovered this way. For example, let us think about angle addition.

$$ e^{i(\theta + \varphi)} = e^{i \theta} e^{i \varphi} $$

We Apply Euler's formula to each complex number.

$$\begin{align}
\cos (\theta + \varphi) + i \sin(\theta + \varphi) 
& = (\cos \theta + i \sin \theta)(\cos \varphi + i \sin \varphi) \\
& = \cos \theta \cos \varphi + i \cos \theta \sin \varphi + i \sin \theta \cos \varphi + i^2 \sin \theta \sin \varphi \\
& = (\cos \theta \cos \varphi - \sin \theta \sin \varphi) + i(\cos \theta \sin \varphi + \sin \theta \cos \varphi) \end{align} $$

Equate real and imaginary parts on both sides:

$$\cos (\theta + \varphi) = \cos \theta \cos \varphi - \sin \theta \sin \varphi \\
\sin (\theta + \varphi ) = \cos \theta \sin \varphi + \sin \theta \cos \varphi $$

The reader is encouraged to try to recover other trigonometric identities this way.
```

