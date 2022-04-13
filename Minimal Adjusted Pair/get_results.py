# William Ard
# CSC 4512 - Optimization
# Project 2

from project2 import get_optimum
import numpy as np


A = [2, 0.2, 3, 8, 1, 2, 0.2, 4]
B = [-2, 7, 1/3, 2, 2, 4, 6, 0.2]



print('\n\nResults using the L1 norm of x as optimization function:')
result_table = []

for i in range(len(A)):

    x1, x2 = get_optimum(A[i], B[i], 'L1')

    print('\n\nMinimal Adjustment for Pair [', A[i], ',', B[i], ']:')
    print('[x1, x2] = [%1.5f, %1.5f]' % (x1, x2))
    print('[A+x1, B+x1] = [%1.5f, %1.5f]' % (A[i]+x1, B[i]+x2))

    result_table.append([A[i], B[i], x1, x2, A[i]+x1, B[i]+x2])

# Saving the output to a csv file to view later
result_table = np.asarray(result_table)
np.savetxt('L1norm.csv', result_table, delimiter=' , ', header='A, B, x1, x2, A+x1, B+x2',
           fmt=['%1.5f', '%1.5f', '%1.5f', '%1.5f', '%1.5f', '%1.5f'], comments='')



print('\n\nResults using the L2 norm of x as optimization function:')
result_table = []

for i in range(len(A)):

    x1, x2 = get_optimum(A[i], B[i], 'L2')

    print('\n\nMinimal Adjustment for Pair [', A[i], ',', B[i], ']:')
    print('[x1, x2] = [%1.5f, %1.5f]' % (x1, x2))
    print('[A+x1, B+x1] = [%1.5f, %1.5f]' % (A[i]+x1, B[i]+x2))
    result_table.append([A[i], B[i], x1, x2, A[i]+x1, B[i]+x2])

# Saving the output to a csv file to view later
result_table = np.asarray(result_table)
np.savetxt('L2norm.csv', result_table, delimiter=' , ', header='A, B, x1, x2, A+x1, B+x2',
           fmt=['%1.5f', '%1.5f', '%1.5f', '%1.5f', '%1.5f', '%1.5f'], comments='')

