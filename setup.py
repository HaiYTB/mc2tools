from setuptools import find_packages, setup

# Introduce
NAME = "mc2tools"
VERSION = "1.0.0"
DESCRIPTION = "Minecraft Tool Using Python"
AUTHOR = "Henry(Minh Hai) Phan"
URL = "https://github.com/HaiYTB/mc2tools"
KEYWORDS = [
    "python",
    "haitool",
    "haiytb",
    "minecraft",
    "server",
    "minecraft-tool",
    "mcserver",
    "cli",
    "tool",
    "automation",
    "minecraft-admin",
    "minecraft-utility",
]

# Requirements
require_packages = []


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email="haiwt2xbox@gmail.com",
    url=URL,
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=require_packages,
    entry_points={"console_scripts": ["mc2tools = mc2tools._main:main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Simulation",
        "Topic :: Utilities",
    ],
    keywords=KEYWORDS,
)
