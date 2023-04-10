#!/usr/bin/env python
#Koki Itagaki
from typing import NamedTuple, Tuple, List, IO

"""A class to represent a color."""
class Colour(NamedTuple):
    """Colour class"""
    red: int
    green: int
    blue: int
    opac: float

"""A class to represent a shape."""
class Shape(NamedTuple):
    """Shape class"""
    x: int
    y: int
    colour: Colour

"""A class to represent a circle shape."""
class CircleShape(Shape):
    """CircleShape class"""
    r: int


"""Draw a circle shape with the specified parameters.

        Args:
        - f (IO[str]): A file object to write the SVG data to.
        - t (int): The number of spaces to indent the SVG data by.
"""
def draw_circle_line(self, f: IO[str], t: int) -> None:
        """draw_circle_line() method"""
        ts: str = "   " * t
        line1: str = f'<circle cx="{self.x}" cy="{self.y}" r="{self.r}" '
        line2: str = f'fill="rgb({self.colour.red}, {self.colour.green}, {self.colour.blue})" fill-opacity="{self.colour.opac}"/>'
        f.write(f"{ts}{line1+line2}\n")

"""A class to represent a rectangle shape."""
class RectangleShape(Shape):
    """RectangleShape class"""
    w: int
    h: int


"""Draw a rectangle shape with the specified parameters.

        Args:
        - f (IO[str]): A file object to write the SVG data to.
        - t (int): The number of spaces to indent the SVG data by.
"""
def draw_rect_line(self, f: IO[str], t: int) -> None:
        """draw_rect_line() method"""
        ts: str = "   " * t
        line1: str = f'<rect x="{self.x}" y="{self.y}" width="{self.w}" height="{self.h}" '
        line2: str = f'fill="rgb({self.colour.red}, {self.colour.green}, {self.colour.blue})" fill-opacity="{self.colour.opac}"/>'
        f.write(f"{ts}{line1+line2}\n")

"""A class to represent an ellipse."""
class Ellipse(NamedTuple):
    """Ellipse class"""
    x: int
    y: int
    rx: int
    ry: int

"""A class to represent an ellipse shapes."""
class EllipseShape(Shape):
    """EllipseShape class"""
    rx: int
    ry: int


"""Draw an ellipse shape with the specified parameters.

        Args:
        - f (IO[str]): A file object to write the SVG data to.
        - t (int): The number of spaces to indent the SVG data by.
"""
def draw_ellipse_line(self, f: IO[str], t: int) -> None:
        """draw_ellipse_line() method"""
        ts: str = "   " * t
        line1: str = f'<ellipse cx="{self.x}" cy="{self.y}" rx="{self.rx}" ry="{self.ry}" '
        line2: str = f'fill="rgb({self.colour.red}, {self.colour.green}, {self.colour.blue})" fill-opacity="{self.colour.opac}"/>'
        f.write(f"{ts}{line1+line2}\n")

"""A class to represent an SVG canvas."""
class SvgCanvas:
    """SvgCanvas class"""


    """Create a new SVG canvas with the specified width and height.

        Args:
        - w (int): The width of the canvas.
        - h (int): The hight of the canvas.
    """
    def __init__(self, w: int, h: int) -> None:
        self.w: int = w
        self.h: int = h
        self.shapes: List[Shape] = []


    """Add a shape to the SVG canvas.
    Args:
    - shape (Shape): The shape to add to the canvas.
    """
    def add_shape(self, s: Shape) -> None:
        """add_shape() method"""
        self.shapes.append(s)



    """Get the SVG data for the current state of the canvas.
    Returns:
    - str: The SVG data for the current state of the canvas.
    """
    def gen_art(self, f: IO[str], t: int) -> None:
        """gen_art() method"""
        ts: str = "   " * t
        f.write(f'{ts}<svg viewBox="0 0 {self.w} {self.h}" xmlns="http://www.w3.org/2000/svg">\n')
        for shape in self.shapes:
            if isinstance(shape, CircleShape):
                shape.draw_circle_line(f, t+1)
            elif isinstance(shape, RectangleShape):
                shape.draw_rect_line(f, t+1)
            elif isinstance(shape, EllipseShape):
                shape.draw_ellipse_line(f, t+1)
        f.write(f"{ts}</svg>\n")



"""Represents an HTML document"""
class HtmlDocument:
    """HtmlDocument class"""


    """
        Initializes an HtmlDocument instance.

        Args:
        - title (str): the title of the HTML document

        Returns: None
    """
    def __init__(self, title: str) -> None:
        self.title: str = title
        self.canvas_list: List[SvgCanvas] = []

    """
        Adds an SvgCanvas instance to the canvas_list of this HtmlDocument instance.

        Args:
        - c (SvgCanvas): the SvgCanvas instance to be added

        Returns: None
    """
    def add_canvas(self, c: SvgCanvas) -> None:
        """add_canvas() method"""
        self.canvas_list.append(c)

