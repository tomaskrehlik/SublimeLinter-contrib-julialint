#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Tomas Krehlik
# Copyright (c) 2014 Tomas Krehlik
#
# License: MIT
#

"""This module exports the Julialint plugin class."""

from SublimeLinter.lint import Linter, util
from os.path import dirname, realpath
# import sublime


class Julialint(Linter):

    """Provides an interface to julialint."""

    syntax = 'julia'
    executable = 'julia'
    regex = r'(?P<file>^.*\.jl):(?P<line>\d{1,4}) \[(?P<func>.*)\] ((?P<error>ERROR)|(?P<warning>WARN)) (?P<message>.*)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = "jl"
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    comment_re = r'#'
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None

    def cmd(self):
        """Return a list with the command line to execute."""

        command = 'using Lint; lintfile(ARGS[1])'
        print([self.executable_path, '-e', command])
        return ['julia',
                '-e',
                command]