from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in migoo_new/__init__.py
from migoo_new import __version__ as version

setup(
	name="migoo_new",
	version=version,
	description="migoo",
	author="palak",
	author_email="palakpadalia19@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
