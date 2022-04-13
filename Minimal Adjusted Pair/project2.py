# William Ard
# CSC 4512 - Optimization
# Project 2


def get_optimum(A, B, optimization_function_type: str):
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

    # Initialize dictionary for storing results
    result = dict()

    # Call the solver, solving the problem in terms of x1
    x1_case1, x2_case1, z_current_case1 = solver(A, B, optimization_function_type)
    result[z_current_case1] = [x1_case1, x2_case1]
    # print(x1_case1, x2_case1, z_current_case1)

    # Call the solver, solving the problem in terms of x2
    x2_case2, x1_case2, z_current_case2 = solver(B, A, optimization_function_type)
    result[z_current_case2] = [x1_case2, x2_case2]
    # print(x1_case2, x2_case2, z_current_case2)

    # Return the minimum value
    final_result = result[min(result)]

    # print('Optimum Point at [x1, x2] = %1.5f, %1.5f' % (final_result[1][0], final_result[1][1]))

    return final_result[0], final_result[1]


def solver(A, B, optimization_function_type: str):
    """
    Internal function used to find the minimal adjustment (x1, x2)

    :param A: float or int, First point in ordered pair
    :param B: float or int, Second point in ordered pair
    :param optimization_function_type: string, Specify optimization function as either 'L1' or 'L2'
    :return: [x1, x2, z(x1, x2)] where:
             x1: adjustment value for A,
             x2: adjustment value for B,
              z: cost function at the adjustment value for x1 and x2
    """

    if optimization_function_type == 'L1':

        def z(x1, x2):
            """Function to be minimized"""
            # Using the L1 norm as the objective function
            return abs(x1) + abs(x2)

    if optimization_function_type == 'L2':

        def z(x1, x2):
            """Function to be minimized"""
            # Using the L2 norm as the objective function
            return (x1**2+x2**2)**0.5

    def x2(x1):
        """
        Expressing x2 as a function of x1
        Taken from the constraint: (A+x1)*(B+x2)=1
        """
        return 1/(A+x1)-B

    # Start position for optimization search
    x1 = A

    # Increment for search, can adjust this for higher accuracy at the expense of computation time.
    delta = 0.00001

    # Initializing variables
    delta_z = 1     # Change in the objective function
    i = 0           # Iteration counter

    # Solver History
    x1_data = [x1]
    x2_data = [x2(x1)]
    z_data = [z(x1, x2(x1))]
    dz_data = [0.]

    # Objective function value at starting position
    z_current = z(x1, x2(x1))

    # Evaluate objective function along constraint in both directions
    z_plus = z(x1 + delta, x2(x1 + delta))
    z_minus = z(x1 - delta, x2(x1 - delta))

    # Determine direction to move to minimize objective function
    if z_plus < z_minus:
        delta = delta
    else:
        delta = -delta

    # Move along constraint, evaluating objective function until it reaches minimum.
    # The minimum will be when delta_z is no longer positive. In other words, when the
    # objective function begins to increase again.
    while delta_z > 0 and i < 1e10:

        z_current = z(x1, x2(x1))

        z_new = z(x1 + delta, x2(x1 + delta))

        delta_z = z_current - z_new

        # Increment x1
        x1 = x1 + delta

        # Solver History
        x1_data.append(x1)
        x2_data.append(x2(x1))
        z_data.append(z_current)
        dz_data.append(delta_z)

        # Iteration count
        i = i + 1

    return x1_data[-2], x2_data[-2], z_current