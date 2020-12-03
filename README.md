# GrahamConvexHull
Implemens Graham Scan Algorithm.

Use the Vertex class to construct a vertex.

Direct Usage:
User will be prompt for the number of vertices to generate and vertices will be generated and plotted. 
    python convexhull.py

Use as module:
    points = [Vertex(1,5), Vertex(8,85), Vertex(64,88), Vertex(99,31), Vertex(0, 0)]
    ConvexHull(points).solution()


#Or to generate random points
    points = ConvexHull.random(20)
    ConvexHull(points).solution()
