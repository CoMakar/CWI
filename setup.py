import os

from distutils.command.build import build
from setuptools import setup, find_packages


class BuildCommand(build):
    def initialize_options(self):
        build.initialize_options(self)
        self.build_base = "setuptools-build"


def load_env(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File '{path}' not found")

    with open(path) as env:
        for line in env:

            line = line.strip()
            if not line or line.startswith('#'):
                continue

            key, value = line.split('=', 1)
            os.environ[key] = value


load_env(".build_info")

install_requires = [
    "numpy",
    "pyaudio",
    "loguru",
    "rich",
    "click",
]

dev_requires = [
    "pyinstaller",
]

version = os.getenv("VERSION")
name = os.getenv("PKG_NAME")

setup(
    name=name,
    version=version,
    author="QMakar",
    description="CLI morse audio generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=install_requires,
    include_package_data=True,
    extras_require={
        "dev": dev_requires,
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: Windows 10 64bit",
    ],
    entry_points={
        "console_scripts": [
            f"{name} = scripts.cwi:main",
        ],
    },
    cmdclass={"build": BuildCommand},
)
