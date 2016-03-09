import logging

from skeletor import settings


# pylint: disable=too-few-public-methods
class WithLogger(object):
    LOGGER_NAME = settings.LOGGER_NAME

    @staticmethod
    def build(logger_name):
        return type(
            "WithLogger_{0}".format(logger_name), (WithLogger,),
            {"LOGGER_NAME": logger_name})

    @property
    def logger(self, logger_name=None):  # pylint: disable=no-self-use
        return logging.getLogger(
            logger_name if logger_name else self.LOGGER_NAME)
