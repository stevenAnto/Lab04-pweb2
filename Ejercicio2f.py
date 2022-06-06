from interpreter import draw
from chessPictures import *
from picture import *

fila=square.join(square.negative()).horizontalRepeat(4)
draw(fila.up(fila.negative()).verticalRepeat(2))
