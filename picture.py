from colors import *
class Picture:
  def __init__(self, img):
      self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
      if color not in inverter:
          return color
      return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    contador = len(self.img)-1;
    print (contador)
    for i in range(len(self.img)):
        vertical.append(self.img[contador])
        contador=contador-1

    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    #return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    #return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    print (self)
    for i in range(len(self.img)):
        self.img[i]=self.img[i]+p.img[i]

    return Picture(self.img)

  def up(self, p):
      """dsfas"""
    #return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
   # return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    #return Picture(None)

  def verticalRepeat(self, n):
      """dsfsadf"""
   # return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
