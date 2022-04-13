import numpy as np


def lp_solver(constraints_lhs, constraints_rhs, z):

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

    all_points = []

    # Verify that there are constraints in x1 and x2 (that this is a 2-D optimization problem)
    if not np.all(constraints_lhs[:, 0]) and not np.all(constraints_lhs[:, 1]):

        # Iterating over all possible intersections
        for i in range(len(constraints_rhs)-1):
            for j in range(i+1, len(constraints_rhs)):

                # Set up two constraints into the form Ax=B
                A = np.vstack((constraints_lhs[i], constraints_lhs[j]))
                B = np.vstack((constraints_rhs[i], constraints_rhs[j]))

                # Verify that an intersection exists for the two constraints by evaluating the determinant
                if np.linalg.det(A) != 0:

                    # Solve for the intersection
                    temp_soln = np.transpose(np.linalg.solve(A,B)) # Similar to A^-1 * B. Could also use Cramer's Rule.

                    # Evaluate the constraint equations at the intersection
                    evaluated_constraints = (constraints_lhs*temp_soln)[:, 0] + (constraints_lhs*temp_soln)[:, 1]

                    # Check if the point is within the feasible region, and evaluate the objective function
                    # This creates a 1x4 numpy array: [x1, x2, z(x1,x2), Feasible?(T/F)]
                    # Each point is appended to a Python list
                    if np.all(evaluated_constraints <= constraints_rhs):
                        all_points.append(np.append(temp_soln, [(temp_soln*z)[0,0]+(temp_soln*z)[0, 1], True]))
                    else:
                        all_points.append(np.append(temp_soln, [(temp_soln*z)[0,0]+(temp_soln*z)[0, 1], False]))

        # Convert the list to a single array
        all_points = np.asarray(all_points)

        # Pull out the points that are within the feasible region
        valid_intersections = all_points[np.where(all_points[:,3]==1)][:,0:3]

        # Check to see if there are feasible solutions
        if valid_intersections.size == 0:
            print('No Feasible Solutions')
            soln = [[], [], all_points]
        else:
            # Find the index that refers to the point where z is maximum
            index = np.argmax(valid_intersections[:, 2])

            # This will be the final returned list (see the docstring at the top for explanation of this line)
            soln = [valid_intersections[index][0:2], valid_intersections[index][2], all_points]

    # This is for the 1-Dimensional Case
    else:
        print('1-Dimensional Case!')

        # If all x2 constraints == 0
        if np.all(constraints_lhs[:, 0]):

            # The potential solutions are located at the constraints, solving for the intersections:
            simplified_constraints = constraints_rhs / constraints_lhs[:, 0]

            # Building the same array used in the 2-D case ([x1, x2, z(x1,x2), Feasible?(True/False)]
            all_points = np.transpose(np.array(
                [simplified_constraints, np.zeros(len(constraints_rhs)), simplified_constraints * z[0],
                 np.zeros(len(constraints_rhs))]))

            # The feasible solution will be at the maximum value of the constraints
            index = np.argmax(simplified_constraints)

            # Marking the solution as feasible in the array containing all possible points
            all_points[index, 3] = 1

        # If all x1 constraints == 0
        else:

            # Same logic as above
            simplified_constraints = constraints_rhs / constraints_lhs[:, 1]
            all_points = np.transpose(np.array(
                [np.zeros(len(constraints_rhs)), simplified_constraints, simplified_constraints * z[1],
                 np.zeros(len(constraints_rhs))]))
            index = np.argmax(simplified_constraints)
            all_points[index, 3] = 1

        # This will be the final returned list (see the docstring at the top for explanation of this line)
        soln = [all_points[index][0:2], all_points[index][2], all_points]

    # Sorting the list of all intersections by feasibility and z value
    soln[2] = soln[2][np.lexsort((soln[2][:, 2], soln[2][:, 3]))][::-1]

    # Changing any -0's to 0
    # (IEEE754 floats can have negative zero, but for cleanliness of output they are removed here)
    soln[2][(np.where(soln[2] == -0))] = 0


    print('Optimum Value:', soln[1])
    print('At [x1, x2] =', soln[0])
    print('Table of Results: ')
    print('   x1          x2         z(x1,x2)     Feasible?')
    print(soln[2])

    return soln

