import math

class Polygon:
    """
    This is a class which generates a regular strict convex polygon with desired vertex and circumradius
    """

    def __init__(self,no_of_edges:int,circumradius:float)->None:
        """
        This is a constructor which initialises the number of edges/vertices and circumradius
        """
        if no_of_edges<3:
            raise ValueError("Number of edges/vertices should be equal to or greater than 3(Three)")

        self.no_of_edges = no_of_edges
        self.circumradius = circumradius


    def __repr__(self)->str:
        """
        This is a representation function
        """
        return f'This is a polygon of {self.no_of_edges} edges with circumradius: {self.circumradius}'

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
        This is a equal to (==) function which checks for the number of edges and circumradius
        """

        if isinstance(other, Polygon):
            return True if self.no_of_edges==other.no_of_edges and self.circumradius == other.circumradius else False
        else:
            raise TypeError("This operation can be performed only with two polygon type objects")

    def __gt__(self, other:'Polygon class')->bool:
        """
        This is a greater than function which calculates based on number of edges.
        """
        if isinstance(other, Polygon):
            return True if self.no_of_edges > other.no_of_edges else False
        else:
            raise TypeError("This operation can be performed only with two polygon type objects")