class GrayscaleToRGB(object):
	def __init__(self):
		pass
	
	def __call__(self, sample):
		return sample.repeat(3, 1, 1)
