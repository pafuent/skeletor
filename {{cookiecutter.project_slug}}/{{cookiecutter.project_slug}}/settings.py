from logging import config
import os


USER_PATH = os.path.expanduser("~")

# The following escape codes are made availible for use in the format string:
# {color}, fg_{color}, bg_{color}:
#   Foreground and background colors.
#   The color names are black, red, green, yellow, blue, purple, cyan and white
# bold, bold_{color}, fg_bold_{color}, bg_bold_{color}: Bold/bright colors.
# reset: Clear all formatting (both foreground and background colors).
LOGGER_NAME = '{{ cookiecutter.project_slug }}'
LOG_DIR = USER_PATH
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)-8s %(thread)d %(message)s',
        },
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s %(levelname)-8s %(thread)d %(message)s',
            'log_colors': {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'colored',
        },
        'to_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, '{0}.log'.format(LOGGER_NAME)),
            'when': 'D',
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        LOGGER_NAME: {
            'handlers': ['console', 'to_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

config.dictConfig(LOGGING)
