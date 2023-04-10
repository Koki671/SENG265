#!/usr/bin/env python
#Koki Itagaki
from typing import NamedTuple, Tuple, List, IO
import random
from collections import namedtuple
import random as r
import collections

"""A class to represent a color and this is for type hints."""
class Colour(NamedTuple):
    """Colour class"""
    red: int
    green: int
    blue: int
    opac: float

"""A class to represent a shape and this is for type hints."""
class Shape(NamedTuple):
    """Shape class"""
    x: int
    y: int
    colour: Colour

"""A class to represent a shape and this is for type hints."""
class CircleShape(Shape):
    """CircleShape class"""
    r: int




    """Draws a line of SVG code to represent the circle.

        Args:
        - f (IO[str]): a file object to write the SVG code to
        - t (int): the indentation level for the generated SVG code
    """
    def draw_circle_line(self, f: IO[str], t: int) -> None:
        """draw_circle_line() method"""
        ts: str = "   " * t
        line1: str = f'<circle cx="{self.x}" cy="{self.y}" r="{self.r}" '
        line2: str = f'fill="rgb({self.colour.red}, {self.colour.green}, {self.colour.blue})" fill-opacity="{self.colour.opac}"/>'
        f.write(f"{ts}{line1+line2}\n")

"""A class to represent a rectangle shape, and this is for type hints"""
class RectangleShape(Shape):
    """RectangleShape class"""
    w: int
    h: int



    """Draws a line of SVG code to represent the rectangle.

        Args:
        - f (IO[str]): a file object to write the SVG code to
        - t (int): the indentation level for the generated SVG code
    """
    def draw_rect_line(self, f: IO[str], t: int) -> None:
        """draw_rect_line class"""
        ts: str = "   " * t
        line1: str = f'<rect x="{self.x}" y="{self.y}" width="{self.w}" height="{self.h}" '
        line2: str = f'fill="rgb({self.colour.red}, {self.colour.green}, {self.colour.blue})" fill-opacity="{self.colour.opac}"/>'
        f.write(f"{ts}{line1+line2}\n")

"""
The Ellipse class represents an ellipse. It inherits from the NamedTuple class.

Args:
x (int): the x-coordinate of the ellipse's center.
y (int): the y-coordinate of the ellipse's center.
rx (int): the horizontal radius of the ellipse.
ry (int): the vertical radius of the ellipse.
"""
class Ellipse(NamedTuple):
    """Ellipse class"""
    x: int
    y: int
    rx: int
    ry: int


"""
The EllipseShape class represents an ellipse shape. It inherits from the Shape class.

Args:
None
"""
class EllipseShape(Shape):
    """EllipseShape class"""
    rx: int
    ry: int




    """
    This method generates an SVG representation of the ellipse on the canvas.

    Args:
    f (IO[str]): a file object to write the SVG image to.
    t (int): the indentation level for the generated SVG code.
    Returns:
    None.
    """

    def draw_ellipse_line(self, f: IO[str], t: int) -> None:
            """draw_ellipse_line class"""
            ts: str = "   " * t
            line1: str = f'<ellipse cx="{self.x}" cy="{self.y}" rx="{self.rx}" ry="{self.ry}" '
            line2: str = f'fill="rgb({self.colour.red}, {self.colour.green}, {self.colour.blue})" fill-opacity="{self.colour.opac}"/>'
            f.write(f"{ts}{line1+line2}\n")

"""
The SvgCanvas class represents an SVG canvas.

Arguments:
w (int): the width of the canvas in pixels.
h (int): the height of the canvas in pixels.
"""
class SvgCanvas:
    """SvgCanvas class"""


    """Constructor for SvgCanvas class.

        Args:
        - w (int): width of the canvas in pixels
        - h (int): height of the canvas in pixels
    """
    def __init__(self, w: int, h: int) -> None:
        """__init__ class"""
        self.w = w
        self.h = h
        self.shapes: List[Shape] = []



    """Adds a Shape object to the list of shapes on the canvas.

        Args:
        - s (Shape): a Shape object to add to the canvas
    """
    def add_shape(self, s: Shape) -> None:
        """add_shape class"""
        self.shapes.append(s)




    """Generates an SVG image of the canvas with the shapes drawn on it.

        Args:
        - f (IO[str]): a file object to write the SVG image to
        - t (int): the indentation level for the generated SVG code
    """
    def gen_art(self, f: IO[str], t: int) -> None:
        """gen_art() method"""
        ts: str = "   " * t
        f.write(f"{ts}<svg viewBox='0 0 {self.w} {self.h}' xmlns='http://www.w3.org/2000/svg'>\n")
        for shape in self.shapes:
            if isinstance(shape, CircleShape):
                shape.draw_circle_line(f, t + 1)
            elif isinstance(shape, RectangleShape):
                shape.draw_rect_line(f, t + 1)
            elif isinstance(shape, EllipseShape):
                shape.draw_ellipse_line(f, t + 1)
        f.write(f"{ts}</svg>\n")


