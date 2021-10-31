from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Ddvc-nlp-project-demo"
AUTHOR_USER_NAME = "plaban1981"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for DVC-NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/plaban1981/dvc-nlp-project-demo",
    author_email="nayakpplaban@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)