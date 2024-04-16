# Path Planning Algorithms:
Question 1:
Some of the path planning algorithms and their variants include:
1. Dijkstra’s Algorithm and variants (Graph Search)
2. A* Algorithm and variants (Informed Search (Heuristic))
3. RRT (Rapidly exploring Random Tree) Algorithm and variants (Sampling-Based (Probabilistic))
	
Dijkstra’s algorithm systematically explores all possible paths in a graph, assigning distances to each node. It prioritizes visiting the node with the currently shortest distance estimate. This process continues until the goal node is reached.

A* The algorithm  is similar to Dijkstra's, it explores the graph, but it uses a heuristic function to estimate the remaining cost (distance or time) to reach the goal from any point in the search space.

RRT Algorithm's probabilistic approach builds a tree structure from the starting point, randomly sampling points in the configuration space (all possible robot poses) and attempting to connect them to the existing tree while avoiding obstacles. This process continues until the goal is reached or a time limit is met.

Question 2:
Looking into the consideration of being computationally efficient and presence of a complex environment, RRT algorithms are well suited for UAV navigation. Since it is built on sampling points and tree structures, it is adaptable to changing environments and hence complex situations could be handled well using RRT.
Lifelong Planning A* (LPA*) is also another viable algorithm which can be used in rapidly changing environments. It excels in re-planning the route, with minimal computational resource use for replanning the route. For UAVs in a smaller environment LPA* is a better algorithm than RRT, but in large environments some initial exploration is required by both the algorithm and RRT is better at it due to its random sampling approach. But a better optimal solution and efficient re-planning trades-off for this, and LPA* become a better choice.

Question 3:
