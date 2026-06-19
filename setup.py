from setuptools import setup, find_packages

setup(
    name='moriarty',
    version='1.0.0',
    description='OSINT Framework para busca de informações públicas',
    packages=find_packages(), # Encontra automaticamente a pasta 'src' porque ela tem o __init__.py
    install_requires=[
        'httpx',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'moriarty=src.main:main', # Aponta para o arquivo dentro de src e chama a função main()
        ],
    },
)
