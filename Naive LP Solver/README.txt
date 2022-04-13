File List:

---------------------------------------
lp_solver_function.py
---------------------------------------
Main solver for the project. Usage instructions are included in docstring at top of function, but are repeated here for convenience:

lp_solver(constraints_lhs, constraints_rhs, z)

    """
    This function iterates over the constraints, solving for each intersection, evaluating the objective function
    at each point and checking if each point is within the feasible region.

    :param constraints_lhs: An nx2 numpy array of constraints with each row corresponding to a different constraint.
    The first column is x1, the 2nd column is x2. IMPORTANT: All constraints should be expressed as <= to the right-hand
    side (Example: x1 >= 2 should be expressed as -x1 <= -2)
    :param constraints_rhs: An nx1 numpy array representing the right-hand side of the constraint equations.
    :param z: np.array([C1, C2]) for the objective function: z = C1*x1+C2*x2
    :return: A Python list containing: [np.array([x1, x2]), max_value, np.array(all_points)] where
                [x1, x2] is the optimal point
                max_value is the objective function evaluated at the optimal point
                all_points is a nx4 numpy array: [x1, x2, Z(x1,x2), True/False],
                    giving each intersection (x1, x2),
                    the value of the objective function at that intersection Z(x1,x2),
                    and a check to verify if it is in the feasible region (1/0)
    """


---------------------------------------
get_solutions.py
---------------------------------------
Solves problems 1-7 using lp_solver_function, prints output to terminal, and writes csv files for each problem.


---------------------------------------
plot_tool.py	
---------------------------------------		
Used to generate a plots of constraints, feasible region, and the optimal point (not necessary for project).


---------------------------------------
profiler.py
---------------------------------------
Used to benchmark project code against SciPy's interior point and simplex methods (not necessary for project).