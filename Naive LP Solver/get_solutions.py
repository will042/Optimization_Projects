import numpy as np
from lp_solver_function import lp_solver

#%% Problem 1
# Constraints and optimization function are defined here.

constraints_lhs = np.array([[6, 4],
                            [1, 2],
                            [-1, 1],
                            [0, 1],
                            [-1, 0],
                            [0, -1]])
constraints_rhs = np.transpose(np.array([24, 6, 1, 2, 0, 0]))
z = np.array([5, 6])
print('\nProblem 1')
soln = lp_solver(constraints_lhs, constraints_rhs, z)
np.savetxt('Problem 1.csv', soln[2], delimiter=' , ', header='x1, x2, z(x1 x2), Feasible',
           fmt=['%.2f', '%.2f', '%.2f', '%2.i'], comments='')

#%% Problem 2
# Constraints and optimization function are defined here.

constraints_lhs = np.array([[6, 4],
                            [1, 2],
                            [-1, 1],
                            [0, 1],
                            [-1, 0],
                            [0, -1]])
constraints_rhs = np.transpose(np.array([24, 6, 1, 2, 0, 0]))
z = np.array([8, 10])
print('\nProblem 2')
soln = lp_solver(constraints_lhs, constraints_rhs, z)
np.savetxt('Problem 2.csv', soln[2], delimiter=' , ', header='x1, x2, z(x1 x2), Feasible',
           fmt=['%.2f', '%.2f', '%.2f', '%2.i'], comments='')

#%% Problem 3
# Constraints and optimization function are defined here.

constraints_lhs = np.array([[6, 4],
                            [1, 2],
                            [-1, 1],
                            [-1, 0],
                            [0, 1],
                            [-1, 0],
                            [0, -1]])
constraints_rhs = np.transpose(np.array([24, 6, 1, -5, 2, 0, 0]))
z = np.array([5, 6])
print('\nProblem 3')
soln = lp_solver(constraints_lhs, constraints_rhs, z)
np.savetxt('Problem 3.csv', soln[2], delimiter=' , ', header='x1, x2, z(x1 x2), Feasible',
           fmt=['%.2f', '%.2f', '%.2f', '%2.i'], comments='')

#%% Problem 4
# Constraints and optimization function are defined here.

constraints_lhs = np.array([[3, 2],
                            [2, 4],
                            [-1, 1],
                            [0, 2],
                            [-1, 0],
                            [0, -1]])
constraints_rhs = np.transpose(np.array([12, 12, 1, 4, 0, 0]))
z = np.array([10, 18])
print('\nProblem 4')
soln = lp_solver(constraints_lhs, constraints_rhs, z)
np.savetxt('Problem 4.csv', soln[2], delimiter=' , ', header='x1, x2, z(x1 x2), Feasible',
           fmt=['%.2f', '%.2f', '%.2f', '%2.i'], comments='')

#%% Problem 5
# Constraints and optimization function are defined here.
# Converted constraints to maximization problem to allow for solver function to work.

constraints_lhs = np.array([[-5, 0],
                            [-2, 0],
                            [-6, 0],
                            [-3, 0],
                            [-1, 0]])
constraints_rhs = np.transpose(np.array([-20, -30, -6, -24, 0]))
z = np.array([6, 0])
print('\nProblem 5')
soln = lp_solver(constraints_lhs, constraints_rhs, z)
np.savetxt('Problem 5.csv', soln[2], delimiter=' , ', header='x1, x2, z(x1 x2), Feasible',
           fmt=['%.2f', '%.2f', '%.2f', '%2.i'], comments='')

#%% Problem 6
# Constraints and optimization function are defined here.

constraints_lhs = np.array([[1, 5],
                            [-1, 0],
                            [-1, 0],
                            [0, -1]])
constraints_rhs = np.transpose(np.array([20, -2, 0, 0]))
z = np.array([3, 4])
print('\nProblem 6')
soln = lp_solver(constraints_lhs, constraints_rhs, z)
np.savetxt('Problem 6.csv', soln[2], delimiter=' , ', header='x1, x2, z(x1 x2), Feasible',
           fmt=['%.2f', '%.2f', '%.2f', '%2.i'], comments='')

#%% Problem 7
# Constraints and optimization function are defined here.

constraints_lhs = np.array([[5, 0],
                            [-1, 0]])
constraints_rhs = np.transpose(np.array([20, 0]))
z = np.array([6, 0])
print('\nProblem 7')
soln = lp_solver(constraints_lhs, constraints_rhs, z)
np.savetxt('Problem 7.csv', soln[2], delimiter=' , ', header='x1, x2, z(x1 x2), Feasible',
           fmt=['%.2f', '%.2f', '%.2f', '%2.i'], comments='')