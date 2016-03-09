import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class {{ cookiecutter.project_slug.replace('_', '').capitalize() }}CommandLine(App):  # pylint: disable=too-few-public-methods
    """{{ cookiecutter.project_slug.capitalize() }} command line application.
    In order to add a new commands to this command line application, you need
    to create a class that inhitered from cliff.Command:
        import cliff


        class NewCommand(cliff.command.Command):
            def get_description(self):
                return "A New command"

            def get_parser(self, prog_name):
                parser = super(NewCommand, self).get_parser(prog_name)
                parser.add_argument('aParameter', nargs='?', default='.')
                return parser

            def take_action(self, parsed_args):
                some = SomeClass()
                some.execute()

    Then add to your setup.py a new entry_point to this class in the
    '{{ cookiecutter.project_slug }}.commandline.commands' namespace
        setuptools.setup(
            .
            entry_points={
                '{{ cookiecutter.project_slug }}.commandline.commands': [
                    'new-command = path.to.new.command:NewCommand',
                ],
            },
        )
    """
    def __init__(self):
        super({{ cookiecutter.project_slug.replace('_', '').capitalize() }}CommandLine, self).__init__(
            description='',
            version='{{ cookiecutter.project_version }}',
            command_manager=CommandManager(
                '{{ cookiecutter.project_slug }}.commandline.commands'),)


def main(argv=sys.argv[1:]):
    app = {{ cookiecutter.project_slug.replace('_', '').capitalize() }}CommandLine()
    return app.run(argv)

if __name__ == '__main__':
    sys.exit(main(argv=sys.argv[1:]))
