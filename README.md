 SublimeLinter-contrib-julialint
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-julialint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-julialint)

## Temporary

Because this is still a development version, the repository is not in package control and you have to manually add this repository. To do that:

- Open command palette (`Cmd + Shift + P` on Mac)
- Search for Add repository.
- Paste URL of this page.
- Now you can install the package.

## About

This linter plugin for [SublimeLinter][docs] provides an interface to [julialint](https://github.com/tonyhffong/Lint.jl). It will be used with files that have the “julia” syntax. Currently, it takes some time until it lints, because of the start-up time of the linter, but it should improve with time independently of this linter.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that you have a usable instance of `julia` and have installed a `Lint` package. To install `Lint`, do the following:

1. Open Julia.

2. Input the following:
   ```
   Pkg.update()
   Pkg.add("Lint")
   ```

### Linter configuration

To make it working you need to specify path to your executable of `Julia` and edit the script within the package content. Do the following:

1. Go to `Sublime Text -> Preferences -> Browse packages...`

2. Navigate to the `SublimeLinter-contrib-julialint`. Depending on your platform you will edit either `osx.sh`, `linux.sh`, or `windows.bat`. The typical paths look as follows
    - **OS X**: `/Applications/Julia-0.3.5.app/Contents/Resources/julia/bin/julia` if you have the binaries (the number changes based on the version), or just `julia` if you have it exported to your path.
    - **Linux**: `julia`, most probably it will be exported to your PATH.
    - **Windows**: you should locate julia.exe

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `julialint`. Among the entries you should see `SublimeLinter-contrib-julialint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
There are no settings so far.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
