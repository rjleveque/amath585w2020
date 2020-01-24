from pylab import *

def solve_bvp_nonlinear(epsilon, f, ainfo, binfo, m, u0_func, max_iter=10, 
                        plot_iterates=True, debug=False):
    """
    Solve the 2-point BVP with Dirichlet BCs
    Input:
        epsilon > 0 coefficient of u''
        f is a function defining the right hand side,
        ainfo = (ax, alpha) defines the Dirichlet boundary condition u(ax) = alpha,
        binfo = (bx, beta) defines the Dirichlet boundary condition u(bx) = beta,
        m is the number of (equally spaced) interior grid points to use.
        u0_func = function to evaluation for initial guess
        max_iter = maximum number of iterations of Newton
        plot_iterates: if set to True, plot the approximate solution each iteration
        debug: if set to True, print some things out including the matrix at each
            iteration, so generally use this only for small m.
    
    Returns:
        x = array of grid points (including boundaries, so of length m+2)
        u = array of approximate solution at these points.
    """
    
    from scipy import sparse
    from scipy.sparse.linalg import spsolve
        
    ax, alpha = ainfo
    bx, beta = binfo
    
    h = (bx-ax)/float(m+1)    # h = delta x
    x = linspace(ax,bx,m+2)   # note x[0]=ax, x[m+1]=bx
    if debug: 
        print('+++ h = %g, m+2 = %i' % (h,m+2))
        print('+++ x = ',x)
    
    # convergence tolerances:
    tol_delta = 1e-12
    tol_Gk = 1e-12
    
    # set up m by m matrix A for the u''(x) term, 
    # which is always needed as part of the Jacobian
    A_diag = ones(m+2)
    A_offdiag = ones(m+1)
    A = sparse.diags([A_offdiag, -2*A_diag, A_offdiag], [-1, 0, 1], 
                     shape=(m+2,m+2), format='csc')
    A = epsilon * A / h**2
    
    # modify first and last row for Dirichlet BCs:
    A[0,0] = 1.
    A[0,1] = 0.
    A[m+1,m] = 0.
    A[m+1,m+1] = 1.
    
    # initial guess for Newton iteration:
    Uk = u0_func(x)  # of length m+2
    if debug: print('+++ Initial Uk = ', Uk)
    
    if plot_iterates:
        # make a plot showing how the solution evolves:
        fig = figure(figsize=(8,6))
        ax = axes()
        grid(True)
        title('Approximate solution while iterating')
    
    # Newton iteration:
    for k in range(max_iter):
        
        if plot_iterates:
            plot(x,Uk,label='k = %i' % k)
        
        U = Uk.copy()  # use in slicing below so Uk not changed

        # Jacobian matrix with be A from above plus nonlinear part N:
        
        N_subdiag = -U[1:m+2]
        N_subdiag[m] = 0.
        N_diag = zeros(m+2)
        N_diag[1:m+1] = U[2:m+2] - U[0:m] - 2*h
        N_superdiag = U[0:m+1]
        N_superdiag[0] = 0.
        N = sparse.diags([N_subdiag, N_diag, N_superdiag], [-1, 0, 1], 
                     shape=(m+2,m+2), format='csc')
        N = N / (2*h)
        
        Jk = A + N
        if debug: print('+++ after forming Jk, Uk = ', Uk)
        if debug: print('+++ Jk = \n', Jk.toarray())
        
        # Use Uk below, since U got changed above.
        Gk = zeros(m+2)
        if debug: print('+++ Uk[0] = %g, alpha = %g' % (Uk[0], alpha))
        Gk[0] = Uk[0] - alpha
        Gk[m+1] = Uk[m+1] - beta
        Gk[1:m+1] = epsilon/h**2 * (Uk[0:m] - 2*Uk[1:m+1] + Uk[2:m+2]) \
                    + Uk[1:m+1] * ((Uk[2:m+2] - Uk[0:m])/(2*h) -1.) \
                    - f(x[1:m+1])
        
        # solve linear system:
        if debug: print('+++ Uk = ',Uk)
        if debug: print('+++ Gk = ',Gk)
        delta = spsolve(Jk, Gk)
        Uk = Uk - delta
        if debug: print('+++ delta = ',delta)
        norm_delta = norm(delta, inf)
        norm_Gk = norm(Gk, inf)
        print('Iteration k = %i: norm(Gk) = %.2e, norm(delta) = %.2e' \
               % (k, norm_Gk, norm_delta))
        if (norm_delta < tol_delta) or (norm_Gk < tol_Gk):
            print('Declared convergence after %i iterations' % k)
            break
        if k==(max_iter-1):
            print('Reached max_iter, possible nonconvergence')
    
    if plot_iterates:
        legend()
        
    return x,Uk
