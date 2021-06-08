import setuptools
setuptools.setup(
    name='procmanager',
    version='1.0.1',
    scripts=['./main.py'],
    author='Supra#6561 / Github: supraaxdd',
    description='Simple CLI process manager.',
    packages=setuptools.find_packages(),
    install_requires=[
        'setuptools',
        'psutil',
        'typer'
    ],
    python_requires='>=3.9'
)