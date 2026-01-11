from setuptools import setup, find_packages

setup(
    name="devhelp",
    version="0.1.0",
    # find_packages() busca automáticamente la carpeta 'src'
    packages=find_packages(),
    # Esto asegura que se incluyan tus archivos JSON de la carpeta data
    include_package_data=True,
    # Aquí definimos el comando que el equipo usará en la terminal
    entry_points={
        'console_scripts': [
            'devhelp=src.main:main',
        ],
    },
    install_requires=[
        # Si más adelante usas librerías como 'rich', las pondremos aquí
    ],
    python_requires='>=3.6',
)