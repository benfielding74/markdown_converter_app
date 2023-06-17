from setuptools import setup

setup(
    name='markdown_converter',
    version='1.0.0',
    packages=['markdown_converter'],
    install_requires=['markdownify', 'tqdm', 'click'],
    entry_points={
        'console_scripts': [
            'markdown_converter = markdown_converter.main:main'
        ]
    },
)
