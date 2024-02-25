from timeit import default_timer
from constraint import Problem

#instance = [[0,0,0,0,9,4,0,3,0],
#           [0,0,0,5,1,0,0,0,7],
#           [0,8,9,0,0,0,0,4,0],
#           [0,0,0,0,0,0,2,0,8],
#           [0,6,0,2,0,1,0,5,0],
#           [1,0,2,0,0,0,0,0,0],
#          [0,7,0,0,0,0,5,2,0],
#          [9,0,0,0,6,5,0,0,0],
#          [0,4,0,9,7,0,0,0,0]]

def solve_sudoku_csp(instance):
    problem = Problem()
    
    # Define variables
    for i in range(9):
        for j in range(9):
            if instance[i][j] == 0:
                problem.addVariable((i, j), range(1, 10))
            else:
                problem.addVariable((i, j), [instance[i][j]])
    
    # Define constraints
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9):
                problem.addConstraint(lambda x, y: x != y, [(i, j), (i, k)])
                problem.addConstraint(lambda x, y: x != y, [(j, i), (k, i)])
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(3):
                for l in range(3):
                    for m in range(k+1, 3):
                        for n in range(3):
                            problem.addConstraint(lambda x, y: x != y, [(i+k, j+l), (i+m, j+n)])
    
    # Solve CSP
    solution = problem.getSolution()
    if solution:
        result = [[solution[(i, j)] for j in range(9)] for i in range(9)]
        return result
    else:
        return None

#start = default_timer()
solved_instance = solve_sudoku_csp(instance)
#execution = default_timer() - start

if solved_instance:
   # print("Solution trouvée :")
   # for row in solved_instance:
   #     print(" ".join(map(str, row)))
        r=instance
else:
    print("Aucune solution Trouvée")

#print("Le temps de résolution est de : ", execution, " secondes en tant que valeur flottante")
