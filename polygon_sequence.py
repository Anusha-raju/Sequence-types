from polygon import Polygon as poly

class Polygon_sequence:
    """
    This is a polygon sequence class used to develop a custom sequence
    """
    def __init__(self,highest_no_of_edges:int,circumradius:float)->None:
        """
        This is a constructor which initialises the highest number of edges/vertices and circumradius
        """
        if highest_no_of_edges<3:
            raise ValueError("Number of edges/vertices should be equal to or greater than 3(Three)")

        self.highest_no_of_edges = highest_no_of_edges
        self.circumradius = circumradius
        self.sequence = [poly(n, self.circumradius) for n in range(3,self.highest_no_of_edges+1)]
        self.ratios = [p.area/p.perimeter for p in self.sequence]


    def __repr__(self)->str:
        """
        This is a representation function
        """
        return f'This is a polygon sequence of {self.highest_no_of_edges-2} elements with {self.highest_no_of_edges} as highest edge with common circumradius: {self.circumradius}'


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
    def max_efficiency(self)->str:
        """
        This function calculates the maximum_efficieny:highest area/perimeter ratio

        """
        maximum_efficieny = max(self.ratios)
        index = self.ratios.index(maximum_efficieny)+3
        return f"maximum efficient polygon is Number of edges :{index} maximum_efficieny is {maximum_efficieny}"