# Composition and Inverse Functions

## Injection, Surjection, Bijection

```{index} Injection
```

```{index} Surjection
```

```{index} Bijection
```

Before we start talking about inverse functions, let us define some very important terms.

A function $f: A \to B$ is:

1. an **injection** (or *injective* or *one-to-one*) if different elements of the domain are assigned different elements of the codomain, i.e.:

$$ \forall a, a' \in A, (a \neq a') \Rightarrow (f(a) \neq f(a')). $$

We can determine easily whether a function is an injection from its graph. For a function to be injective, any horizontal line must cross its graph in at most one point. This is why the introduced notion of strictly monotonic function is important: if a function is **strictly monotonic** (on some interval or on its entire domain), then it is an injection.

2. a **surjection** (or *surjective* or *onto*) if *every* element of its codomain $B$ is a possible value of $f(a)$ for some $a \in A$. That is, the image of $f$ must be equal to its codomain. That is,

$$ \forall b \in B, \exists a \in A : f(a) = b. $$

3. a **bijection** (or *bijective* or one-to-one and onto or one-to-one correspondence) if it is both an injection and a surjection. That is,

$$ \forall b \in B, \exists ! a \in A: f(a) = b. $$

Let us summarise this in a table (source: [Wikipedia](https://en.wikipedia.org/wiki/Bijection,_injection_and_surjection)):

```{list-table}
:header-rows: 1
:widths: 10 20 20
:align: center

* - 
  - <p align="center"> surjective
  - <p align="center"> non-surjective
* -  **injective**
  - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Bijection.svg/200px-Bijection.svg.png" align="center">  <p align="center"> **bijective**
  - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Injection.svg/200px-Injection.svg.png" align="center">  <p align="center"> **injective-only**
* - **non-injective**
  - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Surjection.svg/200px-Surjection.svg.png" align="center"> <p align="center"> **surjective-only**
  - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Total_function.svg/200px-Total_function.svg.png" align="center"> <p align="center"> **general**
```

## Function composition

```{index} Composition (functions)
```

Let $f: A \to B$ and $g: C \to D$ be two functions. If $f[A] \subseteq C$, we can define a function $h: A \to D$ such that $h(x) = g[f(x)], \forall x \in A$. We denote the function $h$ defined this way by $g \circ f$ and call it the **composition** of $g$ and $f$.

This is generally *not* a commutative operation. For $f: \mathbb{R} \to \mathbb{R}, f(x) = x + 1$ and $g: \mathbb{R} \to \mathbb{R}, g(x) = x^2$:

$$ (g \circ f)(x) = (x+1)^2 \\
(f \circ g)(x) = x^2 + 1 $$

But it is associative. For $f: \mathbb{R} \to \mathbb{R}, f(x) = x + 1, g: \mathbb{R} \to \mathbb{R}, g(x) = \sin(x)$ and $h: \mathbb{R} \to \mathbb{R}, h(x) = \sqrt{x^2}$:

$$ [h \circ (g \circ f)](x) = h[\sin(x + 1)] = \sqrt{\sin^2(x+1)} \\
[(h \circ g) \circ f](x) = \sqrt{ \sin^2[f(x)] } = \sqrt{\sin^2(x+1)} $$

As an example of a function composition that is *not* defined, consider $f: \mathbb{R} \to \mathbb{R}$ where $f(x) = \cos x$ and $g: \mathbb{R} \to \mathbb{R}$ where $g(x) = \sqrt{x}$. The range of $f$ is $[-1, 1]$ but the natural domain of $g$ is $[0, + \infty)$.

## Inverse function

```{index} Inverse (functions)
```

Let $f: A \to B$ be a function and assume there exists another function $g: B \to A$ such that for all $x \in A$ and for all $y \in B$:

$$ g[f(x)] = x \iff f[g(y)] = y. $$

We then call $g$ the **inverse function** of $f$ and we denote it $g = f^{-1}$.

```{admonition} Properties

- A function $f$ is invertible iff it is a bijection

- The inverse function $f^{-1}$ is unique.

- The graph of the inverse function $G(f^{-1})$ is symmetric to the graph $G(f)$ with respect to $y = x$. 

- Monotonic properties of $f$ are preserved on $f^{-1}$
```

