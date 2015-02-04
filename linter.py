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
import sublime


class Julialint(Linter):

    """Provides an interface to julialint."""

    syntax = 'julia'
    plat = sublime.platform()
    if plat=='osx':
        cmd = "\"" + dirname(realpath(__file__)) + '/osx.sh\"'
    elif plat=='linux':
        cmd = "\"" + dirname(realpath(__file__)) + '/linux.sh\"'
    else:
        cmd = "\"" + dirname(realpath(__file__)) + '/windows.bat\"'

    executable = None
    regex = r'(?P<file>^.*\.jl):(?P<line>\d{1,4}) \[(?P<func>.*)\] ((?P<error>ERROR)|(?P<warning>WARN)) (?P<message>.*)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = "jl"
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None