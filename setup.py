import os
import setuptools
from pip.download import PipSession
from pip.req import parse_requirements


PACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))

# parse_requirements() returns generator of pip.req.InstallRequirement objects
PACKAGE_REQS = parse_requirements("requirements.txt", session=PipSession())

# reqs is a list of requirement
# e.g. ['tornado==3.2.2', '...']
REQS = [str(ir.req) for ir in PACKAGE_REQS]

if __name__ == "__main__":
    setuptools.setup(
        name="skeletor",
        version="0.1",
        description="",
        author="pafuent",
        packages=setuptools.find_packages(PACKAGE_PATH, exclude=["*.test",
                                                                 "*.test.*",
                                                                 "test.*",
                                                                 "test"]),
        keywords="",
        install_requires=REQS,
        include_package_data=True,
        entry_points={
            'console_scripts': [
                'skeletor = skeletor.commandline.skeletor:main',
            ],
            'skeletor.commandline.commands': [
                'dummy = skeletor.commandline.commands.dummy:DummyCommand',
            ],
        },
    )
