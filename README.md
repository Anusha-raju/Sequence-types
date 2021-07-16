# Session 10 - Sequence Types- I

## ASSIGNMENT



1. A regular strictly convex polygon is a polygon that has the following characteristics:
   1. all interior angles are less than 180
   2. all sides have equal length
2. For a regular strictly convex polygon with:
   - **n** edges (=n vertices)
   - **R** circumradius
   - interiorAngle=(n−2)⋅180/n
   - edgeLength,s=2⋅R⋅sin⁡(π/n)
   - apothem,a=R⋅cos⁡(π/n)
   - area=0.5⋅n⋅s⋅a
   - perimeter=n⋅s
3. Objective 1 :
   1. Create a Polygon Class:
      1. where initializer takes in:
         1. number of edges/vertices
         2. circumradius
      2. that can provide these properties:
         1. \# edges
         2. \# vertices
         3. interior angle
         4. edge length
         5. apothem
         6. area
         7. perimeter
      3. that has these functionalities:
         1. a proper __repr__ function
         2. implements equality (==) based on # vertices and circumradius (__eq__)
         3. implements > based on number of vertices only (__gt__)
   2. Objective 2 :
      1. Implement a Custom Polygon sequence type:
         1. where initializer takes in:
            1. number of vertices for largest polygon in the sequence
            2. common circumradius for all polygons
         2. that can provide these properties:
            1. max efficiency polygon: returns the Polygon with the highest **area: perimeter** ratio
         3. that has these functionalities:
            1. functions as a sequence type (__getitem__)
            2. supports the len() function (__len__)
            3. has a proper representation (__repr__)









## Solution



#### Objective 1

```
import math

class Polygon:
    """
    This is a class which generates a regular strict convex polygon with desired vertex 	and circumradius
    """

    def __init__(self,no_of_edges:int,circumradius:float)->None:
        """
        This is a constructor which initialises the number of edges/vertices and       			circumradius
        """
        
        if no_of_edges<3:
            raise ValueError("Number of edges/vertices should be equal to or greater than 								3(Three)")

        self.no_of_edges = no_of_edges
        self.circumradius = circumradius


    def __repr__(self)->str:
        """
        This is a representation function
        """
        return f'This is a polygon of {self.no_of_edges} edges with circumradius: 																		{self.circumradius}'

    @property
    def interior_angle(self)->float:
        """
        This is a function which calculates the interior angle
        """

        return (self.no_of_edges - 2)*(180/self.no_of_edges)

    @property
    def edge_length(self)->float:
        """
        This is a function which calculates the edge length of the polygon
        """

        return (2*self.circumradius)*math.sin(math.pi/self.no_of_edges)

    @property
    def apothem(self)->float:
        """
        This is a function which calculates the apothem of the polygon
        """

        return self.circumradius*math.cos(math.pi/self.no_of_edges)

    @property
    def area(self)->float:
        """
        This is a function which calculates the area of the polygon

        """

        return 0.5*self.no_of_edges*self.apothem*self.edge_length

    @property
    def perimeter(self)->float:
        """
        This is a function which calculates the perimeter of the polygon

        """
        return self.no_of_edges*self.edge_length

    def __eq__(self, other:'Polygon class')->bool:
        """
        This is a equal to (==) function which checks for the number of edges and 				circumradius
        """

        if isinstance(other, Polygon):
            return True if self.no_of_edges==other.no_of_edges and self.circumradius == 					other.circumradius else False
        else:
            raise TypeError("This operation can be performed only with two polygon type 																			objects")

    def __gt__(self, other:'Polygon class')->bool:
        """
        This is a greater than function which calculates based on number of edges.
        """
        if isinstance(other, Polygon):
            return True if self.no_of_edges > other.no_of_edges else False
        else:
            raise TypeError("This operation can be performed only with two polygon type 																			objects")
```





#### Objective 2

```
from polygon import Polygon as poly

class Polygon_sequence:
    """
    This is a polygon sequence class used to develop a custom sequence
    """
    def __init__(self,highest_no_of_edges:int,circumradius:float)->None:
        """
        This is a constructor which initialises the highest number of edges/vertices and 																			circumradius
        """
        if highest_no_of_edges<3:
            raise ValueError("Number of edges/vertices should be equal to or greater than 																				3(Three)")

        self.highest_no_of_edges = highest_no_of_edges
        self.circumradius = circumradius
        self.sequence = [poly(n, self.circumradius) for n in range(3,self.highest_no_of_edges+1)]

    def __repr__(self)->str:
        """
        This is a representation function
        """
        return f'This is a polygon sequence of {self.highest_no_of_edges-2} elements with 				{self.highest_no_of_edges} as highest edge with common circumradius: 											{self.circumradius}'


    def __len__(self)->int:
        """
        This is a length function
        """
        return self.highest_no_of_edges - 2

    def __getitem__(self, vertex)->float:
        """
        This function returns the element of the sequence in  the desired vertex
        """
        if isinstance(vertex, int):
            if vertex < 0:
                vertex = self.no_edges + vertex
            if vertex < 0 or vertex >= self.highest_no_of_edges:
                raise IndexError
            else:
                return self.sequence[vertex]
        else:
            start, stop, step = vertex.indices(self.highest_no_of_edges)
            rng = range(start, stop, step)
            return [self.sequence[i] for i in rng]


    @property
    def max_efficieny(self)->str:
        """
        This function calculates the maximum_efficieny

        """
        ratios = [p.area/p.perimeter for p in self.sequence]
        maximum_efficieny = max(ratios)
        index = ratios.index(maximum_efficieny)+3
        print(ratios)
        return f"maximum efficient polygon is/n Number of edges :{index} /n 													maximum_efficieny is {maximum_efficieny}"
```

