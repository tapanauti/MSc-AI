from ortools.linear_solver import pywraplp, _pywraplp




def const(gnt,solver,var_list):
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[3] + var_list[4] + var_list[5] + var_list[6] + var_list[7] + var_list[8]+ var_list[9] == dmd[0])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[10] + var_list[11] + var_list[12] + var_list[13] + var_list[14] + var_list[15]+ var_list[16] == dmd[1])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[17] + var_list[18] + var_list[19] + var_list[20] + var_list[21] + var_list[22]+ var_list[23] == dmd[2])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[24] + var_list[25] + var_list[26] + var_list[27] + var_list[28] + var_list[29]+ var_list[30] == dmd[3])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[31] + var_list[32] + var_list[33] + var_list[34] + var_list[35] + var_list[36]+ var_list[37] == dmd[4])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[38] + var_list[39] + var_list[40] + var_list[41] + var_list[42] + var_list[43]+ var_list[44] == dmd[5])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[45] + var_list[46] + var_list[47] + var_list[48] + var_list[49] + var_list[50]+ var_list[51] == dmd[6])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[52] + var_list[53] + var_list[54] + var_list[55] + var_list[56] + var_list[57]+ var_list[58] == dmd[7])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[59] + var_list[60] + var_list[61] + var_list[62] + var_list[63] + var_list[64]+ var_list[65] == dmd[8])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[66] + var_list[67] + var_list[68] + var_list[69] + var_list[70] + var_list[71]+ var_list[72] == dmd[9])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[73] + var_list[74] + var_list[75] + var_list[76] + var_list[77] + var_list[78]+ var_list[79] == dmd[10])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[80] + var_list[81] + var_list[82] + var_list[83] + var_list[84] + var_list[85]+ var_list[86] == dmd[11])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[87] + var_list[88] + var_list[89] + var_list[90] + var_list[91] + var_list[92]+ var_list[93] == dmd[12])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[94] + var_list[95] + var_list[96] + var_list[97] + var_list[98] + var_list[99]+ var_list[100] == dmd[13])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[101] + var_list[102] + var_list[103] + var_list[104] + var_list[105] + var_list[106]+ var_list[107] == dmd[14])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[108] + var_list[109] + var_list[110] + var_list[111] + var_list[112] + var_list[113]+ var_list[114] == dmd[15])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[115] + var_list[116] + var_list[117] + var_list[118] + var_list[119] + var_list[120]+ var_list[121] == dmd[16])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[122] + var_list[123] + var_list[124] + var_list[125] + var_list[126] + var_list[127]+ var_list[128] == dmd[17])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[129] + var_list[130] + var_list[131] + var_list[132] + var_list[133] + var_list[134]+ var_list[135] == dmd[18])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[136] + var_list[137] + var_list[138] + var_list[139] + var_list[140] + var_list[141]+ var_list[142] == dmd[19])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[143] + var_list[144] + var_list[145] + var_list[146] + var_list[147] + var_list[148]+ var_list[149] == dmd[20])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[150] + var_list[151] + var_list[152] + var_list[153] + var_list[154] + var_list[155]+ var_list[156] == dmd[21])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[157] + var_list[158] + var_list[159] + var_list[160] + var_list[161] + var_list[162]+ var_list[163] == dmd[22])
    con_list = solver.Add(var_list[0] + var_list[1] + var_list[2]+ var_list[66] + var_list[164] + var_list[165] + var_list[166] + var_list[167] + var_list[168]+ var_list[169] == dmd[23])
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
	
    var_list = [solver.NumVar(gnt[z][1],gnt[z][2],str(gnt[z][0])) for z in range (0,len(gnt))]
    print(var_list)
    con_list = const(gnt,solver,var_list)   
    objt = obj(gnt,solver,var_list,con_list)
    result = solve(solver)
    prt(solver,objt)
	
	
   
     
   

    return{'var_list':var_list,
            'con_list':con_list,
            'objt':objt,
            'solver':solver,
            'result':result}

