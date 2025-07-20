"""
Dict Merger包的安装配置
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dict-merger",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="一个用于合并字典的Python包，支持深度合并和值覆盖",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dict-merger",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    keywords="dict dictionary merge deep-merge utility",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/dict-merger/issues",
        "Source": "https://github.com/yourusername/dict-merger",
    },
) 