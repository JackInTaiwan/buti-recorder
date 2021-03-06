from setuptools import setup, find_packages

setup(
	name='butirecorder',
	version='0.3',
	description='A python module providing clear and beautified methods to make recording and saving trained model systematic and clarified.',
	url='https://github.com/jackintaiwan/buti-recorder',
	author='Yuan Chia, Zheng',
	author_email='jackconvolution@gmail.com',
	packages=['butirecorder', 'butirecorder.recorders'],
    python_requires='>=3.0',
    install_requires=[
        "numpy",
    ]
)