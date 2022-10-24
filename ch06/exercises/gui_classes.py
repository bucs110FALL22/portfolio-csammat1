class brick_block:
	def __init__(self):
    self.destroyed = False
    self.color = 'brown'
    self.texture = brick
class goomba:
  def __init__(self):
    self.alive = True
    self.color = 'brown'
    self.lives = 1
class mario:
  def __init__(self):
    self.alive = True
    self.lives = 3
    self.player = 1
    self.on_screen = True