class HtmlDocument:
    """HtmlDocument class"""
    def __init__(self, title: str, head: List[str] = None):
        """__init__() method"""
        self.title = title
        self.head = head or []
        self.body = []



    """
    This method adds an HTML head tag to the list of head tags.

    Args:
    tag (str): an HTML head tag to add to the list of head tags.
    """
    def add_head_tag(self, tag: str) -> None:
        """add_head_tag() method"""
        self.head.append(tag)


    """
    This method adds an HTML body tag to the list of body tags.

    Arguments:
    tag (str): an HTML body tag to add to the list of body tags.
    Returns:
    None.
    """
    def add_body_tag(self, tag: str) -> None:
        """add_body_tag() method"""
        self.body.append(tag)




    
    """
    The gen_html() method generates an HTML file with random shapes rendered using the SvgCanvas class from the svg_canvas.py module. The generated file is saved in the ./a43 directory with the given file_name.

    Arguments:

    file_name (str): The name of the file to be generated.
    t (int): The number of tabs (4 spaces) to use for indentation in the generated HTML file.
    Returns:

    None
    """

    def gen_html(self, file_name: str, t: int) -> None:
        """gen_html() method"""
        file_path = f"./a43/{file_name}"
        ts: str = "   " * t
        with open(file_path, 'w') as f:
            f.write(f"{ts}<!DOCTYPE html>\n")
            f.write(f"{ts}<html>\n")
            f.write(f"{ts}<head>\n")
            f.write(f"{ts}   <title>{self.title}</title>\n")
            for tag in self.head:
                f.write(f"{ts}   {tag}\n")
            f.write(f"{ts}</head>\n")
            f.write(f"{ts}<body>\n")
            f.write(f"{ts}   <div>\n")
            canvas = SvgCanvas(500, 500)
            for i in range(500):
                shape_type = random.choice(["circle", "rectangle", "ellipse"])
                if shape_type == "circle":
                    x = random.randint(50, 450)
                    y = random.randint(50, 450)
                    r = random.randint(10, 50)
                    red = random.randint(0, 255)
                    green = random.randint(0, 255)
                    blue = random.randint(0, 255)
                    opac = random.uniform(0.2, 0.8)
                    canvas.add_shape(CircleShape(x, y, Colour(red, green, blue, opac), r))
                elif shape_type == "rectangle":
                    x = random.randint(50, 450)
                    y = random.randint(50, 450)
                    w = random.randint(10, 50)
                    h = random.randint(10, 50)
                    red = random.randint(0, 255)
                    green = random.randint(0, 255)
                    blue = random.randint(0, 255)
                    opac = random.uniform(0.2, 0.8)
                    canvas.add_shape(RectangleShape(x, y, Colour(red, green, blue, opac), w, h))
                elif shape_type == "ellipse":
                    x = random.randint(50, 450)
                    y = random.randint(50, 450)
                    rx = random.randint(10, 50)
                    ry = random.randint(10, 50)
                    red = random.randint(0, 255)
                    green = random.randint(0, 255)
                    blue = random.randint(0, 255)
                    opac = random.uniform(0.2, 0.8)
                    canvas.add_shape(EllipseShape(x, y, Colour(red, green, blue, opac), rx, ry))

            canvas.gen_art(f, t + 1)

            f.write(f"{ts}   </div>\n")
            f.write(f"{ts}</body>\n")
            f.write(f"{ts}</html>\n")



"""
Args:
- r (int): Red value (0-255)
- g (int): Green value (0-255)
- b (int): Blue value (0-255)
- a (float): Alpha value (0-1)

Returns:
- None
"""
class Colour:
    """Colour class"""
    def __init__(self, r: int, g: int, b: int, a: float):
        self.r = r
        self.g = g
        self.b = b
        self.a = a


    """
    Returns a string representation of the colour in RGBA format
    """
    def __str__(self) -> str:
        """__str__() method"""
        return f"rgba({self.r}, {self.g}, {self.b}, {self.a})"






"""
Args:
- x (int): x-coordinate of the shape
- y (int): y-coordinate of the shape
- colour (Colour): Colour of the shape

Returns:
- None
"""
class Shape:
    """Shape class"""
    def __init__(self, x: int, y: int, colour: Colour):
        """__init__() method"""
        self.x = x
        self.y = y
        self.colour = colour



    """
    Returns a string representation of the shape in SVG format
    """
    def __str__(self) -> str:
        """__str__() method"""
        return f"fill:{self.colour};"





