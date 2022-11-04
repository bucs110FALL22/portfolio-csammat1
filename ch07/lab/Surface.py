from Rectangle import Rectangle
class Surface():
  def __init__(self, filename, x, y, h, w):
    self.rect = Rectangle(x, y, h, w)
    self.image = filename
  def getRect(self):
    '''
    returns the instance of the Surface object
    Args: (Surface) self Surface
    return: (Rectangle) returns a rectangle stored on this surface
    '''
    return self.rect