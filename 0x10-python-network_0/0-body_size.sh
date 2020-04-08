#!/bin/bash
#test
curl -Is 0.0.0.0:5000 | grep "Content-Length:" | cut -c 17-
