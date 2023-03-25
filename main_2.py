import os
import sys
os.environ['PATH'] += ';' + '\\'.join(sys.argv[0].split('\\')[:-1])
print(os.environ['PATH'])

from pulp import LpVariable, LpProblem, LpMinimize

def main_2():
    x, y = LpVariable('x'), LpVariable('y')
    model = LpProblem('MyProblem', LpMinimize)
    
    model += x + y

    model += y >= 1
    model += y <= 2*x + 10
    model += y <= -2*x + 10

    model.solve()

    print(x.value(), y.value())

if __name__ == '__main__':
    main_2()