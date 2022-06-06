from interpreter import draw
from chessPictures import *
from picture import *

fila=square.join(square.negative()).horizontalRepeat(4)
draw(fila.under(fila.negative()).verticalRepeat(2))
