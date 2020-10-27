from ortools.linear_solver import pywraplp, _pywraplp



def variable(gnt,solver,hr):

    zero = [1,2,3,4,5,6,20,21,22,23,24]
    fifty = [7,8,9,10,11,17,18,19]
    full = [12,13,14,15,16]
    var_list = [solver.NumVar(gnt[z][1],gnt[z][2],str(gnt[z][0])) for z in range (0,len(gnt)-2)]

    if hr in zero:
        var_list.append(solver.NumVar(0,0,'i'))
        var_list.append(solver.NumVar(0,0,'j'))

    elif hr in fifty:
        var_list.append(solver.NumVar(0,35,'i'))
        var_list.append(solver.NumVar(0,10,'j'))

    elif hr in full:
        var_list.append(solver.NumVar(0,70,'i'))
        var_list.append(solver.NumVar(0,20,'j'))
    

    return var_list

def const(gnt,solver,var_list,hr):

    con_list = []  
    for i in range(0,len(dmd)):
        if hr == i+1:
            con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[3] + var_list[4] + var_list[5] + var_list[6] + var_list[7] + var_list[8]+ var_list[9] == dmd[i])
            
       
      
    return con_list

def obj(hr,gnt,solver,var_list,con_list):

    objt= solver.Objective()

    for i in range(0,len(gnt)):
        objt.SetCoefficient(var_list[i],gnt[i][3])
    objt.SetMinimization()
    
    return objt

def solve(solver):
    result = solver.Solve()
    return result


def prt(solver,objt):
    for v in solver.variables():
        print(f"{v.name()} = {v.solution_value():.5}; coefficient {objt.GetCoefficient(v):.5}")
            
    print(f"Optimal objective value = {objt.Value():.5}")

   
        
def main(gnt):

    solver = pywraplp.Solver('Generator',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    for hr in range(1,3):
        var_list = variable(gnt,solver,hr)
        con_list = const(gnt,solver,var_list,hr)
        objt = obj(hr,gnt,solver,var_list,con_list)
        result = solve(solver)
        print_sol(solver,result,var_list,con_list)
        prt(solver,objt)
        solver.Clear()

       
   

    return{'var_list':var_list,
            'con_list':con_list,
            'objt':objt,
            'solver':solver,
            'result':result}

if __name__ == '__main__':


    gnt = [['a',10,100,1.4],
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
    
    main(gnt)