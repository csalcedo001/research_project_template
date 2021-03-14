import matplotlib.pyplot as plt

def plot_loss(losses_list, labels, title=None):
	if len(losses_list) != len(labels):
		raise Exception("Each list must have a corresponding label")

	for i, losses in enumerate(losses_list):
		plt.plot(losses, label=labels[i])

	
	if title == None:
		title = "Training loss"
	
	plt.title(title)
	plt.ylabel("Loss")
	plt.xlabel("Iterations")
	plt.legend()
