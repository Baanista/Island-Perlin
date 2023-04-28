# Imports PIL module
from PIL import Image, ImageDraw, ImageFont
import generator
# creating a image object (new image object) with
# RGB mode and size 200x200

im = generator.create_image(50, 13, False, (100, 100), .01, 5)


# This method will show image in any image viewer

im.save('/Users/303student/CellularEvo/generatorim.png', 'PNG')

im.show()
