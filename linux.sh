#!/bin/bash
julia -e "using Lint; lintfile(\"$1\")"
