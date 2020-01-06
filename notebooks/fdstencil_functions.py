# Converted from fdstencil.ipynb and then edited

# coding: utf-8

# # Computing finite difference stencils
# 
# [AMath 585, Winter Quarter 2020](http://staff.washington.edu/rjl/classes/am585w2020/) at the University of Washington. Developed by R.J. LeVeque and distributed under the [BSD license](https://github.com/rjleveque/amath585w2020/blob/master/LICENSE).  You are free to modify and use as you please, with attribution.
# 
# These notebooks are all [available on Github](https://github.com/rjleveque/amath585w2020/).

# This notebook illustrates how finite difference coefficients can be determined for approximating the $k$th derivative of a function at some point $\bar x$, based on function values at $n$ nearby points, with $n > k$.  If the points have uniform spacing $\Delta x$, then the order of accuracy will be ${\cal O}\left((\Delta x)^{n-k}\right)$ in general, but the points need not be equally spaced.
# 
# The general idea is to determine the interpolating polynomial of degree $n-1$ and compute the $k$th derivative of this at the specified point.
# 



# In[2]:


from pylab import *
from scipy.special import factorial


# ## Vandermonde matrix solution
# 
# The simplest way to determine the coefficients is to derive an $n \times n$ linear system of equations involving a Vandermonde matrix, as described in Section 1.5 of [[FDM-book]](http://faculty.washington.edu/rjl/fdmbook/), and implemented there as a simple Matlab code (also available as `fdcoeffV.m` from the book website).  Here is the Python equivalent:

# In[3]:


def fdcoeffV(k,xbar,x):
    x = array(x)  # in case a list or tuple passed in, convert to numpy array
    n = len(x)
    if k >=n:
        raise ValueError('*** len(x) must be larger than k')
        
    A = ones((n,n))
    xrow = x - xbar  # displacement vector
    
    for i in range(1,n):
        A[i,:] = (xrow**i) / factorial(i)
      
    condA = cond(A)  # condition number
    if condA > 1e8:
        print("Warning: condition number of Vandermonde matrix is approximately %.1e" % condA)
        
    b = zeros(x.shape)
    b[k] = 1.
    
    c = solve(A,b)
    
    return c

# ## Printing the stencil
# 
# If you want to compute the weights in general, we can choose $\Delta x = 1$ and then no
# te that any second-derivative difference approximation will have $\Delta x^2$ in the denominator.  In the function below this is made more general, to work for any order $k$ derivative, but assuming equally spaced points.  

# In[5]:


def fdstencil(k, jbar, stencil_points):
    """
    Compute and print the finite difference stencil for an order k derivative
    using at least k+1 equally spaced points.
    The stencil_points are thus assumed to be integers (indices of stencil points)
    as is jbar, the index at which the approximation is to be used.
    
    For example, the standard second order stencil for u''(x_0) 
    can be printed via
        fdstencil(2, 0, [-1,0,1])
    """
    assert type(jbar) is int, '*** jbar should be an integer'
    stencil_pts = array(stencil_points)
    assert stencil_pts.dtype == int, '*** stencil_points should be integers'
    
    c = fdcoeffV(k, jbar, stencil_pts)
    
    print("Stencil for approximation to order %s derivative at U_{%s} is:"           % (str(k), str(jbar)))
    coeffs = ['%s / h^2' % str(cj) for cj in c]
    s = '[' 
    for j in range(len(c)):
        subj = str(stencil_pts[j])
        cj = c[j]
        sj = '%g U_{%s}' % (abs(cj), stencil_pts[j])
        if cj >= 0:
            s = s + ' + ' + sj
        else:
            s = s + ' - ' + sj
    s = s + '] / h^%i' % k
    print(s)
    return c




# ## Fornberg's method
# 


# A more stable approach was introduced by B. Fornberg in 
# - Generation of Finite Difference Formulas on Arbitrarily Spaced Grids, *Mathematics of Computation* 51(1988) pp. 699-706, [doi:10.1090/S0025-5718-1988-0935077-0](https://doi.org/10.1090/S0025-5718-1988-0935077-0)
# 
# and explained in these classroom notes,
# - Calculation of weights in finite difference formulas, *SIAM Review* 40 (1998), pp. 685-691, [doi:10.1137/S0036144596322507](https://doi.org/10.1137/S0036144596322507)
# 
# This approach is implemented in Matlab in the file `fdcoeffF.m` available from the website [[FDM-book]](http://faculty.washington.edu/rjl/fdmbook/).
# 
# A Python version is below.  This is based directly on the Fortran code in the SIAM Review paper listed above (which uses 0-based indexing, like Python, whereas the Matlab code is 1-based).
# 
# **Note:** Forberg's algorithm can be used to simultaneously compute the coefficients for derivatives of order `0, 1, ..., m` where `m <= n-1`. This gives a coefficient matrix `C(1:n,1:m)` whose k'th column gives the coefficients for the k'th derivative.
# 
# In the version below we set `m=k` and only compute the coefficients for derivatives of order up to order k, and then return only the k'th column of the resulting `C` matrix (converted to a row vector).   This routine is then compatible with ` fdcoeffV` defined above.    If the optional argument `fullC` is `True` then the full matrix of coefficients for derivatives of all orders up to `n-1` will be returned.

# In[10]:


def fdcoeffF(k, xbar, x, fullC=False):
    n = len(x) - 1
    if k > n:
        raise ValueError('*** len(x) must be larger than k')
    
    m = k  # for consistency with Fornberg's notation
    c1 = 1.
    c4 = x[0] - xbar
    C = zeros((n+1,m+1))
    C[0,0] = 1.
    for i in range(1,n+1):
        mn = min(i,m)
        c2 = 1.
        c5 = c4
        c4 = x[i] - xbar
        for j in range(i):
            c3 = x[i] - x[j]
            c2 = c2*c3
            if j==i-1:
                for s in range(mn,0,-1):
                    C[i,s] = c1*(s*C[i-1,s-1] - c5*C[i-1,s])/c2
                C[i,0] = -c1*c5*C[i-1,0]/c2
            for s in range(mn,0,-1):
                C[j,s] = (c4*C[j,s] - s*C[j,s-1])/c3
            C[j,0] = c4*C[j,0]/c3
        c1 = c2
    
    if fullC:
        return C
    else:
        c = C[:,-1] # last column of C
        return c


