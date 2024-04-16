import numpy as np
import matplotlib.pyplot as plt
import random

# Node class definition
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.cost = 0.0


def node_2_node_distance(node1, node2):
# This function [Assumes nodes are in 2D plane] defenition is to compute the euclidean distance between two nodes.
    return np.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)

def check_collision_free(new_node, obstacles, obstacle_radius):
# This is a collision checking function. By default it assumes True, ie. no collision.
    for obstacle in obstacles:
        distance = node_2_node_distance(new_node, obstacle)
        if distance < obstacle_radius:
            return False  # Collision
    return True  # Default -> collision free

def move_node_2_node(from_node, to_node, max_distance):
# Moves between nodes within a maximum distance.
# complete the code to move between nodes, where new_x &new_y are the end points.
    if(node_2_node_distance(from_node,to_node)<max_distance):
        x_new=to_node.x
        y_new=to_node.y
        return Node(x_new,y_new)
    else:
        x_new=from_node.x+max_distance*(to_node.x-from_node.x)/node_2_node_distance(to_node,from_node)
        y_new=from_node.y+max_distance*(to_node.y-from_node.y)/node_2_node_distance(to_node,from_node)
        return Node(x_new,y_new)

def rewire_tree(tree, new_node, max_distance, obstacles, obstacle_radius, goal):
# complete the Function that reqires the tree to update the parent of nodes if a shorter path is found
    for node in tree:
        if node != new_node.parent and node_2_node_distance(new_node, node) < max_distance and check_collision_free(new_node, obstacles, obstacle_radius):
            if check_collision_free(move_node_2_node(node, new_node, max_distance), obstacles, obstacle_radius):
                direction_to_parent = (new_node.parent.x - node.x, new_node.parent.y - node.y)
                direction_to_goal = (goal.x - node.x, goal.y - node.y)
                dot_product = direction_to_parent[0] * direction_to_goal[0] + direction_to_parent[1] * direction_to_goal[1]
                cosine_similarity = dot_product / (np.linalg.norm(direction_to_parent) * np.linalg.norm(direction_to_goal))
                if cosine_similarity > 0:
                    new_node.parent = node
                    new_node.cost = node.cost + node_2_node_distance(new_node, node)
                    while node.parent:
                        node.cost = node.parent.cost + node_2_node_distance(node, node.parent)
                        node = node.parent

def is_range(node, x_range, y_range):
    if(node.x>min(x_range) and node.x<max(x_range)
       and node.y>min(y_range) and node.y<max(y_range)):
        return False
    return True

# Main RRT* algorithm
def rrt_star(start, goal, x_range, y_range, obstacles, max_iter=1000, max_distance=1, obstacle_radius=1):
    path=[start]
    newn=start
    ep=0.2
    for i in range (max_iter):
        print(i)
        direx=(goal.x-newn.x)/node_2_node_distance(newn,goal)
        direy=(goal.y-newn.y)/node_2_node_distance(newn,goal)
        x_adj=random.uniform(direx+ep,direx-ep)*max_distance
        y_adj=random.uniform(direy+ep,direy-ep)*np.sqrt((max_distance**2)-(x_adj**2))
        randomn=Node(newn.x+x_adj,newn.y+y_adj)
        
        if is_range(randomn,x_range,y_range):
            continue
        newn=move_node_2_node(newn,randomn,max_distance)
        if not check_collision_free(newn,obstacles, obstacle_radius):
            rewire_tree(path, newn, max_distance, obstacles, obstacle_radius, goal)
            path.append(newn)
            if node_2_node_distance(newn,goal)<max_distance:
                path.append(goal)
                return path
    return path

# Here I have set up the start and goal nodes, state space, obstacles and radius of obstacle(assumed circular).
start_node = Node(0, 0)
goal_node = Node(5, 5)
x_range = (-1, 6)
y_range = (-1, 6)
obstacle1 = Node(1, 1)
obstacle2 = Node(2, 0.5)
obstacle3 = Node(2, 2)
obstacle4 = Node(3, 4)
obstacle5 = Node(3, 0)
obstacle6 = Node(4, 1)
obstacle7 = Node(3, 3)
obstacle8 = Node(1.5, 3)
obstacle9 = Node(4, 4)
obstacle10 = Node(0, 1)
obstacle11 = Node(1.3, 2)
obstacle12 = Node(2.5, 1.3)
obstacle13 = Node(3.5, 1.5)
obstacle14 = Node(4, 2)
obstacle15 = Node(4.5, 3)
obstacle16 = Node(5, 4)
obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7, obstacle8, obstacle9, obstacle10, obstacle11, obstacle12, obstacle13, obstacle14, obstacle15, obstacle16]
obstacle_radius = 0.2

# Running the RRT* algorithm.
max_iter=10
path = rrt_star(start_node, goal_node, x_range, y_range, obstacles)


# Plotting results for Visualization.
plt.scatter(start_node.x, start_node.y, color='green', marker='o', label='Start')
plt.scatter(goal_node.x, goal_node.y, color='red', marker='o', label='Goal')
plt.scatter(*zip(*[(obstacle.x, obstacle.y) for obstacle in obstacles]), color='black', marker='x', label='Obstacle')
plt.plot(*zip(*[(node.x,node.y) for node in path]),linestyle='-',marker='.', color='blue', label='Path')
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('RRT* algorithm')
plt.show()