import pyfiglet
from pyfiglet import Figlet


fig = Figlet(font='graffiti')
text = input("Input text ")
ascii_text = pyfiglet.figlet_format(text)

print(ascii_text)

 
