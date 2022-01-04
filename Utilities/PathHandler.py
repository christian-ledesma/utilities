from inspect import stack
from os import path

class PathHandler:

    def get_current_path():
        """
        params: Get caller file's path
        """
        a = path.abspath(stack()[1].filename)
        return path.dirname(a)
