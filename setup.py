from setuptools import find_packages, setup
from typing import List

### UPDATE BELOW SCTION FOR THE PROJECT###
__version__ = "0.0.0"

AUTHOR_NAME = "Arindam C"
REPO_NAME = "CICD_Wine_Quality_Prediction"
AUTHOR_USER_NAME = "arindam-29"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "arindam.choudhury.email@gmail.com"

##########################################

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    from requirements.txt file
    '''
    # Initializing blank requirements list
    requirements = []
    HYPHEN_E_DOT_TEXT = '-e . # This is needed for creation as a local Project'
    # Opening requirements.txt file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        # Remove hyphen_e_dot if present in requirements
        if HYPHEN_E_DOT_TEXT in requirements:
            requirements.remove(HYPHEN_E_DOT_TEXT)

    return requirements

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for ml apps with cicd",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = get_requirements('requirements.txt')
)