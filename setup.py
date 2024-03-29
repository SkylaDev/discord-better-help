from setuptools import setup

with open("README.md") as README:
    long_description = README.read()

setup(
    name='discord-better-help',
    version='1.3.0',
    description='An extension module for discord.py to make setting up a help command easier.',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='SkylaDev',
    author_email='',
    url='',
    packages=['better_help'],
    install_requires=['discord.py'],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
    ],
    project_urls={
        "Source": "https://github.com/SkylaDev/discord-better-help",
    },
)
