import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import textwrap

# ID Generator class will go here.

class IDGen:
	
	def __init__(self, design_option, unit_name_caps, unit_name_slug):
		self.design_option = design_option
		self.unit_name_caps = unit_name_caps
		self.unit_name_slug = unit_name_slug

	def temporaryrun(self): # Just to get the class running initially
		font_muid = ImageFont.truetype("form/static/fonts/ameri-webfont.ttf", 100) #replace 100 with font size
	
		muid_k = Image.open("form/static/img/muid/muid-template-rgb.png")	
		draw = ImageDraw.Draw(muid_k)

		draw.text((0, 0), self.unit_name_caps, (0,0,0), font=font_muid) #position, text, color, font
		draw = ImageDraw.Draw(muid_k)

		muid_k.save(self.unit_name_slug + "-K.png")
		muid_k.save(self.unit_name_slug + "-K.jpeg")
		muid_k.convert("CMYK").save(self.unit_name_slug + "-K.pdf")
		muid_k.convert("CMYK").save(self.unit_name_slug + "-K.eps")