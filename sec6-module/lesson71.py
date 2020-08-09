try:
    from lesson68_package import utils
except ImportError:
    from lesson68_package.tools import utils

print(utils.say_twice('word'))