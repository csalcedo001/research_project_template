import os
import matplotlib.pyplot as plt

def save_plot(directory, name, id=None):
	filename = name
	
	if id is not None:
		filename += "_{0:0=3d}".format(id)

	filename += ".jpg"

	plt.savefig(os.path.join(directory, filename))
