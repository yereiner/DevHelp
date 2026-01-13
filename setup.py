from setuptools import setup, find_packages

setup(
    name="devhelp",
    version="1.0.1", # Sube la versión para que pipx note el cambio
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'devhelp=src.main:main',
        ],
    },
    install_requires=[
        'rich>=10.0.0', # <--- ESTO ES VITAL
    ],
    python_requires='>=3.7',
)