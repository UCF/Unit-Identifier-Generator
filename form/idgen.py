from django.template.defaultfilters import slugify

import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import textwrap

# ID Generator class will go here.

class IDGen:
	
	# Define color combinations (same across all iterations):
	gold_m = '-G-874'			# Gold (G) PMS 874 (metallic)
	gold_b = '-G-7406'			# Gold (G) PMS 7406 (bright)
	black = '-B'				# Black (K)
	white = '-W'				# White (W)
	black_gold_m = '-KG-874'	# Black/Gold (KG) PMS 874 (metallic)
	black_gold_b = '-KG-7406'	# Black/Gold (KG) PMS 7406 (bright)
	white_gold_m = '-WG-874'	# White/Gold (KG) PMS 874 (metallic)
	white_gold_b = '-WG-7406'	# White/Gold (KG) PMS 7406 (bright)
	colors = [gold_m, gold_b, black, white, black_gold_m, black_gold_b, white_gold_m, white_gold_b]
	
	# Define Raster logo output dimensions/positions (.png, .jpeg) for text positioning later:
	id_width = 2000 	# All logos use this width
	uid_ypos = 642
	muid_ypos = 140
	muid_ypos_ol = 257 	# If MUID is only on one line, the ypos needs to be this number
	vuid_ypos = 853
	
	def __init__(self, design_option, unit_name, fontsize, spanw, spanh, muid_linebreak='n'):
		self.design_option = design_option
		self.unit_name = unit_name
		self.fontsize = int(fontsize)
		self.spanw = spanw
		self.spanh = spanh
		self.muid_linebreak = muid_linebreak # Whether or not the MUID uses a linebreak
		
		self.unit_name_caps = self.unit_name.upper()
		self.unit_name_slug = slugify(self.unit_name)
	
	#if self.muid_linebreak == 'y':
	#	muid_ypos = muid_ypos_ol	

	def temporaryrun(self): # Just to get the class running initially
		font_muid = ImageFont.truetype("form/static/fonts/ameri-webfont.ttf", self.fontsize) #replace 100 with font size
	
		muid_k = Image.open("form/static/img/muid/muid-template-rgb.png")	
		draw = ImageDraw.Draw(muid_k)

		draw.text((0, 0), self.unit_name_caps, (0,0,0), font=font_muid) #position, text, color, font
		draw = ImageDraw.Draw(muid_k)

		muid_k.save(self.unit_name_slug + "-K.png")
		muid_k.save(self.unit_name_slug + "-K.jpeg")
		muid_k.convert("CMYK").save(self.unit_name_slug + "-K.pdf")
		muid_k.convert("CMYK").save(self.unit_name_slug + "-K.eps")