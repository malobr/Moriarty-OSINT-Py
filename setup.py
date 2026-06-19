from setuptools import setup

setup(
    name='moriarty',
    version='1.0.0',
    description='OSINT Framework para busca de informações públicas',
    py_modules=['main', 'motor'], # Aqui listamos os arquivos que fazem o projeto rodar
    install_requires=[
        'httpx',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'moriarty=main:main', # Isso cria o comando nativo no terminal
        ],
    },
)