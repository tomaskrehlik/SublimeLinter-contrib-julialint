#!/bin/bash

(echo ${1}; sleep 4) | nc -w 4 localhost 2222