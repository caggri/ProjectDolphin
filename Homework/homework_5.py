import math
import pprint

pp = pprint.PrettyPrinter(indent=3)

k = 2 # depth
all_points = [[1,2],[2,1],[2,5],[2,6],[4,2],[5,6],[6,1],[6,5]]
new_point = [[1,4],[1,1],[6,6],[6,1],[4,4]]
threshold_point = []
threshold_i = 0

def distance(point1, point2):
	x1, y1 = point1
	x2, y2 = point2

	dx = x1 - x2
	dy = y1 - y2

	return math.sqrt(dx * dx + dy * dy)

def closest_point(all_points, new_point):
	best_point = None
	best_distance = None

	for current_point in all_points:
		current_distance = distance(new_point, current_point)

		if best_distance is None or current_distance < best_distance:
			best_distance = current_distance
			best_point = current_point

	return best_point

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
ksay = 0
def kdtree_closest_point(root, point, depth=0):
	global ksay
	if root is None:
		return None

	axis = depth % k

	next_branch = None
	opposite_branch = None

	if point[axis] < root['point'][axis]:
		print ("-> Left")
		ksay = ksay+1
		next_branch = root['left']
		opposite_branch = root['right']
	else:
		print ("-> Right")
		ksay = ksay+1
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
		print("ksay", ksay)
