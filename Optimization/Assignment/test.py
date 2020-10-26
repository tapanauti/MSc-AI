from ortools.linear_solver import pywraplp




def configure_variables(cfg, solver):
	food = cfg['food']
	minShop = cfg['minShop']
	variable_list = [[]] * len(food)
	for i in range(0, len(food)):
		#you must buy at least minShop of each
		variable_list[i] = solver.NumVar(minShop, solver.infinity(), str(food[i][0]))

	return variable_list


def configure_constraints(cfg, solver, variable_list):
	food = cfg['food']
	maxWeight = cfg['maxWeight']
	maxCost = cfg['maxCost']
	minCals = cfg['minCals']

	#Define the constraints	
	constraint_list=[]
	#Constraint 1: totalWeight<maxWeight
	#ham + lettuce + cheese + tuna + bread <= maxWeight
	constraint_list.append(solver.Constraint(0, maxWeight))
	for i in range(0, len(food)):
		constraint_list[0].SetCoefficient(variable_list[i],1)

	#Constraint 2: totalPrice<=maxCost
	constraint_list.append(solver.Constraint(0, maxCost))
	for i in range(0, len(food)):
		constraint_list[1].SetCoefficient(variable_list[i],food[i][2])

	#Constraint 3: totalCalories>=minCals
	constraint_list.append(solver.Constraint(minCals, minCals + 100))
	for i in range(0, len(food)):
		constraint_list[2].SetCoefficient(variable_list[i],food[i][1])

	return constraint_list


def configure_objective(what, cfg, solver, variable_list, constraint_list):
	
	food = cfg['food']

	objective = solver.Objective()

	if (what=='cost'):
		# Define our objective: minimizing cost
		for i in range(0, len(food)):
			objective.SetCoefficient(variable_list[i], food[i][2])
		objective.SetMinimization()

	elif(what=='calories'):
		# Define our objective: maximizing calories
		for i in range(0, len(food)):
			objective.SetCoefficient(variable_list[i], food[i][1])
		objective.SetMaximization()

	elif(what=='fat-free'):
		# Define our objective: cutting on ham and cheese
		for i in range(0, len(food)):
			if (food[i][0] in ['ham','cheese']):
				objective.SetCoefficient(variable_list[i],1)
		objective.SetMinimization()

	elif(what=='gluten-free'):
		# Define our objective: cutting on ham, cheese and tuna
		for i in range(0, len(food)):
			if (food[i][0] in ['bread']):
				objective.SetCoefficient(variable_list[i],1)
		objective.SetMinimization()

	else:
		# Define our objective: use all the money
		for i in range(0, len(food)):
			objective.SetCoefficient(variable_list[i], food[i][2])
		objective.SetMaximization()

	return objective


def solve(solver):
	result_status = solver.Solve()
	return result_status

def print_solution(solver,result_status,variable_list,constraint_list):

	if result_status == solver.OPTIMAL:
		print('Successful solve.')
		# The problem has an optimal solution.
		print(('Problem solved in %f milliseconds' % solver.wall_time()))
		# The objective value of the solution.
		print(('Optimal objective value = %f' % solver.Objective().Value()))
		# The value of each variable in the solution.
		var_sum=0
		for variable in variable_list:
			print(('%s = %f' % (variable.name(), variable.solution_value())))
			var_sum+=variable.solution_value()
		print(('Variable sum = %f' % var_sum));

		print('Advanced usage:')
		print(('Problem solved in %d iterations' % solver.iterations()))

		for variable in variable_list:
			print(('%s: reduced cost = %f' % (variable.name(), variable.reduced_cost())))
		
		activities = solver.ComputeConstraintActivities()
		for i, constraint in enumerate(constraint_list):
			print(('constraint %d: dual value = %f\n'
		      '               activity = %f' %
		      (i, constraint.dual_value(), activities[constraint.index()])))

	#elif result_status == solver.INFEASIBLE:
   	#	print('No solution found.')
  	#elif result_status == solver.POSSIBLE_OVERFLOW:
		# print('Some inputs are too large and may cause an integer overflow.')

def main(cfg, what):

	solver = pywraplp.Solver('SolveSimpleSystem',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

	variable_list = configure_variables(cfg, solver)
	constraint_list = configure_constraints(cfg, solver, variable_list)
	objective = configure_objective(what, cfg, solver, variable_list, constraint_list)

	result_status = solve(solver)

	print_solution(solver, result_status, variable_list, constraint_list)

	return {'variable_list':variable_list, 
			'constraint_list': constraint_list, 
			'objective':objective, 
			'solver':solver, 
			'result_status': result_status}

if __name__ == '__main__':


	cfg = {'maxWeight': 10,
			'maxCost': 100,
			'minCals': 14000,
			'minShop': 4/16.0, #16 ounces per pound
			'food':  [['ham',650, 4],
						['lettuce',70,1.5],
						['cheese',1670,5],
						['tuna',830,20],
						['bread',1300,1.20]]
		}

	main(cfg,'cost')
