from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file path.
    """
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
       
    return requirements




setup(
    name="mlproject",
    version="0.0.1",
    author="Masihuddin",
    author_email="masihuddinkhan025@gmail.com",
    package = find_packages(),
    install_requires=get_requirements('requirements.txt')
)