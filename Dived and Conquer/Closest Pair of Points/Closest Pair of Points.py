import random
import sys


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def random_points(n):
    points = []
    for i in range(n):
        points.append(Point(random.randint(0, 100), random.randint(0, 100)))

    return points


def closest_pair(points):

    def distance(p1: Point, p2: Point):
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
    
    # if points is empty, return infinity as the distance
    if len(points) == 1:
        return (points[0], points[0]), sys.maxsize
    
    if len(points) == 0:
        return (Point(0, 0), Point(0, 0)), sys.maxsize

    # terminate if there are less than 3 points, just use brute force method to find closest pair and return that point and distance between them
    if len(points) < 3:
        data = list()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                data.append((points[i], points[j], distance(points[i], points[j])))
        data.sort(key=lambda x: x[2])
        return (data[0][0], data[0][1]), data[0][2]  # return the closest pair

    # split the points into two halves, and find a vertical line that divides the points into two halves
    # divide
    mid = len(points)//2
    left_points = [points[i] for i in range(mid) if points[i].x < mid]
    right_points = [points[i] for i in range(mid) if points[i].x >= mid]
    left_pair, left_min = closest_pair(left_points)
    right_pair, right_min = closest_pair(right_points)

    # combine the two halves and find the closest pair of points
    min_distance = min(left_min, right_min)
    min_pair = left_pair if left_min < right_min else right_pair
    
    # remove points that are too far away from the line
    points = [points[i] for i in range(len(points)) if abs(points[i].x - mid) < min_distance]

    # # for point pi in stored points
    for i in range(len(points)):
        # compute the distance between point pi+1, pi+2 , ... , pi+7
        for j in range(i+1, len(points)):
            if abs(points[i].y - points[j].y) < min_distance:
                # update delta if the distance is smaller than the current delta
                min_distance = distance(points[i], points[j])
                min_pair = (points[i], points[j])

    # return the closest pair and the distance between the two points
    return min_pair, min_distance


if __name__ == '__main__':

    # generate random 20 points
    points = random_points(20)
    
    #print all points
    for i in points:
        print(i.x, i.y)

    # #sort points by x-coordinate and y-coordinate and store them in Px and Py
    sorted(points, key=lambda x: (x.x, x.y))
    points, distance = closest_pair(points)
    print("Closest pair of points: ({}, {}) ({}, {})".format(points[0].x , points[0].y , points[1] .x , points[1].y))
    print("Distance between the two points:", distance)
