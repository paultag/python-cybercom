from setuptools import setup


long_description = """\
This package contains a set of Python grpc bindings and native objects that
talk to the CYBERCOM server, which manages and issues x509 Certifciates.
"""

setup(
    name="cybercom",
    version="0.1",
    packages=[
        'cybercom',
        'cybercom.pb',
    ],
    author="Paul Tagliamonte",
    author_email="paultag@gmail.com",
    long_description=long_description,
    description='grpc CYBERCOM bindings',
    license="Expat",
    url="",
    platforms=['any']
)
