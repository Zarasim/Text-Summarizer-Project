import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.1"
REPO_NAME = "Text-Summarizer-Project"
AUTHOR_NAME = "Zarasim"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "simone.appella@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
                                      
    