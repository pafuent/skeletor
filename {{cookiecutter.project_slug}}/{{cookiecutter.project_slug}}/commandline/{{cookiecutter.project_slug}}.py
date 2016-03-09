import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class SkeletorCommandLine(App):  # pylint: disable=too-few-public-methods
    """Skeletor command line application.
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
    'skeletor.commandline.commands' namespace
        setuptools.setup(
            .
            entry_points={
                'skeletor.commandline.commands': [
                    'new-command = path.to.new.command:NewCommand',
                ],
            },
        )
    """
    def __init__(self):
        super(SkeletorCommandLine, self).__init__(
            description='',
            version='0.1',
            command_manager=CommandManager(
                'skeletor.commandline.commands'),)


def main(argv=sys.argv[1:]):
    app = SkeletorCommandLine()
    return app.run(argv)

if __name__ == '__main__':
    sys.exit(main(argv=sys.argv[1:]))
