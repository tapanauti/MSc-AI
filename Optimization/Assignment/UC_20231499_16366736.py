from ortools.linear_solver import pywraplp, _pywraplp


def solve(solver):
    result = solver.Solve()
    return result


def prt(solver,objt):
    for v in solver.variables():
        print(f"{v.name()} = {v.solution_value():.5}; coefficient {objt.GetCoefficient(v):.5}")
            
    print(f"Optimal objective value = {objt.Value():.5}")

   
        
def main(gnt,dmd):

    solver = pywraplp.Solver('Generator',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    var_list = []

    A = [solver.NumVar(gnt[0][1],gnt[0][2],f'A{i}') for i in range (1,25)]
    B = [solver.NumVar(gnt[1][1],gnt[1][2],f'B{i}') for i in range (1,25)]
    C = [solver.NumVar(gnt[2][1],gnt[2][2],f'C{i}') for i in range (1,25)]
    D = [solver.NumVar(gnt[3][1],gnt[3][2],f'D{i}') for i in range (1,25)]
    E = [solver.NumVar(100,900,'E')]
    F = [solver.NumVar(100,600,'F')]
    G = [solver.NumVar(10,100,'G')]
    H = [solver.NumVar(gnt[7][1],gnt[7][2],f'H{i}') for i in range (1,25)]
    I = [solver.NumVar(0,0,f'I{i}') for i in range (1,7)]
    I.extend([solver.NumVar(0,35,f'I{i}') for i in range (7,12)])
    I.extend([solver.NumVar(0,70,f'I{i}') for i in range (12,17)])
    I.extend([solver.NumVar(0,35,f'I{i}') for i in range (17,20)])
    I.extend([solver.NumVar(0,0,f'I{i}') for i in range (20,25)])
    J = [solver.NumVar(0,0,f'J{i}') for i in range (1,7)]
    J.extend([solver.NumVar(0,10,f'J{i}') for i in range (7,12)])
    J.extend([solver.NumVar(0,20,f'J{i}') for i in range (12,17)])
    J.extend([solver.NumVar(0,10,f'J{i}') for i in range (17,20)])
    J.extend([solver.NumVar(0,0,f'J{i}') for i in range (20,25)])

    var_list.append(A)
    var_list.append(B)
    var_list.append(C)
    var_list.append(D)
    var_list.extend(E)
    var_list.extend(F)
    var_list.extend(G)
    var_list.append(H)
    var_list.append(I)
    var_list.append(J)
    
    for j in range (0,24):
        print(var_list[0][j])
        solver.Add(var_list[0][j] + var_list[1][j] + var_list[2][j] + var_list[3][j] + var_list[4] + var_list[5] + var_list[6] + var_list[7][j] + var_list[8][j] + var_list[9][j]== dmd[j])
           



    objt = solver.Objective()
    for i in range(0,10):
        if(i<4 or i>6):
            for j in range (0,24):
                objt.SetCoefficient(var_list[i][j],gnt[i][3])
    objt.SetCoefficient(var_list[4],gnt[4][3])
    objt.SetCoefficient(var_list[5],gnt[5][3])
    objt.SetCoefficient(var_list[6],gnt[6][3])
    objt.SetMinimization()   
    
    
    result = solve(solver)
    prt(solver,objt)

if __name__ == '__main__':


    gnt = [ ['a',10,100,1.4],
            ['b',10,80,1.4],
            ['c',10,60,1.4],
            ['d',1,10,1.4],
            ['e',100,900,4.4],
            ['f',100,600,4.4],
            ['g',10,100,4.4],
            ['h',100,400,9.1],
            ['i',0,70,6.6],
            ['j',0,20,6.6]
              

           
           
           
    ]

    dmd = [1461,
        1446,
        1446,
        1438,
        1425,
        1420,
        1467,
        1503,
        1507,
        1504,
        1504,
        1502,
        1498,
        1496,
        1492,
        1492,
        1492,
        1509,
        1518,
        1517,
        1515,
        1496,
        1479,
        1463,

    ]
    
    main(gnt,dmd)