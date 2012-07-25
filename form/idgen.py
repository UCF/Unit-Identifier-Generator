from django.template.defaultfilters import slugify

import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import textwrap

# The IDGen() class is designed to handle a single
# logo type with multiple color combinations and file types.

class IDGen:
	
	# Define color combinations (same across all iterations):
	gold_m = '-G-874'			# Gold (G) PMS 874 (metallic)
	gold_b = '-G-7406'			# Gold (G) PMS 7406 (bright)
	black = '-K'				# Black (K)
	white = '-W'				# White (W)
	black_gold_m = '-KG-874'	# Black/Gold (KG) PMS 874 (metallic)
	black_gold_b = '-KG-7406'	# Black/Gold (KG) PMS 7406 (bright)
	white_gold_m = '-WG-874'	# White/Gold (KG) PMS 874 (metallic)
	white_gold_b = '-WG-7406'	# White/Gold (KG) PMS 7406 (bright)
	colors = [gold_m, gold_b, black, white, black_gold_m, black_gold_b, white_gold_m, white_gold_b]
	
	# Define Raster logo output dimensions/positions (.png, .jpeg) for text positioning later:
	id_width = 2000 	# All logos use this width
	uid_ypos = 642
	muid_xpos = 815
	muid_ypos = 227
	muid_ypos_ol = 320 	# If MUID is only on one line, the ypos needs to be this number
	vuid_ypos = 853
	
	def __init__(self, design_option, unit_name, fontsize, spanw, spanh, muid_linebreak='n'):
		self.design_option = design_option
		self.unit_name = unit_name
		self.fontsize = int(fontsize)
		self.spanw = int(spanw)
		self.spanh = int(spanh)
		self.muid_linebreak = muid_linebreak # Whether or not the MUID uses a linebreak
		
		self.unit_name_caps = self.unit_name.upper()
		self.unit_name_slug = slugify(self.unit_name)
	
		self.font = ImageFont.truetype("form/static/fonts/ameri-webfont.ttf", self.fontsize)
		
		if self.design_option == 'MUID':
			self.xpos = self.muid_xpos
			if self.muid_linebreak == 'y':
				self.ypos = self.muid_ypos
			else:
				self.ypos = self.muid_ypos_ol
		else:
			self.xpos = (self.id_width - self.spanw) / 2
		 
		if self.design_option == 'UID':
			self.ypos = self.uid_ypos
					
		if self.design_option == 'VUID':
			self.ypos = self.vuid_ypos
	
	#if self.muid_linebreak == 'y':
	#	muid_ypos = muid_ypos_ol	

	def temporaryrun(self): # Just to get the class running initially
		muid_k = Image.open("form/static/img/muid/muid-template-K.png")	
		draw = ImageDraw.Draw(muid_k)

		draw.text((self.xpos, self.ypos), self.unit_name_caps, (0,0,0), font=self.font) #position, text, color, font
		draw = ImageDraw.Draw(muid_k)

		muid_k.save(self.unit_name_slug + "-K.png")
		muid_k.save(self.unit_name_slug + "-K.jpeg")
		muid_k.convert("CMYK").save(self.unit_name_slug + "-K.pdf")
		muid_k.convert("CMYK").save(self.unit_name_slug + "-K.eps")