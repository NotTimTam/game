# Imports.
from os import system, name
from shutil import get_terminal_size

# Clear the screen.
def clearScrn(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# Basic display.
class display:
  hdng = ""
  txt = []
  borders = ["╚", "╔", "═", "║", "╗", "╝"]
  vertical_bar = borders[3]
  horizontal_bar = borders[2]
  bl = borders[0]
  br = borders[5]
  tl = borders[1]
  tr = borders[4]
  
  def __init__(self, heading="Heading", text=["Text1", "Text2"], clearscreen=True):
    # Clear the screen.
    if clearscreen == True:
      clearScrn()
    # Assign class variables to the inputted values.
    self.hdng = heading
    self.txt = text

  def screenWidth(self):
    screen_dimensions = get_terminal_size()
    return screen_dimensions[0]

  def bounds(self):
    # Variables
    width = 0
    height = 1
    l = 0
    t = 0

    # Set the height to the total number of objects, and the width to the longest object.
    for item in self.txt:
      height += 1
      if len(item) > width:
        width = len(item)
    # Set the width to the len of heading if it is wider than the predetermined width.
    if len(self.hdng) > width:
      width = len(self.hdng)
    return l, t, width, height

  # Display the menu.
  def showMenu(self):
    # Get the bounds.
    left_b, top_b, wid, hei = self.bounds()

    # Display the top line.
    print(self.tl + (self.horizontal_bar * (self.screenWidth()-2)) + self.tr)

    # Display the content.
    print(self.borderText(self.hdng.upper()))
    for item in self.txt:
      print(self.borderText(item))

    # Display the bottom line.
    print(self.bl + (self.horizontal_bar * (self.screenWidth()-2)) + self.br)

  def borderText(self, text):
    rt = self.vertical_bar + text + self.vertical_bar 
    r_space = self.screenWidth() - len(rt)
    return self.vertical_bar + text + (" " * r_space) + self.vertical_bar