if __name__ == '__main__':


    gnt = [ ['e',100,900,4.4],['f',100,600,4.4],['g',10,100,4.4],['a1',10,100,1.4],['b1',10,80,1.4],['c1',10,60,1.4],['d1',1,10,1.4],     
		['h1',100,400,9.1],['i1',0,0,6.6],['j1',0,0,6.6],['a2',10,100,1.4],['b2',10,80,1.4],['c2',10,60,1.4],['d2',1,10,1.4],['h2',100,400,9.1],['i2',0,0,6.6],['j2',0,0,6.6],['a3',10,100,1.4],['b3',10,80,1.4],['c3',10,60,1.4],
		['d3',1,10,1.4],['h3',100,400,9.1],['i3',0,0,6.6],['j3',0,0,6.6],['a4',10,100,1.4],['b4',10,80,1.4],['c4',10,60,1.4],['d4',1,10,1.4],['h4',100,400,9.1],['i4',0,0,6.6],['j4',0,0,6.6],['a5',10,100,1.4],['b5',10,80,1.4],
		['c5',10,60,1.4],['d5',1,10,1.4],['h5',100,400,9.1],['i5',0,0,6.6],['j5',0,0,6.6],['a6',10,100,1.4],['b6',10,80,1.4],['c6',10,60,1.4],['d6',1,10,1.4],['h6',100,400,9.1],['i6',0,0,6.6],['j6',0,0,6.6],['a7',10,100,1.4],
		['b7',10,80,1.4],['c7',10,60,1.4],['d7',1,10,1.4],['h7',100,400,9.1],['i7',0,35,6.6],['j7',0,10,6.6],['a8',10,100,1.4],['b8',10,80,1.4],['c8',10,60,1.4],['d8',1,10,1.4],['h8',100,400,9.1],['i8',0,35,6.6],['j8',0,10,6.6],
		['a9',10,100,1.4],['b9',10,80,1.4],['c9',10,60,1.4],['d9',1,10,1.4],['h9',100,400,9.1],['i9',0,35,6.6],['j9',0,10,6.6],['a10',10,100,1.4],['b10',10,80,1.4],['c10',10,60,1.4],['d10',1,10,1.4],        
		['h10',100,400,9.1],['i10',0,35,6.6],['j10',0,10,6.6],['a11',10,100,1.4],['b11',10,80,1.4],['c11',10,60,1.4],['d11',1,10,1.4],['h11',100,400,9.1],['i11',0,35,6.6],['j11',0,10,6.6],
		['a12',10,100,1.4],['b12',10,80,1.4],['c12',10,60,1.4],['d12',1,10,1.4],['h12',100,400,9.1],['i12',0,70,6.6],['j12',0,20,6.6],['a13',10,100,1.4],['b13',10,80,1.4],['c13',10,60,1.4],
		['d13',1,10,1.4],['h13',100,400,9.1],['i13',0,70,6.6],['j13',0,20,6.6],['a14',10,100,1.4],['b14',10,80,1.4],['c14',10,60,1.4],['d14',1,10,1.4],['h14',100,400,9.1],['i14',0,70,6.6],['j14',0,20,6.6],
        ['a15',10,100,1.4],['b15',10,80,1.4],['c15',10,60,1.4],['d15',1,10,1.4],['h15',100,400,9.1],['i15',0,70,6.6],['j15',0,20,6.6],['a16',10,100,1.4],['b16',10,80,1.4],['c16',10,60,1.4],['d16',1,10,1.4],['h16',100,400,9.1],
		['i16',0,70,6.6],['j16',0,20,6.6],['a17',10,100,1.4],['b17',10,80,1.4],['c17',10,60,1.4],['d17',1,10,1.4],['h17',100,400,9.1],['i17',0,35,6.6],['j17',0,10,6.6],['a18',10,100,1.4],['b18',10,80,1.4],['c18',10,60,1.4],
		['d18',1,10,1.4],['h18',100,400,9.1],['i18',0,35,6.6],['j18',0,10,6.6],['a19',10,100,1.4],['b19',10,80,1.4],['c19',10,60,1.4],['d19',1,10,1.4],['h19',100,400,9.1],['i19',0,35,6.6],['j19',0,10,6.6],
		['a20',10,100,1.4],['b20',10,80,1.4],['c20',10,60,1.4],['d20',1,10,1.4],['h20',100,400,9.1],['i20',0,0,6.6],['j20',0,0,6.6],['a21',10,100,1.4],['b21',10,80,1.4],['c21',10,60,1.4],['d21',1,10,1.4],['h21',100,400,9.1],
		['i21',0,0,6.6],['j21',0,0,6.6],['a22',10,100,1.4],['b22',10,80,1.4],['c22',10,60,1.4],['d22',1,10,1.4],['h22',100,400,9.1],['i22',0,0,6.6],['j22',0,0,6.6],['a23',10,100,1.4],['b23',10,80,1.4],['c23',10,60,1.4],
		['d23',1,10,1.4],['h23',100,400,9.1],['i23',0,0,6.6],['j23',0,0,6.6],['a24',10,100,1.4],['b24',10,80,1.4],['c24',10,60,1.4],['d24',1,10,1.4],['h24',100,400,9.1],['i24',0,0,6.6],['j24',0,0,6.6]


           
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

