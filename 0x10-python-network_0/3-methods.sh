#!/bin/bash
#test
curl -Is "$1" | grep "Allow:" | cut -c 8-
