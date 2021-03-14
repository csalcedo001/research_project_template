import matplotlib.pyplot as plt
import numpy as np
import math
import torchvision.utils

def plot_grid_from_batch(batch, grid_side=None, title=""):
	if grid_side == None:
		grid_side = int(math.sqrt(len(batch)))
	
	plt.title(title)
	plt.axis("off")
	plt.imshow(np.transpose(torchvision.utils.make_grid(batch[: grid_side ** 2], grid_side, padding=2, normalize=True).cpu().numpy(), (1, 2, 0)))

def plot_sample(batch, title=""):
	plt.title(title)
	plt.axis("off")
	plt.imshow(np.transpose(batch[0].cpu().numpy(), (1, 2, 0)))
