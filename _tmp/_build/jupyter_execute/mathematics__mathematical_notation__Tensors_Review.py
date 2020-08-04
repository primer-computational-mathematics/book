# Review of tensors

We present here an overview of tensors and tensor notations (also called suffix or index notation).

**Definition.** (from Wolfram) An nth-rank tensor in m-dimensional space is a mathematical object that has n indices and $m^n$ components and obeys certain transformation rules.

In three-dimensional space, i.e. $m=3$, we can recover some familiar objects:

\\( \quad \quad n = 0\\): **scalar** $a$, a 0th order tensor with no intrinsic direction - e.g. temperature

\\( \quad \quad n = 1\\): **vector** $a_i$, a 1st order tensor that has a magnitude and direction at each point in space - e.g. acceleration

\\( \quad \quad n = 2\\): **2nd order tensor** (dyad) $a_{ij}$, describes the relationship between other algebraic objects related to vector fields - e.g. stress tensor

Later we will introduce a special rank-3 tensor (triad), the Levi-Civita symbol $\varepsilon_{ijk}$ which therefore has three indices, $i, j, k$.

## Stress tensor

To introduce the stress tensor, let us assume there is a point P in space where we want to evaluate the stress. We then draw an arbitrarily oriented surface $S$ with area $\Delta S$ around P, with the orientation of the surface being uniquely defined by the unit normal vector $\mathbf{n} = (n_x, n_y, n_z)$. Instead of dealing with the force $\mathbf{F}$ acting on the surface, we will be dealing with its density, or the *stress*. That is, the stress is a vector quantity defined by the limit

$$ \mathbf{T}_n = \lim_{\Delta S \to 0} \frac{\mathbf{F}_n}{\Delta S},$$

where the limit $\Delta S \to 0$ means that the surface $S$ shrinks to point M, the point where we want to evaluate the stress. Note that the stress vector $\mathbf{T}_n$ (often called traction vector, hence $T$) depends on the orientation of the surface (and the position of the point P, of course). This is indicated by the suffix $n$. 

Let us now place the origin of our coordinate system into point P and draw a surface $S_x$ around P, such that the surface is normal to the x-axis, like in the figure below. Appropriately, we denote the stress on $S_x$ by $\mathbf{T}_x$.

<img src="../notebooks/images/tensor_surface_element.png" width=400\>

As shown in the figure above, the stress $\mathbf{T}_x$ may be represented in coordinate decomposition form:

$$ \mathbf{T}_x = \sigma_{xx}\mathbf{i} + \sigma_{xy}\mathbf{j} + \sigma_{xz}\mathbf{k}. $$

Similarly, we can draw surfaces $S_y$ and $S_z$ and corresponding stresses $\mathbf{T}_y$ and $\mathbf{T}_z$, whose coordinate decompositions are:

$$ \mathbf{T}_y = \sigma_{yx}\mathbf{i} + \sigma_{yy}\mathbf{j} + \sigma_{yz}\mathbf{k} \\
   \mathbf{T}_z = \sigma_{zx}\mathbf{i} + \sigma_{zy}\mathbf{j} + \sigma_{zz}\mathbf{k}. $$

Together, these nine components of the stress vectors form the stress tensor $\mathbf{\sigma}$

$$ \bar{\bar{\sigma}} = \begin{pmatrix}
\sigma_{xx} & \sigma_{xy} & \sigma_{xz} \\
\sigma_{yx} & \sigma_{yy} & \sigma_{yz} \\
\sigma_{zx} & \sigma_{zy} & \sigma_{zz}
\end{pmatrix}. $$

Going back to the above figure, we see that $\sigma_{xx}$ acts normal to the surface $S_x$, while components $\sigma_{xy}$ and $\sigma_{xz}$ are parallel to $S_x$. We can make similar observations about the y- and z- components of the stress vector, where $\sigma_{yy}$ and $\sigma_{zz}$ will be the normal stress components. Therefore, we call the diagonal elements of the stress tensor the *normal stresses* and the off-diagonal elements the *tangential* or *shear stresses*. Often tangential stresses are denoted by $\tau$, e.g. $\tau_{xy}$.

We will now state without proof that the stress vector $\mathbf{T}_n$ acting on an arbitrary surface can be easily found if we know the stress tensor. This relation is:

