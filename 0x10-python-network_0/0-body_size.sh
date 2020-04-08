#!/bin/bash
#test
curl -Is "$1" | grep "Content-Length:" | cut -c 17-
