import cliff

from skeletor.mixins import logger


class DummyCommand(cliff.command.Command, logger.WithLogger):
    def get_description(self):
        return "A dummy command"

    def get_parser(self, prog_name):
        parser = super(DummyCommand, self).get_parser(prog_name)
        parser.add_argument('aParameter', nargs='?', default='.')
        return parser

    def take_action(self, parsed_args):
        self.logger.debug("Debug")
        self.logger.info("Info")
        self.logger.warning("Warning")
        self.logger.error("Error")
        self.logger.critical("Critical")
