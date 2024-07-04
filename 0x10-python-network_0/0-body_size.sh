#!/bin/bash
# Takes in a URL and sends a request to it
curl -s $1 | wc -c