#!/bin/bash
# sends request to URL and displays size of the body in response
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
