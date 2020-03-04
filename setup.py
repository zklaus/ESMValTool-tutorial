import setuptools
import versioneer


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="esmvaltool-tutorial",
    version=versioneer.get_version(),
    author="Klaus Zimmermann",
    author_email="klaus.zimmermann@smhi.se",
    description="A ESMValTool Beginner's Guide",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zklaus/ESMValTool-tutorial",
    cmdclass=versioneer.get_cmdclass(),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
