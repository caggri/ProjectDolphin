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
	if amount >=6:
		y = 6
		x = amount - 6
	elif amount < 6:
		x = 0
		y = amount
	return x, y

def yToX(x, y):
	amount = x + y
	if amount >=10:
		x = 10
		y = amount - 10
	elif amount < 10:
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
	return allowed

def isVisited(test_x, test_y, path):
	for i in range(len(path)):
		if(path[i] == [test_x, test_y]):
			return True
	return False

def runSearch(x, y):
	path = [[x,y]]
	count = 1
	while x != goal:
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
		if(is_visited == False):
			x, y = eval(run_function)
			path.append([x, y])
			count += 1

	return count, path
# Main
if __name__ == "__main__":
	for i in range(1,6):
		count, path = runSearch(x, y)
		print("Search number ",i," completed!")
		print(path)
		print(count," times turned!")