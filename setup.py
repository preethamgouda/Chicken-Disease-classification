
import setuptools

with open ("Readme.md","r",encoding="utf-8") as f:
    long_description=f.read()


version1 = "0.0.0"

REPO_NAME ="Chicken-Disease-classification"
AUTHOR_USER_NAME="preethamgouda"
SRC_REPO="cnnClassifier"
AUTHOUR_EMAIL="preethamgowda1231@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=version1,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOUR_EMAIL,
    description=" small python package",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")


)