"""Represents a circle"""
class Circle:
    """Circle class"""


    """
        Initializes a Circle instance.

        Args:
        - cir (Tuple[int, int, int]): a tuple containing the x and y coordinates of the center
            of the circle and the radius of the circle
        - col (Tuple[int, int, int, float]): a tuple containing the RGB color values of the
            circle and the opacity of the fill

        Returns: None
    """
    def __init__(self, cir: Tuple[int, int, int], col: Tuple[int, int, int, float]) -> None:
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]


"""
    Writes an HTML comment to the file.

    Args:
    - f (IO[str]): the file to write to
    - t (int): the number of tabs to insert before the comment
    - com (str): the text of the comment

    Returns: None
"""
def writeHTMLcomment(f: IO[str], t: int, com: str) -> None:
    """writeHTMLcomment() method"""
    ts: str = "   " * t
    f.write(f"{ts}<!--{com}-->\n")



"""
    Writes an SVG circle to the file.

    Args:
    - f (IO[str]): the file to write to
    - t (int): the number of tabs to insert before the circle
    - c (Circle): the Circle instance to be drawn

    Returns: None
"""
def drawCircleLine(f: IO[str], t: int, c: Circle) -> None:
    """drawCircle() method"""
    ts: str = "   " * t
    line1: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" '
    line2: str = f'fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
    f.write(f"{ts}{line1+line2}\n")



"""
    Generates an SVG art and writes it to the file.

    Args:
    - f (IO[str]): the file to write to
    - t (int): the number of tabs to insert before the art

    Returns: None
"""
def genArt(f: IO[str], t: int) -> None:
    """genART() method"""
    drawCircleLine(f, t, Circle((50,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((150,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((250,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((350,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((450,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((50,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((150,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((250,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((350,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((450,250,50), (0,0,255,1.0)))



"""
    Open an SVG drawing box in the given file handle with the given indentation level and dimensions.

    Args:
        f (IO[str]): The file handle to write to.
        t (int): The level of indentation to use.
        canvas (Tuple[int, int]): A tuple containing the width and height of the canvas.

    Returns:
        None.
"""
def openSVGcanvas(f: IO[str], t: int, canvas: Tuple[int, int]) -> None:
    """openSVGcanvas() method"""
    ts: str = "   " * t
    writeHTMLcomment(f, t, "Define SVG drawing box")
    f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')


"""
    Close an SVG drawing box in the given file handle with the given indentation level.

    Args:
        f (IO[str]): The file handle to write to.
        t (int): The level of indentation to use.

    Returns:
        None.
"""
def closeSVGcanvas(f: IO[str], t: int) -> None:
    """closeSVGcanvas() method"""
    ts: str = "   " * t
    f.write(f"{ts}</svg>\n")
    f.write(f"</body>\n")
    f.write(f"</html>\n")




"""
    Write an HTML line to the given file handle with the given indentation level.

    Args:
        f (IO[str]): The file handle to write to.
        t (int): The level of indentation to use.
        line (str): The HTML line to write.

    Returns:
        None.
"""
def writeHTMLline(f: IO[str], t: int, line: str) -> None:
    """writeLineHTML() method"""
    ts: str = "   " * t
    f.write(f"{ts}{line}\n")


"""
    Write the HTML header to the given file handle with the given window title.

    Args:
        f (IO[str]): The file handle to write to.
        winTitle (str): The title to use for the HTML window.

    Returns:
        None.
"""
def writeHTMLHeader(f: IO[str], winTitle: str) -> None:
    """writeHeadHTML() method"""
    writeHTMLline(f, 0, "<html>")
    writeHTMLline(f, 0, "<head>")
    writeHTMLline(f, 1, f"<title>{winTitle}</title>")
    writeHTMLline(f, 0, "</head>")
    writeHTMLline(f, 0, "<body>")

import os


"""
    Write an HTML file containing an SVG drawing.

    Returns:
        None.
"""
def writeHTMLfile() -> None:
    """writeHTMLfile() method"""
    dir_path: str = "./a41/"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    fnam: str = os.path.join(dir_path, "a41.html")
    winTitle: str = "My Art"
    f: IO[str] = open(fnam, "w")
    writeHTMLHeader(f, winTitle)
    openSVGcanvas(f, 1, (500,300))
    genArt(f, 2)
    closeSVGcanvas(f, 1)
    f.close()



"""Main function that generates an HTML file with an SVG drawing.

    Calls the writeHTMLfile function to generate an HTML file, which includes an SVG drawing.
"""
def main() -> None:
    """main() method"""
    writeHTMLfile()

if __name__ == "__main__":
    main()
