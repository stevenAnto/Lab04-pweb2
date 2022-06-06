from interpreter import draw
from chessPictures import *
from picture import *
nk= knight.negative()
k= knight
fila= k.join(nk)
draw(fila.negative().up(fila))