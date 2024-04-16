# Path Planning Algorithms:
1. Some of the path planning algorithms and their variants include:
   > Dijkstra’s Algorithm and variants (Graph Search)
   > A* Algorithm and variants (Informed Search (Heuristic))
   > RRT (Rapidly exploring Random Tree) Algorithm and variants (Sampling-Based (Probabilistic))
   Dijkstra’s algorithm systematically explores all possible paths in a graph, assigning distances to each node. It prioritizes visiting the node with the currently shortest distance estimate. This process continues until the goal node is reached.

A* The algorithm  is similar to Dijkstra's, it explores the graph, but it uses a heuristic function to estimate the remaining cost (distance or time) to reach the goal from any point in the search space.

RRT Algorithm's probabilistic approach builds a tree structure from the starting point, randomly sampling points in the configuration space (all possible robot poses) and attempting to connect them to the existing tree while avoiding obstacles. This process continues until the goal is reached or a time limit is met.

   
