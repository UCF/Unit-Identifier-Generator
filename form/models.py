from django.db import models

# Create your models here.
class Request(models.Model):
	requester = models.CharField("requested by", max_length=300)
	unit_name = models.CharField("unit name", max_length=300)
	department = models.CharField(max_length=300)
	phone = models.CharField("phone number", max_length=50)
	email = models.EmailField(max_length=254)
	request_date = models.DateTimeField("requested on", auto_now_add=True)
	design_options = models.CharField(max_length=300)
	# Add generated file output here when I actually figure that out...
	def __unicode__(self):
		return self.unit_name
	
class Logo(models.Model):
	request_id = models.ForeignKey(Request),
	request_name = models.ForeignKey(Request, to_field="unit_name"),
	design_option = models.CharField(max_length=400)
	# Now we store each generated color version of the given design option:
	# ... if I can figure out how to store the files...
	# Color field names correspond to CMYK color code and whether color is
	# bright or metallic; g=gold, k=black, w=white, m=metallic, b=bright 
	color_g_m = models.CharField("Gold (G) PMS 874 (metallic)", max_length=300)
	color_g_b = models.CharField("Gold (G) PMS 7406 (bright)", max_length=300)
	color_b = models.CharField("Black (K)", max_length=300)
	color_w = models.CharField("White (W)", max_length=300)
	color_kg_m = models.CharField("Black/Gold (KG) PMS 874 (metallic)", max_length=300)
	color_kg_b = models.CharField("Black/Gold (KG) PMS 7406 (bright)", max_length=300)
	color_wg_m = models.CharField("White/Gold (WG) PMS 874 (metallic)", max_length=300)
	color_wg_b = models.CharField("White/Gold (WG) PMS 7406 (bright)", max_length=300)
	# The above fields are temporary to just get some fields in the admin.
	# Use the below fields when the front-end is set up:
	
	# color_g_m = models.FileField()
	# color_g_b = models.FileField()
	# color_b = models.FileField()
	# color_w = models.FileField()
	# color_kg_m = models.FileField()
	# color_kg_b = models.FileField()
	# color_wg_m = models.FileField()
	# color_wg_b = models.FileField()
	def __unicode__(self):
		return self.request_name
	