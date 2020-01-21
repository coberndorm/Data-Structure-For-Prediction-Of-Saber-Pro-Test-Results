
class Punto2D():
    """Representacion de punto en 2 dimenciones"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
      	return self.y
      
    def radio_polar(self):
        return math.sqrt(x*x + y*y)

    def angulo_polar(self):
 				return math.atan(self.y/self.x)

    def dist_euclidiana(self, Punto2D other):
    	return math.sqrt((other.x - self.x)*(other.x - self.x) + (other.y - self.y)*(other.y - self.y))
    	
      
class Fecha():
		"""" Representacion de una fecha con este formato día/mes/año"""
    
    def __init__(self, mes, dia, año):
    	self.mes = mes
      self.dia = dia
      self.año = año
      
    def __init__ (self, fecha)
    	dia
      
      
    def get__mes(self):
      return self.mes
      
      
    def get__dia(self):
      return self.dia
      
    def get__año(self):
      return self.año
      
    def cadena__fecha(self, mes, dia, año):
    	return self.mes+"/"+self.dia+"/"+self.año
