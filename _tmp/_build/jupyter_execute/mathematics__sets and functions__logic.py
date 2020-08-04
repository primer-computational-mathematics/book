# Logic and proof

## Logic symbols

```{index} Logic symbols
```

The origins of logic symbols stem from first attempts at creating a clear language to express logic statements. Everyday languages are not suitable for this as the use of them can easily lead to ambiguities and paradoxes. This is the case in mathematics as well, so general mathematics was influenced by this language and borrowed some of it. The use of logic symbols is more widespread in areas of mathematics where there is a need for a clear language, for example set theory (which is full of paradoxes!).

Here we will list some more common logic symbols. For a full list visit [Wikipedia](https://en.wikipedia.org/wiki/List_of_logic_symbols).

```{list-table} Common logic symbols
:name: logic-symbols
:header-rows: 1
:widths: 10 20 20 25 25
:align: center

* - Symbol
  - Name
  - Read as
  - Example
  - Meaning
* - $\forall$
  - universal quantification
  - for all, for any, for each
  - $\forall x \in \mathbb{R}, x^2 \geq 0$
  - For all real numbers $x$, $x^2$ is greater or equal to $0$
* - $\exists$
  - existential quantification
  - there exists
  - $\forall n \in \mathbb{N}, \exists x \in \mathbb{R} : | n - x | < 1$
  - For all natural numbers $n$ there exists a real number $x$ such that $| n - x| < 1$
* - $\exists !$
  - uniqueness quantification
  - there exists exactly one
  - $A \subseteq \mathbb{N} \implies \exists ! m \in A : m \geq n, \forall n \in A$
  - If $A$ is a subset of $\mathbb{N}$ then there exists a unique $m \in A$ such that $m \geq n$, for all $n \in A$  
* - $\lnot$
  - negation
  - not
  - $\lnot (x = y) \iff (x \neq y)$
  - $x = y$ is not true iff $x \neq y$
* - $\land$
  - conjunction
  - and
  - $((x \leq 1) \land (x \geq 1)) \iff x = 1$
  - $x$ is less or equal than 1 and greater or equal to $1$ iff $x = 1$
* - $\lor$
  - disjunction
  - or
  - $((x \leq 0) \lor (x \geq 0)) \iff x \in \mathbb{R}$
  - $x \leq 0$ or $x \geq 0$ iff $x$ is a real number
* - $\implies$
  - implication
  - implies, if... then
  - $n \in \mathbb{N} \implies n \in \mathbb{Z}$
  - If $n$ is element of $\mathbb{N}$ then it is element of $\mathbb{Z}$
* - $\iff$
  - equivalence
  - if and only if, iff
  - ($x$ is prime) $\land (x\mod 2 = 0) \iff x=2$
  - $x=2$ if and only if $x$ is a prime number and $x \mod 2 = 0$
* - $:$, $|$, s.t.
  - condition
  - such that
  - $\forall x \in \mathbb{R} : x > 0, \sqrt{x} > 0$
  - For all $x$ element of $\mathbb{R}$ such that x is greater than $0$, $\sqrt{x}$ is greater than $0$
  
```

