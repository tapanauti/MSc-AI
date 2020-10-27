from ortools.linear_solver import pywraplp, _pywraplp




def const(gnt,solver,var_list,variables):
    # con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[3] + var_list[4] + var_list[5] + var_list[6] + var_list[7] + var_list[8]+ var_list[9] == dmd[0])
    # con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[10] + var_list[11] + var_list[12] + var_list[13] + var_list[14] + var_list[15]+ var_list[16] == dmd[1])
    #for i in range(0,3):
    for j in range(0,3):
        con_list = solver.Add(var_list[0] + var_list[1] + var_list[2] + variables[0][j] + variables[1][j] == 400  )

    return con_list


def obj(gnt,solver,var_list,con_list):

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

   
        
def main(gnt,dmd):

    solver = pywraplp.Solver('Generator',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
	
    variables = [['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13','a14','a15','a16','a17','a18','a19','a20','a21','a22','a23','a24'],
    ['b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','b12','b13','b14','b15','b16','b17','b18','b19','b20','b20','b21','b22','b23','b24']]
    var_list = [solver.NumVar(100,900,'e'), solver.NumVar(100,600,'f'),solver.NumVar(10,100,'g') ]
    
    for i in range(0,len(variables)):
        var_list.extend([solver.NumVar(gnt[i][1],gnt[i][2],str(variables[i][z])) for z in range (0,24)])

    print(var_list)
    con_list = const(gnt,solver,var_list,variables)   
    objt = obj(gnt,solver,var_list,con_list)
    result = solve(solver)
    prt(solver,objt)
	
	
   
     
   

    return{'var_list':var_list,
            'con_list':con_list,
            'objt':objt,
            'solver':solver,
            'result':result}

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