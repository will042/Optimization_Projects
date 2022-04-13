import numpy as np
from lp_tools import lp_solver
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from sympy import plot_implicit, symbols, Eq, And

#%% Constraints and optimization function are defined here. See docstring in lp_solver_function.py for more information.

constraints_lhs = np.array([[1, 5],
                            [-1, 0],
                            [-1, 0],
                            [0, -1]])
constraints_rhs = np.transpose(np.array([20, -2, -0, -0]))
z = np.array([3, 4])

soln = lp_solver(constraints_lhs, constraints_rhs, z)
#%% Plotting the Feasible Region and the Optimal Point (for fun, you don't need this to run the solver)

# Just to make figure generation a little easier.
# The figure is saved as a .png using this title as well
plot_title = 'Problem 6'

C1, C2, x1, x2 = symbols('C1 C2 x1 x2')

eq = C1*x1 + C2*x2

FR_plot_code = "FR_plot = plot_implicit(And("

for i in range(len(constraints_rhs)):
    FR_plot_code = FR_plot_code + "eq.subs([(C1, constraints_lhs[" + str(i) + ", 0]), " \
            "(C2, constraints_lhs[" + str(i) + ", 1])]) <= constraints_rhs[" + str(i) + "],"

FR_plot_code = FR_plot_code[:-1] + "), backend = 'matplotlib', show=False, xlabel='', " \
                                   "ylabel='',line_color='0.75', x_var = (x1, -5, 20), y_var = (x2, -5, 20), title='" + plot_title + "')"

exec(FR_plot_code)

for i in range(len(constraints_rhs)):
    line_plot_code = ("lp = plot_implicit(Eq(eq.subs([(C1, constraints_lhs[" + str(i) + ", 0]), "
                "(C2, constraints_lhs[" + str(i) + ", 1])]), constraints_rhs[" + str(i) + "]), x_var = (x1, -5, 10), y_var = (x2, -5, 10) "
                ", xlabel='', ylabel='', backend = 'matplotlib', line_color='0.5', show=False)")

    exec(line_plot_code)
    FR_plot.append(lp[0])


# Can plot objective function using this:
# obj_function_plot = plot_implicit(Eq(eq.subs([(C1, z[0]), (C2, z[1])]),1,), x_var = (x1, -5, 10),
# y_var = (x2, -5, 10), xlabel='', ylabel='', backend = 'matplotlib', show=False)
# FR_plot.append(obj_function_plot[0])


## This function from: https://stackoverflow.com/questions/60325325/putting-together-plots-of-matplotlib-and-sympy
def move_sympyplot_to_axes(p, ax):
    backend = p.backend(p)
    backend.ax = ax
    # Fix for > sympy v1.5
    backend._process_series(backend.parent._series, ax, backend.parent)
    backend.ax.spines['right'].set_color('none')
    backend.ax.spines['bottom'].set_position('zero')
    backend.ax.spines['top'].set_color('none')
    plt.close(backend.fig)
## End of code from Stack Overflow


fig, ax = plt.subplots(ncols=1)

move_sympyplot_to_axes(FR_plot, ax)
ax.set_ylabel('$x_2$', loc='top')
ax.set_xlabel('$x_1$', loc='right')

if not np.any(soln[2][:, 3]):
    at = AnchoredText('No Feasible Solution', prop=dict(size=10),
                      frameon=False, loc='upper center')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(at)
else:
    at = AnchoredText('Optimal Value: ' + str(soln[1]) + ' at [x1 x2] = '
                      + str(soln[0]), prop=dict(size=10), frameon=False, loc='upper center')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(at)
    plt.scatter(soln[0][0], soln[0][1], c='r')
plt.xlim(-1,25)
plt.ylim(-1,6)
# plt.tight_layout()
fig.savefig(plot_title, bbox_inches='tight')
plt.show()