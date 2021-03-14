import os
import torch
import glob
import ntpath

def save_model(directory, name, model, epoch=None):
	filename = name

	if epoch != None:
		filename += "_{}".format(epoch)
	
	filename += ".pt"

	path = os.path.join(directory, filename)
	
	torch.save(model.state_dict(), path)

def load_model(directory, filename, model):
	model.load_state_dict(torch.load(os.path.join(directory, filename)))

def load_last_model(directory, name, model):
	filenames = glob.glob(os.path.join(directory, name + "*.pt"))

	if len(filenames) == 0:
		raise Exception("No model named {} found on directory {}.".format(name, directory))

	if os.path.join(directory, name + ".pt") in filenames:
		path = os.path.join(directory, name + ".pt")
	else:
		indices = [int(ntpath.basename(filename)[len(name) + 1: -3]) for filename in filenames]
		indices.sort()

		path = os.path.join(directory, name + "_" + str(indices[-1]) + ".pt")

	model.load_state_dict(torch.load(path))
