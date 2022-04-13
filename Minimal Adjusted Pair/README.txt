William Ard
CSC 4512 - Optimization
Project 2

File List:

---------------------------------------
project2.py
---------------------------------------
Main solver for the project. Usage instructions are included in docstring at top of function, but are repeated here for convenience:

get_optimum(A, B, optimization_function_type: str):

    """
    Function used to find the minimal adjustment (x1, x2), for A and B such that (A+x1)*(B+x2)==1
    Objective function to be minimized is:
        z = abs(x1) + abs(x2) for 'L1'
        z = (x1**2+x2**2)**0.5 for 'L2'

    NOTE: Since the solver works by varying x1, this may not be globally optimal. It's necessary to also
    solve the problem by varying x2 in terms of x1. The function get_optimum() is used to call the solver,
    evaluate both cases, and return the optimum of the two.

    :param A: float, First point in ordered pair
    :param B: float, Second point in ordered pair
    :param optimization_function_type: string, Specify optimization function as either 'L1' or 'L2'
    :return: Minimal adjustment [x1, x2]
    """


---------------------------------------
get_results.py
---------------------------------------
Solves all test cases using the get_optimum() function, prints output to terminal, and writes csv files for both L1 norm and L2 norm optimization functions. 
Numpy was used for generation of CSV tables.


---------------------------------------
plot_tool.m
---------------------------------------		
MATLAB file used to generate a plots (not necessary for project).

