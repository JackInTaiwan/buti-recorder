from setuptools import setup, find_packages

setup(
	name='butirecorder',
	version='0.0',
	description='A python module providing clear and beautified methods to make recording and saving trained model systematic and clarified.',
	url='https://github.com/jackintaiwan/buti-recorder',
	author='Yuan Chia, Zheng',
	author_email='jackconvolution@gmail.com',
	packages=['butirecorder', 'recorders'],
)

setup(install_requires=[
    "numpy",
])

setup(python_requires='>=3.0')