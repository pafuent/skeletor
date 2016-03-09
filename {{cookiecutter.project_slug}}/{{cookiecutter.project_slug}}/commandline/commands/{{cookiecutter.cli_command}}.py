import cliff

from {{ cookiecutter.project_slug }}.mixins import logger


class {{ cookiecutter.cli_command.replace('-', '').replace('_', '') }}Command(cliff.command.Command, logger.WithLogger):
    def get_description(self):
        return "{{ cookiecutter.cli_command }} command"

    def get_parser(self, prog_name):
        parser = super({{ cookiecutter.cli_command.replace('-', '').replace('_', '') }}Command, self).get_parser(prog_name)
        parser.add_argument('aParameter', nargs='?', default='.')
        return parser

    def take_action(self, parsed_args):
        self.logger.debug("Debug")
        self.logger.info("Info")
        self.logger.warning("Warning")
        self.logger.error("Error")
        self.logger.critical("Critical")
