#!/bin/bash
/Applications/Julia-0.3.5.app/Contents/Resources/julia/bin/julia -e "using Lint; lintfile(\"$1\")"