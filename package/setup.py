import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="research_project_name", # Replace with your own username
	version="0.0.1",
	author="Cesar Salcedo",
	author_email="cesar.salcedo@utec.edu.pe",
	description="Research project",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',

	### Uncomment to include data files saved at data/
	# include_package_data=True,
	# package_data={'': ['data/*']},
)
