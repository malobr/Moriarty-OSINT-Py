from setuptools import setup, find_packages

setup(
    name='moriarty',
    version='1.0.0',
    description='OSINT Framework para busca de informações públicas',
    packages=find_packages(), 
    package_data={
        'src': ['data/*.json'], # Força a inclusão do JSON no pacote
    },
    include_package_data=True,
    install_requires=[
        'httpx',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'moriarty=src.main:main', 
        ],
    },
)
