from setuptools import find_packages, setup

setup(
    name="pymongo-migrate",
    version="1.0.0",
    description="MongoDB data migration tool in Python",
    url="https://github.com/stxnext/pymongo-migrate",
    license="Apache",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    platforms="any",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "pymongo>=3.7.2",
        "Click>=7",
    ],
    entry_points={"console_scripts": ["pymongo-migrate=pymongo_migrate.cli:cli"]},
    keywords=["mongo", "mongodb", "pymongo", "migrate", "migration"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database",
    ],
)
