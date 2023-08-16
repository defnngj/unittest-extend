import re
import ast
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('xtest/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setuptools.setup(
    name="xtest",
    version=version,
    author="fnngj",
    author_email="fnngj@126.com",
    description="unittest extend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/defnngj/unittest-extend",
    packages=["xtest"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
    ],
    setup_requires=["setuptools_scm"],
)
