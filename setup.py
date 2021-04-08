import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="svart",
    version="1.0.0",
    author="Siddharth Dushantha",
    author_email="siddharth.dushantha@gmail.com",
    description="Change between dark/light mode depending on the ambient light intensity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdushantha/svart",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["svart = svart.svart:main"]},
    install_requires=["alsmodule-pkg"],
)