$$ \mathbf{T}_n = \mathbf{n} \bar{\bar{\sigma}}, $$

or after the multiplication:

$$ \mathbf{T}_n = n_x \mathbf{T}_x + n_y \mathbf{T}_y + n_z \mathbf{T}_z. $$

## Tensor indices

We will most often work in three dimensions, where we can choose an orthonormal coordinate system $(\hat{e}_1, \hat{e}_2, \hat{e}_3)$ to describe any vector *v* by its three coordinates

$$ \mathbf{v} = (v_1, v_2, v_3) = v_1\mathbf{\hat{e}}_1 + v_2 \mathbf{\hat{e}}_2 + v_3 \mathbf{\hat{e}}_3 = \sum_{i=1}^3 v_i \mathbf{\hat{e}}_i, $$

where $i$ is a *dummy* index and is allowed to take values 1, 2 and 3. We can therefore represent the vector $\mathbf{v}$ as $v_i$. Similarly, we can represent three-dimensional space by the Cartesian coordinates $(x_1, x_2, x_3)$, where $\mathbf{x}$, or equivalently $x_i$, is a general position vector. In this notation $x_1$ corresponds to $x$, $x_2$ to $y$ and $x_3$ to $z$.The gradient $\nabla$ can therefore be written in tensor notation as $\frac{\partial}{\partial x_i}$, or sometimes even more compactly as $\partial_i$.

It is convenient to introduce the Einstein summation convention here. If a dummy index is repeated twice, it is implicitly understood that this represents a sum over all possible values of that index. A dummy index cannot appear more than two times in one additive term. Therefore we can simply remove the summation symbol

$$ \sum_{i=1}^3 v_i \mathbf{\hat{e}}_i = v_i \mathbf{\hat{e}}_i. $$

**Side note:** For completeness, we note that the Einstein summation convention states that the sum over an index should only be performed if that index appears once up and once down, i.e. $v_i \hat{e}^i$. However, this notation is often abused when dealing with flat Cartesian space to avoid confusing the up-index for the power (e.g. $v^2$ is not a square of $v$). We can forgive ourselves for this (incorrect) application of the sum convention since raising and lowering an index in flat space in Cartesian coordinates is achieved as follows:

$$v^i \equiv \delta^{ij}v_j, \quad \quad v_i \equiv \delta_{ij}v^j,$$

where $\delta_{ij}$ is the Kronecker delta and $\delta^{ij}$ is its inverse. We will see below that this is a trivial operation and that $v_i = v^i$, as Kronecker delta functions similarly to the identity matrix and its inverse is also trivially related to it.


### Tensor operations

In order to be able to perform operations on tensors that we are probably more used to in matrix notation, it is necessary to introduce two special tensors: the Kronecker delta $\delta_{ij}$ and the Levi-Civita symbol $\varepsilon_{ijk}$.

Kronecker delta is a function of two variables which has a value of 1 if the two variables are the same, or 0 if they are not.

