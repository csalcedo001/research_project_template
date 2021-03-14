import matplotlib.pyplot as plt

from research_project_name.storage.plot import save_plot

class Plotter():
	def __init__(self, directory, name, plot_function, add_id=True):
		self.directory = directory
		self.name = name
		self.plot_function = plot_function
		self.add_id = add_id

		self.id = 0
		self.fig = None 

	def plot(self, *args, **kwargs):
		if self.fig is not None:
			self.close()

		self.fig = self.plot_function(*args, **kwargs)

		return self

	def save(self):
		if self.fig == None:
			raise Exception("No figure loaded. Call plot() first")

		save_plot(self.directory, self.name, self.id if self.add_id is not None else None)

		self.id += 1
	
	def show(self):
		plt.show()
	
	def close(self):
		plt.close(self.fig)
		self.fig = None

	def __enter__(self):
		pass

	def __exit__(self, exc_type, exc_value, traceback):
		self.close()
