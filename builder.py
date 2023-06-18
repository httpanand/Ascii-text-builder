import pyfiglet
from pyfiglet import Figlet


fig = Figlet(font='graffiti')
text = input("Input text ")
ascii_text = fig.renderText(text)

print(ascii_text)

 
