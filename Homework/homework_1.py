"""
We have 6 operators which are fullX() to fill the x jug, 
				fullY() to fill the y jug, 
				emptyX() to dump the x jug,
				emptyY() to dump the y jug,
				xToY() to pour the x jug to the y jug,
 				yToX() to pour the y jug to the x jug respectively.
 Our algorithm chooses an operator randomly and apply that function to the current state,
 while doing so it also checks whether the possible states are already visited to avoids irrelevant loops.
 Our goal is to reach the (8,d) state starting from (0,0) (where d is don't care value).
 The possible next states are at most 4 (branching factor).
"""
import random
# Initial state of x and y
x = 0
y = 0
goal = 8

x_max = 10
y_max = 6

def fullX(x, y):
	x = x_max
	return x, y

def fullY(x, y):
	y = y_max
	return x, y

def emptyX(x, y):
	x = 0
	return x, y

def emptyY(x, y):
	y = 0
	return x, y

def xToY(x, y):
	amount = x + y
	if amount >=y_max: # y_max = 6
		y = y_max
		x = amount - y_max
	elif amount < y_max:
		x = 0
		y = amount
	return x, y

def yToX(x, y):
	amount = x + y
	if amount >=x_max: # x_max = 10
		x = x_max 
		y = amount - x_max
	elif amount < x_max:
		x = amount
		y = 0
	return x, y

def randomStep(x, y):
	allowed = ["fullX", "fullY", "emptyX", "emptyY", "xToY", "yToX"]
	if x == x_max:
		allowed.remove("fullX")
	if y == y_max:
		allowed.remove("fullY")
	if x == 0:
		allowed.remove("emptyX")
		allowed.remove("xToY")
	if y == 0:
		allowed.remove("emptyY")
		allowed.remove("yToX")
	if x == x_max and y == y_max:
		allowed = ["emptyX","emptyY"]
	return allowed

def isVisited(test_x, test_y, path):
	for i in range(len(path)):
		if path[i] == [test_x, test_y]:
			return True
	return False

def runSearch(x, y):
	global_count = 0
	path = [[x,y]]
	count = 1
	while x != goal:
		# Avoid loop causing due to random function
		if global_count == 50:
			return None, None, False
		global_count += 1

		test_x = x
		text_y = y

		# Get random available function
		functions = randomStep(x, y)
		get_random_index = random.randint(0,len(functions)-1)
		run_function = (functions[get_random_index]+"(x, y)")
		test_x, test_y = eval(run_function)

		# Test if the path visited before
		is_visited = isVisited(test_x, test_y, path)
		# If false visit there
		if is_visited == False:
			x, y = eval(run_function)
			path.append([x, y])
			count += 1

	return count, path, True
# Main
if __name__ == "__main__":
	i = 1
	while i <= 5:
		count, path, is_ok = runSearch(x, y)
		if is_ok:
			print("Search number ",i," completed!")
			print(path)
			print(count," times turned!")
			i += 1
