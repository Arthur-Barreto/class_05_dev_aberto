#!/usr/bin/env python3
from setuptools import setup

setup(
    name="dev_aberto_arthurmsb",
    version="0.1",
    packages=["dev_aberto"],
    install_requires=["requests>=2.32.3"],
    scripts=["scripts/hello.py"],
)
