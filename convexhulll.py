import matplotlib.pyplot as plt
from radicalcomp import RadialComparator, Orientation
import random
from vertex import Vertex
from functools import cmp_to_key


class ConvexHull:
    def __init__(self, vertices: list):
        '''vertices: list of Vertex'''
        self.vertices = vertices

    def convex_chain(self):
        '''Finds the convex hull. 
        Returns all the points on the hull. '''
        anchor = self.__findAnchor()
        S = self.__sort_remaining(anchor)
        return self.__scan(S, anchor)

    def __findAnchor(self):
        '''Finds the anchor point.
        Returns the anchor point as Vertex'''
        v_with_min_x = min(self.vertices, key=lambda v: v.x)

        repeated_min_x = [v for v in self.vertices if v.x <= v_with_min_x.x]

        if len(repeated_min_x) == 1:
            return v_with_min_x

        return min(repeated_min_x, key=lambda v: v.y)

    def __sort_remaining(self, anchor):
        '''Returns a sorted list of vertices. 
        Anchor point is placed in the front and in the back. '''
        vertices = [v for v in self.vertices if v != anchor]
        S = sorted(vertices, key=cmp_to_key(
            RadialComparator(anchor).comp), reverse=True)
        S.insert(0, anchor)
        S.append(anchor)
        return S

    def __scan(self, S: list, a: Vertex):
        '''Execute phase 3 of Graham Scan Algorithm. '''
        H = S[:2]
        for r in S[2:]:
            p,q = H[-2:]
            while RadialComparator(p).comp(q,r) != Orientation.CCW:
                del H[-1] #Deletion of last element in python list is O(1)
                p,q = H[-2:]
            H.append(r)
        return H


    def draw(self, hull):
        '''Draw the convex hull on a plot.
        Green line is the hull'''
        hull.append(hull[0])
        plt.plot([v.x for v in self.vertices], [
                 v.y for v in self.vertices], "r.")
        plt.plot([v.x for v in hull], [v.y for v in hull], 'g-')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.savefig(fname="plot.pdf")

    def solution(self):
        '''Solve the problem and draw the illustration.'''
        self.draw(self.convex_chain())

    @classmethod
    def random_points(self, n):
        '''Produce n random Verices with 0 <= x,y <= 100'''
        return [Vertex(random.randint(0, 100), random.randint(0, 100)) for i in range(n)]

if __name__ == "__main__":
    '''driver'''
    i = int(input("Please enter the amount of points to generate: "))
    ConvexHull(ConvexHull.random_points(i)).solution()
    print("The result is saved as plot.pdf")
