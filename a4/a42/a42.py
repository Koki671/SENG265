#!/usr/bin/env python
#kokiitsgski
from typing import IO
from collections import namedtuple
import random as r
import collections
from typing import Dict, Tuple

# Define named tuples
cnt = collections.namedtuple('cnt', 'min max')  # cnt: Tuple[int, int]
sha = collections.namedtuple('sha', 'min max')  # sha: Tuple[int, int]
coord = collections.namedtuple('coord', 'x_min x_max y_min y_max')  # coord: Tuple[int, int, int, int]
rad = collections.namedtuple('rad', 'min max')  # rad: Tuple[int, int]
eli_rad = collections.namedtuple('eli_rad', 'rx_min rx_max ry_min ry_max')  # eli_rad: Tuple[int, int, int, int]
rec_dim = collections.namedtuple('rec_dim', 'w_min w_max h_min h_max')  # rec_dim: Tuple[int, int, int, int]
red = collections.namedtuple('red', 'min max')  # red: Tuple[int, int]
green = collections.namedtuple('green', 'min max')  # green: Tuple[int, int]
blue = collections.namedtuple('blue', 'min max')  # blue: Tuple[int, int]
opac = collections.namedtuple('opac', 'min max')  # opac: Tuple[float, float]

col = collections.namedtuple('col', 'red green blue opac')  # col: Tuple[int, int, int, float]
cir = collections.namedtuple('cir', 'x y radius')  # cir: Tuple[int, int, int]
rec = collections.namedtuple('rec', 'x y h w')  # rec: Tuple[int, int, int, int]
eli = collections.namedtuple('eli', 'x y rx ry')  # eli: Tuple[int, int, int, int]





"""
        PyArtConfig is a class for holding the configuration parameters for the PyArt graphics library.

        Parameters:
        count (namedtuple): A namedtuple containing the minimum and maximum values for the count parameter.
        shape (namedtuple): A namedtuple containing the minimum and maximum values for the shape parameter.
        coordinate (namedtuple): A namedtuple containing the minimum and maximum values for the x and y coordinates.
        radius (namedtuple): A namedtuple containing the minimum and maximum values for the radius parameter.
        eli_radius (namedtuple): A namedtuple containing the minimum and maximum values for the x and y radius parameters for ellipses.
        rec_dimensions (namedtuple): A namedtuple containing the minimum and maximum values for the width and height parameters for rectangles.
        c_red (namedtuple): A namedtuple containing the minimum and maximum values for the red color component.
        c_green (namedtuple): A namedtuple containing the minimum and maximum values for the green color component.
        c_blue (namedtuple): A namedtuple containing the minimum and maximum values for the blue color component.
        c_opac (namedtuple): A namedtuple containing the minimum and maximum values for the opacity parameter.
        max_cnt (int): The maximum number of shapes to generate.

        Returns:
        None
"""
class PyArtConfig:
    """PyArtConfig Class"""

    def __init__(self, count:namedtuple = cnt(0,10000), shape:namedtuple = sha(0,3), 
                 coordinate:namedtuple = coord(0,500,0,500), radius:namedtuple = rad(0,100),
                 eli_radius:namedtuple = eli_rad(10,30,10,30), rec_dimensions:namedtuple = rec_dim(0,100,0,100),
                 c_red:namedtuple = red(0,255), c_green:namedtuple = green(0,255),
                 c_blue:namedtuple = blue(0,255), c_opac:namedtuple = opac(0.0,1.0),max_cnt: int = 10) -> None:
        self.count = count
        self.shape = shape
        self.coordinate = coordinate
        self.radius = radius
        self.eli_radius = eli_radius
        self.rec_dimensions = rec_dimensions
        self.c_red = c_red
        self.c_green = c_green
        self.c_blue = c_blue
        self.c_opac = c_opac
        self.max_cnt =  max_cnt

class RandomShape:
    """RandomShape Class"""
    config: PyArtConfig = PyArtConfig(count = cnt(0,10))






    """
        line is a class method that generates a random line.

        Parameters:
        cnt (int): The index of the line.

        Returns:
        str: The generated line as a string.
    """
    @classmethod
    def line(cls, cnt:int) -> str:
        """line() method"""
        from typing import Dict, Tuple

        ranges: Dict[str, Tuple[int, int]] = {
                'sha': (cls.config.shape.min, cls.config.shape.max),
                'x': (cls.config.coordinate.x_min, cls.config.coordinate.x_max),
                'y': (cls.config.coordinate.y_min, cls.config.coordinate.y_max),
                'rad': (cls.config.radius.min, cls.config.radius.max),
                'rx': (cls.config.eli_radius.rx_min, cls.config.eli_radius.rx_max),
                'ry': (cls.config.eli_radius.ry_min, cls.config.eli_radius.ry_max),
                'w': (cls.config.rec_dimensions.w_min, cls.config.rec_dimensions.w_max),
                'h': (cls.config.rec_dimensions.h_min, cls.config.rec_dimensions.h_max),
                'R': (cls.config.c_red.min, cls.config.c_red.max),
                'G': (cls.config.c_green.min, cls.config.c_green.max),
                'B': (cls.config.c_blue.min, cls.config.c_blue.max),
                'OP': (cls.config.c_opac.min, cls.config.c_opac.max)
            }

        values = [f"{cnt:>3}"]
        for param, (min_val, max_val) in ranges.items():
            value = r.randint(min_val, max_val) if param != 'OP' else r.uniform(min_val, max_val)
            if param == 'OP':
                values.append(f"{value:.1f}")
            else:
                values.append(f"{value:>3}")
        return " ".join(values)
    



    """
    This method reads in the contents of the file object f and generates an SVG image
    based on the configuration parameters contained in the file. The image is written
    to a file. The parameter t specifies the maximum number of shapes
    to include in the image.
    """
    @classmethod
    def svg(cls, f:IO[str], t:int)->None:
        """svg() method"""
        string:str = cls.line()
        vals:tuple = tuple(map(float, string.split()))
        
        shape:int = vals[1]
        colour:col = col(int(vals[9]), int(vals[10]), int(vals[11]), int(vals[12]))

        shapes = {
        0: cir(int(vals[2]), int(vals[3]), int(vals[4])),
        1: rec(int(vals[2]), int(vals[3]), int(vals[7]), int(vals[8])),
        2: eli(int(vals[2]), int(vals[3]), int(vals[5]), int(vals[6]))
}

        selected_shape = shapes.get(shape, None)


    def __str__(self) -> str:
        """"__str__() method"""
        header:str = f'{"CNT":>3} {"SHA":>3} {"X":>3} {"Y":>3} {"RAD":>3} {"RX":>3} {"RY":>3} {"W":>3} {"H":>3} {"R":>3} {"G":>3} {"B":>3} {"OP":>3}\n'
        parts:str= [self.line(i) for i in range(self.config.max_cnt)]
        return header + '\n'.join(parts)




def main() -> None:
    """Main() method"""
    shape_table = RandomShape()
    print(shape_table)


if __name__ == "__main__":
    main()