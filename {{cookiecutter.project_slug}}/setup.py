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
        name="{{ cookiecutter.project_slug }}",
        version="{{ cookiecutter.project_version }}",
        description="{{ cookiecutter.project_description }}",
        author="{{ cookiecutter.author }}",
        packages=setuptools.find_packages(PACKAGE_PATH, exclude=["*.test",
                                                                 "*.test.*",
                                                                 "test.*",
                                                                 "test"]),
        keywords="",
        install_requires=REQS,
        include_package_data=True,
        entry_points={
            'console_scripts': [
                '{{ cookiecutter.project_slug.replace('_', '-') }} = {{ cookiecutter.project_slug }}.commandline.{{ cookiecutter.project_slug }}:main',
            ],
            '{{ cookiecutter.project_slug }}.commandline.commands': [
                '{{ cookiecutter.cli_command }} = {{ cookiecutter.project_slug }}.commandline.commands.{{ cookiecutter.cli_command }}:{{ cookiecutter.cli_command.replace('_', '').capitalize() }}Command',
            ],
        },
    )
