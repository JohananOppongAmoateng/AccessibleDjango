import io
from setuptools import setup, find_packages
with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="accessible-django",
    version="1.0.0",
    description="A Django package for accessibility checks during development.",
    long_description=long_description,  # Optional: long description from your README
    long_description_content_type="text/markdown",
    author="Johanan Oppong Amoateng",
    author_email="johananoppongamoateng2001@gmail.com",
    packages=find_packages(),
    python_requires=">=3.10",
    license="MIT",
    install_requires=[
        "beautifulsoup4>=4.9.3",
        "Django>=5.1.2",
        "mkdocs==1.6.1",
        "setuptools==75.6.0"
    ]
    ,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Framework :: Django',
        'Framework :: Django :: 5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
)
