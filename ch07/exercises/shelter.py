import time
class animal():
  def __init__(self, name = '', type = ''):
    self.id = time.strftime("%Y%m%M%S")
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d/%m/%Y")
    self.adopted = None
  def adopted(self):
    self.adopted = time.strftime("%d/%m/%Y")
  def __str__(self):
    result_str = f'Name:{self.name}, Type:{self.type}, Arrived:{self.arrived}, ID#:{self.id}, adopted:{self.adopted}'
    return result_str
def main():
  doug = animal('Doug', 'Dog')
  print(doug)
  time.sleep(1)
  sammy = animal('Sammy', 'Cat')
  sammy.adopted()
  print(sammy)
main()