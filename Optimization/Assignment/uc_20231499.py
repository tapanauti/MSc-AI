from ortools.linear_solver import pywraplp



def variable(gnt,solver,hr):

    zero = [1,2,3,4,5,6,20,21,22,23,24]
    fifty = [7,8,9,10,11,17,18,19]
    full = [12,13,14,15,16]
    
    var_list = [solver.NumVar(gnt[z][1],gnt[z][2],str(gnt[z][0])) for z in range (0,len(gnt))]

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

    con_list.append(solver.Constraint(1461))
    for i in range (0,len(var_list)):
        con_list[0].SetCoefficient(var_list[i],1)

    return con_list

def obj(hr,gnt,solver,var_list,con_list):

    objt= solver.Objective()

    

def main(gnt):

    solver = pywraplp.Solver('Generator',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    #for hr in range(1,24):
    var_list = variable(gnt,solver,1)


    

if __name__ == '__main__':


    gnt = [['a',10,100,1.4],
            ['b',10,80,1.4],
            ['c',10,60,1.4],
            ['d',1,10,1.4],
            ['e',100,900,4.4],
            ['f',100,600,4.4],
            ['g',10,100,4.4],
            ['h',100,400,9.1],
            #['i',0,70,6.6],
            #['j',0,20,6.6]
    ]
    
    main(gnt)