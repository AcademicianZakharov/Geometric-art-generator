#!/usr/bin/env python
"""Assignment 4 Part 1 template"""

from typing import IO
import random
from tabulate import tabulate
from doctest import testmod


class ProEpiloge:
    """Prolouge and Epilouge class"""
    def writeHTMLfile() -> None:
        """writeHTMLfile method"""
        fnam: str = "myPart3Art.html"
        winTitle = "My Art"
        maxx :int = 500
        maxy :int = 500
        f: IO[str] = open(fnam, "w")
        ProEpiloge.writeHTMLHeader(f, winTitle)
        ProEpiloge.openSVGcanvas(f, 1, (maxx,maxy))
        ProEpiloge.genArt(f, 2)
        ProEpiloge.closeSVGcanvas(f, 1)
        f.close()

    def writeHTMLHeader(f: IO[str], winTitle: str) -> None:
        """writeHeadHTML method"""
        ProEpiloge.writeHTMLline(f, 0, "<html>")
        ProEpiloge.writeHTMLline(f, 0, "<head>")
        ProEpiloge.writeHTMLline(f, 1, f"<title>{winTitle}</title>")
        ProEpiloge.writeHTMLline(f, 0, "</head>")
        ProEpiloge.writeHTMLline(f, 0, "<body>") 
        
    def openSVGcanvas(f: IO[str], t: int, canvas: tuple) -> None:
        """openSVGcanvas method"""
        ts: str = "   " * t
        ProEpiloge.writeHTMLcomment(f, t, "Define SVG drawing box")
        f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

    def closeSVGcanvas(f: IO[str], t: int) -> None:
        """closeSVGcanvas method"""
        ts: str = "   " * t
        f.write(f"{ts}</svg>\n")
        f.write(f"</body>\n")
        f.write(f"</html>\n")

    def writeHTMLline(f: IO[str], t: int, line: str) -> None:
        """writeLineHTML method"""
        ts = "   " * t
        f.write(f"{ts}{line}\n")
    def writeHTMLcomment(f: IO[str], t: int, com: str) -> None:
        """writeHTMLcomment method"""
        ts: str = "   " * t
        f.write(f"{ts}<!--{com}-->\n")  

    def genArt(f: IO[str], t: int) -> None:
        """genART method"""
        ranvals : tuple = ArtConfig.getvalues(ArtConfig)
        for i in range(ranvals[0]):
            if(ranvals[1][i] == 0):
                Circle.drawCircleLine(f, t, Circle((ranvals[2][i],ranvals[3][i],ranvals[4][i]),
                 (ranvals[9][i],ranvals[10][i],ranvals[11][i], ranvals[12][i])))
            elif(ranvals[1][i] == 1):
                Rectangle.drawRectangleLine(f, t, Rectangle((ranvals[2][i],ranvals[3][i],
                ranvals[7][i], ranvals[8][i]), (ranvals[9][i],ranvals[10][i],ranvals[11][i],ranvals[12][i])))
            else:
                Ellipse.drawEllipseLine(f, t, Ellipse((ranvals[2][i],ranvals[3][i],
                ranvals[5][i], ranvals[6][i]), (ranvals[9][i],ranvals[10][i],ranvals[11][i],ranvals[12][i])))

        
class Circle:
    """Circle class"""
    def __init__(self, cir: tuple, col: tuple) -> None:
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def drawCircleLine(f: IO[str], t: int, c) -> None:
        """drawCircle method"""
        ts: str = "   " * t
        line1: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" '
        line2: str = f'fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
        f.write(f"{ts}{line1+line2}\n")

class Rectangle:
    """Rectangle class"""
    def __init__(self, rect: tuple, col: tuple) -> None:
        self.rx: int = rect[0]
        self.ry: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]        


    def drawRectangleLine(f: IO[str], t: int, r) -> None:
        """drawRectangle method"""
        ts: str = "   " * t
        line1: str = f'<rect x="{r.rx}" y="{r.ry}" width="{r.width}" height="{r.height}" '
        line2: str = f'style="fill:rgb({r.red}, {r.green}, {r.blue});fill-opacity:{r.op}"></rect>'
        f.write(f"{ts}{line1+line2}\n")    
        
class Ellipse:
    """Ellipse class"""
    def __init__(self, ell: tuple, col: tuple) -> None:
        self.cx: int = ell[0]
        self.cy: int = ell[1]
        self.rx: int = ell[2]
        self.ry: int = ell[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]        


    def drawEllipseLine(f: IO[str], t: int, e) -> None:
        """drawEllipse method"""
        ts: str = "   " * t
        line1: str = f'<ellipse cx="{e.cx}" cy="{e.cy}" rx="{e.rx}" ry="{e.ry}" '
        line2: str = f'style="fill:rgb({e.red}, {e.green}, {e.blue});fill-opacity:{e.op}"></ellipse>'
        f.write(f"{ts}{line1+line2}\n")    
        
class genRandom:
    """class for random number generation"""
    def gen_init_in_range(a:int, b:int, cnt)->list:
        """function to make random ints"""
        rlist: list = []
        for k in range(cnt):
            x:int = random.randrange(a, b+1)
            rlist.append(x)
        return rlist

    def gen_rand_rational(a:int, b:int, cnt)->list:
        """function to make random 1 decimal number between 0 and 1
        >>> cnt =10
        >>> cnt == 10
        True
        """
        rlist: list = []
        for k in range(cnt):
            x:int = random.randrange(a, b+1)
            rlist.append(x/10)
        return rlist

class genTable:
    """class to make a table"""
    def createTable(lsha, lx, ly, lrad, lrx, lry, lw,lh, lR, lG, lB, lop) -> None:
        print(tabulate(list(zip(lsha, lx, ly, lrad, lrx, lry, lw,lh, lR, lG, lB, lop)),
                        numalign="right", showindex="always", tablefmt="plain",
                        headers=["CNT", "SHA", "X", "Y", "RAD", "RX", "RY", "W", "H", "R", "G", "B", "OP"]))

class ArtConfig:
    """make ranges for shapes"""
    num :int = 2000
    lsha :list = genRandom.gen_init_in_range(0,2, num)
    lx :list = genRandom.gen_init_in_range(0,500, num)
    ly :list = genRandom.gen_init_in_range(0,500, num)
    lrad :list = genRandom.gen_init_in_range(20,50, num)
    lrx :list = genRandom.gen_init_in_range(20,50, num)
    lry :list = genRandom.gen_init_in_range(20,50, num)
    lw :list = genRandom.gen_init_in_range(30,50, num)
    lh :list = genRandom.gen_init_in_range(30,50, num)
    lR :list = genRandom.gen_init_in_range(0,255, num)
    lG :list = genRandom.gen_init_in_range(0,255, num)
    lB :list = genRandom.gen_init_in_range(0,255, num)
    lop :list = genRandom.gen_rand_rational(1,10, num)
    genTable.createTable(lsha, lx, ly, lrad, lrx, lry, lw, lh, lR, lG, lB, lop)

    def getvalues(cls) -> tuple:
        trandlists :tuple = (cls.num, cls.lsha, cls.lx, cls.ly,
                    cls.lrad, cls.lrx, cls.lry, cls.lw,
                     cls.lh, cls.lR, cls.lG, cls.lB,
                      cls.lop)
        return trandlists


def main() -> None:
    """main method"""
    ProEpiloge.writeHTMLfile()

if __name__ == "__main__":
    main()
    
