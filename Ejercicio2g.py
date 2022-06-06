from ctypes import create_string_buffer
from imp import create_dynamic
from re import S
from interpreter import draw
from chessPictures import *
from picture import *
fCuadra1= square.join(square.negative()).horizontalRepeat(4)
f3456= fCuadra1.negative().up(fCuadra1).verticalRepeat(2)

c1f8= rock.join(knight.join(bishop))
c8f8= bishop.join(knight.join(rock))

f8= fCuadra1.negative().under(c1f8.join(queen.join(king.join(c8f8))))
f7= fCuadra1.under(pawn.horizontalRepeat(8))

tab= f8.up(f7).up(f3456).up(f7.negative()).up(f8.negative())
draw(tab)