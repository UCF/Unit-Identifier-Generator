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
	white_gold_m = '-WG-874'	# White/Gold (WG) PMS 874 (metallic)
	white_gold_b = '-WG-7406'	# White/Gold (WG) PMS 7406 (bright)
	colors = [gold_m, gold_b, black, white, black_gold_m, black_gold_b, white_gold_m, white_gold_b]
	
	# Define all necessary font colors (RBG format):
	font_gold_metallic = (188,155,106)
	font_gold_bright = (205,155,43)
	font_black = (0,0,0)
	font_white = (255,255,255)
	
	# Define which logo color combinations need which font color:
	logos_text_gold_metallic = [gold_m]
	logos_text_gold_bright = [gold_b]
	logos_text_black = [black, black_gold_m, black_gold_b]
	logos_text_white = [white, white_gold_m, white_gold_b]
	
	# Define file types (same across all iterations):
	jpeg = '.jpeg'
	png = '.png'
	pdf = '.pdf'
	eps = '.eps'
	file_types = [png, jpeg, pdf, eps]
	
	# Define whether above file types need to be converted to CMYK format upon saving (default to RGBA):
	needs_cmyk_convert = [pdf, eps]
	
	# Define Raster logo output dimensions/positions (.png, .jpeg) for text positioning later:
	id_width = 2000 	# All logos use this width
	uid_ypos = 608
	muid_xpos = 799
	muid_ypos = 227
	muid_ypos_ol = 313 	# If MUID is only on one line, the ypos needs to be this number
	vuid_ypos = 595
	
	def __init__(self, design_option, unit_name, fontsize, spanw, spanh, muid_linebreak='n'):
		self.design_option = design_option
		self.unit_name = unit_name
		self.fontsize = int(fontsize)
		self.spanw = int(spanw)
		self.spanh = int(spanh)
		self.muid_linebreak = muid_linebreak # Whether or not the MUID uses a linebreak
		
		self.lineheight = self.fontsize
		
		self.unit_name_caps = self.unit_name.upper()
		self.unit_name_slug = slugify(self.unit_name)
	
		self.font = ImageFont.truetype("form/static/fonts/ameribol-webfont.ttf", self.fontsize)
		
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


	# This does the actual processing:
	def makelogos(self):
		
		for color in self.colors:
			img = Image.open("form/static/img/" + self.design_option + "/" + self.design_option + "-template" + color + ".png")
			
			draw = ImageDraw.Draw(img)
			
			# #000 text color for: black, black_gold_m, black_gold_b
			# #BC9B6A text color for: gold_m
			# #CA992C text color for: gold_b
			# #FFF text color for: white, white_gold_m, white_gold_b
			
			font_color = 0
			if color in self.logos_text_gold_metallic:
				font_color = self.font_gold_metallic
			elif color in self.logos_text_gold_bright:
				font_color = self.font_gold_bright
			elif color in self.logos_text_black:
				font_color = self.font_black
			else: # Color assumed to be in self.logos_text_white
				font_color = self.font_white
			
			draw.text((self.xpos, self.ypos), self.unit_name_caps, font_color, font=self.font) #position, text, color, font
			
			# TO-DO: Add black bg fill for .jpegs in self.logos_text_white!
			
			for file_type in self.file_types:
				if file_type in self.needs_cmyk_convert:
					img.convert("CMYK").save(self.design_option + "-" + self.unit_name_slug + color + file_type)
				else:
					img.save(self.design_option + "-" + self.unit_name_slug + color + file_type)