\\( \delta_{ij} = \left\{
    \begin{array}\\
        1 & \mbox{($i = j$)} \\ 
        0 & \mbox{($i \neq j$)} 
    \end{array}
\right.\\)

The values can be arranged into a 2x2 matrix, which will be identical to the identity matrix. Kronecker delta can be also expressed as $\delta_{ij}=\mathbf{\hat{e}}_i\cdot\mathbf{\hat{e}}_j$.

The three-dimensional fully antisymmetric Levi-Civita symbol $\varepsilon_{ijk}$ is defined by:

$$\varepsilon_{ijk} = \left\{
    \begin{array}\\
        +1 & \mbox{if (ijk) = (123), (231), (312)} \\ %\ x \in \mathbf{N}^* \\
        -1 & \mbox{if (ijk) = (132), (231), (321)} \\ %\ x = 0 \\
         0 & \mbox{otherwise (i.e. any 2 are equal)}
    \end{array}
\right. $$

That is, it is 1 if (ijk) is an even permutation of (123), -1 if (ijk) is an odd permutation of 123 and 0 if any index (ijk) is repeated. For example:

$$ \varepsilon_{ijk} = - \varepsilon_{ikj} = - \varepsilon_{jik} = \varepsilon_{kij}.$$

**Cross product** $\boldsymbol{c}$ of two vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ in tensor notation can be expressed as:

$$ c_k \mathbf{\hat{e}}_k=\mathbf{c} = \mathbf{a}\times\mathbf{b} = (a_i\mathbf{\hat{e}}_i)\times (b_j\mathbf{\hat{e}}_j)=a_ib_j(\mathbf{\hat{e}}_i\times\mathbf{\hat{e}}_j)\parallel\cdot \mathbf{\hat{e}}_k,\\
c_k \mathbf{\hat{e}}_k\cdot\mathbf{\hat{e}}_k=c_k=a_i b_j (\mathbf{\hat{e}}_i\times\mathbf{\hat{e}}_j)\cdot\mathbf{\hat{e}}_k$$.

The Levi-Civita symbol is then equal to $\varepsilon_{ijk} = (\mathbf{\hat{e}}_i\times\mathbf{\hat{e}}_j)\cdot\mathbf{\hat{e}}_k$ and in general, cross product can be expressed in tensor notation as:

$$ (\boldsymbol{a} \times \boldsymbol{b} )_i = \varepsilon_{ijk} a_j b_k, $$

where j and k are dummy indices, while i is a *free* index as it only appears once in the term, i.e. it is not summed over. As per the definition of tensors, the number of free indices in a term denotes the rank of that term - in this case there is only one free index so the resulting object is a rank-1 tensor, i.e. a vector.


The **inner product** was already shown to be simply

$$ \mathbf{a} \cdot \mathbf{b} = a_i b_i = b_i a_i. $$

If A is an $n \times n$ matrix, then $A_{ij} = (A^T)_{ji}$, where $A^T$ is the **transpose** of A. If A is symmetric then $A_{ij} = A_{ji}$.

### Examples

For demonstration purposes let us express some common vector identities in tensor notation:

$$ \mbox{Curl of a vector:} \quad \quad \mathbf{a} = \nabla \times \mathbf{b} \quad or \quad a_i = \varepsilon_{ijk} \frac{\partial b_k}{\partial x_j} $$

$$ \mbox{Dot product rule:} \quad \quad \nabla \cdot (\phi \mathbf{a}) = \phi \nabla \cdot \mathbf{a} + \nabla \phi \cdot \mathbf{a} \quad \mbox{or} \quad \frac{\partial}{\partial x_i}(\phi a_i) = \phi \frac{\partial a_i}{\partial x_i} + \frac{\partial \phi}{\partial x_i}a_i$$

$$ \mbox{Triple vector product:} \quad \quad \mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c} \quad \mbox{or} \quad \varepsilon_{ijk}a_k(\varepsilon_{klm}b_lc_m) = (a_jc_j)b_i - (a_jb_j)c_i $$

Here we note that each component of \\(\varepsilon_{ijk}a_k(\varepsilon_{klm}b_lc_m) \\) when written in index notation is just a number, as it points to one of its elements - i.e. $a_k$ is the kth element of $\mathbf{a}$. This means that we can commute them. The LHS can then be written, for example, as \\( \varepsilon_{ijk}\varepsilon_{klm}a_kb_lc_m \\), or in any other order we want. This is one of the advantages of tensor notation, as we **cannot** do this in matrix notation!

$$ \mbox{Determinant in 2D:} \quad \quad \text{det}M = \varepsilon_{ij}m_{1i}m_{2j} $$

The two-dimensional Levi-Civita symbol $\varepsilon_{ij}$ is still an anti-symmetric tensor defined as:

$$ \varepsilon_{ij} = \begin{pmatrix}
0 & 1 \\
-1 & 0
\end{pmatrix} $$

Let us check explicitly that this is indeed correct.

$$ \varepsilon_{ij}m_{1i}m_{2j} = \sum_{i=1}^2 \sum_{j=1}^2 \varepsilon_{ij}m_{1i}m_{2j} \\
    = \varepsilon_{11}m_{11}m_{21} + \varepsilon_{12}m_{11}m_{22} + \varepsilon_{21}m_{12}m_{21} + \varepsilon_{22}m_{12}m_{22} \\
    = m_{11}m_{22} - m_{12}m_{21}$$
    
which is indeed correct.

$$ \mbox{Determinant in 3D:} \quad \quad \text{det}M = \varepsilon_{ijk}m_{1i}m_{2j}m_{3k} $$


