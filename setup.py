import setuptools

import package_name as lib



with open("requirements.txt", "r", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

with open("HISTORY.md", "r", encoding="utf-8") as f:
    history = f.read()



setuptools.setup(
    name=lib.__name__,
    version=lib.__version__,
    description=lib.__description__,
    long_description=readme,
    long_description_content_type="text/markdown",
    author=lib.__author__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.4",
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={
        "Source": about["__url__"]
    },
)
