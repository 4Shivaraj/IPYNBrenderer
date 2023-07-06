import setuptools

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "IPYNBrenderer"
AUTHOR_USER_NAME = "4Shivaraj"
SRC_REPO = "IPYNBrenderer"
AUTHOR_EMAIL = "4shivaraj.gowda@gmail.com"
REPO_URL= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=REPO_URL,
    project_urls = {
        "Bug Tracker": f"{REPO_URL}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)