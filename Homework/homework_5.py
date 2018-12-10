"""
Project Dolphin
----------------
Mehmet Ali Karakamış
Semih Teker
Çağrı Bayram
Burak Yaşar
Berk Türk

This homework was done based on this resource below
https://github.com/tsoding/kdtree-in-python
which was built in Python2 and also kdtree partition was done such that divison lines go throgh
the points. We inverted the code to the Python3 and changed its structure so that our partition on
kdtree divides the areas by going through the middle of points(between the points)
instead of going over them
In our resource kd-tree was built by taking points as the nodes(root and child), we changed this
structure such that our tree takes the intersection points where the lines intersect according to
our division
"""

import math
import pprint

pp = pprint.PrettyPrinter(indent=3)

k = 2 # depth
all_points = [[1,2],[2,1],[2,5],[2,6],[4,2],[5,6],[6,1],[6,5]]
new_point = [[1,4],[1,1],[6,6],[6,1],[4,4]]
other_points = [[2, 1], [2, 5], [2, 6], [4, 2], [5, 6], [6, 1], [6, 5]]
threshold_point = []

def distance(point1, point2):
	x1, y1 = point1
	x2, y2 = point2

	dx = x1 - x2
	dy = y1 - y2

	return math.sqrt(dx * dx + dy * dy)


def closer_distance(pivot, p1, p2):
	if p1 is None:
		return p2

	if p2 is None:
		return p1

	d1 = distance(pivot, p1)
	d2 = distance(pivot, p2)

	if d1 < d2:
		return p1
	else:
		return p2
"""
find_average function is used to find the line which acrosses the middle of points
to do this calculation the axis and the points are informed via parameters
according to axis the fuction simply calculate the average point
the return value is the point where the line intersects the corresponding axis
"""
def find_average(axis, points):
	sum_x = 0
	sum_y = 0

	for point in points:
		sum_x += point[0]
		sum_y += point[1]

	avg_x = sum_x / (len(points) * 1.0)
	avg_y = sum_y / (len(points) * 1.0)

	if axis is 0:
		threshold_point.append([avg_x, 0])
		return (avg_x, 0)
	else:
		threshold_point.append([0, avg_y])
		return (0, avg_y)
"""
build_kdtree is a recursive function to bild a kdtree from the given points array
axis is changed in each step by looking the remainder of 2, 0 for x-axis, 1 for y-axis
the given points are sorted according to axis and sent to find_average function to find middle line
the given points are grouped by looking the avg_point and split two groups
the build_kdtree function is called again until the length of the points array becomes 1
each call returns as an element of the tree with point, left and rigth attributes
"""
def build_kdtree(points, depth=0):
	n = len(points)
	if n <= 1:
		return None

	axis = depth % k
	sorted_points = sorted(points, key=lambda point: point[axis])
	avg_point = find_average(axis, sorted_points)

	next_points_right = []
	next_points_left = []

	if axis == 0:
		t = avg_point[0]
		for p in sorted_points:
			if p[0] > t:
				next_points_right.append(p)
			else:
				next_points_left.append(p)
	else:
		t = avg_point[1]
		for p in sorted_points:
			if p[1] > t:
				next_points_right.append(p)
			else:
				next_points_left.append(p)
	return {
		'point': sorted_points[int((n)/2)],
		'left': build_kdtree(next_points_left, depth + 1),
		'right': build_kdtree(next_points_right, depth + 1)
	}

"""
kdtree_closest_point fuction is used to find the point in the given points set closest to given point
by tracing the kdtree from root to leaves. according to distance metric of the left and rigth childs
it chooses the proper way to find closest point recursively.
"""
def kdtree_closest_point(root, point, depth=0):
	if root is None:
		return None

	axis = depth % k
	next_branch = None
	opposite_branch = None

	if point[axis] < root['point'][axis]:
		print ("-> Left")
		next_branch = root['left']
		opposite_branch = root['right']
	else:
		print ("-> Right")
		next_branch = root['right']
		opposite_branch = root['left']

	best = closer_distance(point,
						   kdtree_closest_point(next_branch,
												point,
												depth + 1),
						   root['point'])

	if distance(point, best) > abs(point[axis] - root['point'][axis]):
		best = closer_distance(point,
							   kdtree_closest_point(opposite_branch,
													point,
													depth + 1),
							   best)
	return best

# Main
if __name__ == "__main__":
	print("\n**************** EUCLID METRIC ****************\n")
	""" Simple distance method based on input point
	calculate the distance between input point and each given point on the map
	works in O(N) where N is the number of given points on the map"""
	for current_point in new_point:
		distance_1 = distance(current_point, [1,2])
		result = [1, 2]
		for point in other_points:
			distance_2 = distance(current_point, point)
			#nonlocal distance_1
			if (distance_2 < distance_1):
				result = point
				distance_1 = distance_2

		print("The closest point for ", current_point)
		if result == [1, 2]:
			print("is (1, 2) and it's color red")
		elif result == [2, 1]:
			print("is (2, 1) and it's color violet")
		elif result == [2, 5]:
			print("is (2, 5) and it's color orange")
		elif result == [2, 6]:
			print("is (2, 6) and it's color red")
		elif result == [4, 2]:
			print("is (4, 2) and it's color blue")
		elif result == [5, 6]:
			print("is (5, 6) and it's color yellow")
		elif result == [6, 1]:
			print("is (6, 1) and it's color green")
		elif result == [6, 5]:
			print("is (6, 5) and it's color purple")
		else:
			print("No closest point has been found!")

	kdtree = build_kdtree(all_points)

	print ("\n**************** ALL TREE ****************\n")
	pp.pprint(kdtree)
	print ("\n******************************************\n")

	for current_point in new_point:
		res = kdtree_closest_point(kdtree, current_point);
		print ("The closest point for ", current_point)
		if res == [1,2]:
			print ("is (1, 2) and it's color red")
		elif res == [2, 1]:
			print ("is (2, 1) and it's color violet")
		elif res == [2, 5]:
			print ("is (2, 5) and it's color orange")
		elif res == [2, 6]:
			print ("is (2, 6) and it's color red")
		elif res == [4, 2]:
			print ("is (4, 2) and it's color blue")
		elif res == [5, 6]:
			print ("is (5, 6) and it's color yellow")
		elif res == [6, 1]:
			print ("is (6, 1) and it's color green")
		elif res == [6, 5]:
			print ("is (6, 5) and it's color purple")
		else:
			print ("No closest point has been found!")
