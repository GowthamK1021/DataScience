from setuptools import find_packages,setup
edot="-e ."
def get_requirements(path:str)->list:
    """
    This Fuction reads the requirment packagaes for the project
    """
    with open(path) as file:
        requirements=file.readlines()
        requirements= [r.replace("\n","") for r in requirements]
    if edot in requirements:
        requirements.remove(edot)
    return requirements


setup(
    name='Mle2eproject',
    version='0.0.1',
    author='Gowtham',
    author_email='itsgowtham1021@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)