"""
Args:
- x (int): x-coordinate of the center of the circle
- y (int): y-coordinate of the center of the circle
- colour (Colour): Colour of the circle
- r (int): Radius of the circle

Returns:
- None
"""
class CircleShape(Shape):
    """CircleShape class"""
    def __init__(self, x: int, y: int, colour: Colour, r: int):
        """__init__() method"""
        super().__init__(x, y, colour)
        self.r = r

    """
    Returns a string representation of the circle in SVG format
    """
    def __str__(self) -> str:
        """__str__() method"""

        return f"<circle cx=\"{self.x}\" cy=\"{self.y}\" r=\"{self.r}\" style=\"{super().__str__()}\" />"






"""  Rectangle Shape class
Args:
- x (int): x-coordinate of the top left corner of the rectangle
- y (int): y-coordinate of the top left corner of the rectangle
- colour (Colour): Colour of the rectangle
- w (int): Width of the rectangle
- h (int): Height of the rectangle

Returns:
- None
"""
class RectangleShape(Shape):
    """RectangleShape class"""
    def __init__(self, x: int, y: int, colour: Colour, w: int, h: int):
        super().__init__(x, y, colour)
        self.w = w
        self.h = h

    def __str__(self) -> str:
        return f"<rect x=\"{self.x}\" y=\"{self.y}\" width=\"{self.w}\" height=\"{self.h}\" style=\"{super().__str__()}\" />"


"""
Ellipse Shape class
Args:
- x (int): x-coordinate of the center of the ellipse
- y (int): y-coordinate of the center of the ellipse
- colour (Colour): Colour of the ellipse
- rx (int): X-radius of the ellipse
- ry (int): Y
"""
class EllipseShape(Shape):
    """EllipseShape class"""
    def __init__(self, x: int, y: int, colour: Colour, rx: int, ry: int):
        super().__init__(x, y, colour)
        self.rx = rx
        self.ry = ry

    def __str__(self) -> str:
        """__str__() method"""
        return f"<ellipse cx=\"{self.x}\" cy=\"{self.y}\" rx=\"{self.rx}\" ry=\"{self.ry}\" style=\"{super().__str__()}\" />"

"""
SvgCanvas class
This class represents an SVG canvas and holds a list of shapes to be drawn on the canvas.
"""
class SvgCanvas:
    """SvgCanvas class"""


    """
    Initializes the SvgCanvas object with the given width and height.
    Arg:
    width : int : The width of the canvas.
    height : int : The height of the canvas.
    """
    def __init__(self, width: int, height: int):
        """__init__() method"""
        self.width = width
        self.height = height
        self.shapes = []


    """
    Adds a shape to the list of shapes to be drawn on the canvas.
    Args:
    shape : Shape : The shape object to be added to the canvas.
    """
    def add_shape(self, shape: Shape) -> None:
        """Add_shape() method"""
        self.shapes.append(shape)


    """
    Generates the SVG art and writes it to the given IO stream.

    Args:
    f : IO[str] : The IO stream to which the SVG art will be written.
    t : int : The indentation level of the SVG elements in the output.
    Return Type: None.
"""
    def gen_art(self, f: IO[str], t: int) -> None:
        """gen_art() method"""
        ts: str = "   " * t
        f.write(f"{ts}<svg width=\"{self.width}\" height=\"{self.height}\">\n")
        for shape in self.shapes:
            f.write(f"{ts}   {shape}\n")
        f.write(f"{ts}</svg>\n")



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




    """
    This method returns a string representation of the configuration of the SVG image.
    The output format is as follows:
    
    CNT SHA X Y RAD RX RY W H R G B OP
    
    where:
    - CNT: the number of the shape in the SVG image
    - SHA: the type of shape (0 = circle, 1 = rectangle, 2 = ellipse)
    - X: the x-coordinate of the center of the shape
    - Y: the y-coordinate of the center of the shape
    - RAD: the radius of the shape (if SHA = 0)
    - RX: the x-radius of the shape (if SHA = 1 or 2)
    - RY: the y-radius of the shape (if SHA = 1 or 2)
    - W: the width of the shape (if SHA = 1 or 2)
    - H: the height of the shape (if SHA = 1 or 2)
    - R: the red component of the shape's color
    - G: the green component of the shape's color
    - B: the blue component of the shape's color
    - OP: the opacity of the shape's color
    """
    def __str__(self) -> str:
        """"__str__() method"""
        header:str = f'{"CNT":>3} {"SHA":>3} {"X":>3} {"Y":>3} {"RAD":>3} {"RX":>3} {"RY":>3} {"W":>3} {"H":>3} {"R":>3} {"G":>3} {"B":>3} {"OP":>3}\n'
        parts:str= [self.line(i) for i in range(self.config.max_cnt)]
        return header + '\n'.join(parts)


    """
    This is the main entry point for the program. It generates three SVG images with different
    configurations using the HtmlDocument class.
    """
def main() -> None:
    """main() method"""
    random.seed(1234)
    doc = HtmlDocument("My Document", ["<meta charset='UTF-8'>"])
    doc.gen_html("a431.html", 2)
    doc.gen_html("a432.html", 0)
    doc.gen_html("a433.html", 10)

if __name__ == "__main__":
    main()
