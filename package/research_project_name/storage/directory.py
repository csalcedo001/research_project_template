import os
from datetime import datetime

# Get a subdirectory from directory named after
# the time of execution
def get_subdirectory_by_time(directory):
	subdirectory = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

	return os.path.join(directory, subdirectory)

# Create directory and files if not created already
def setup(directory):
	os.makedirs(directory)
