#!/bin/bash
# sends request to URL and displays size of the body in response

curl -s ${URL} | grep -i content-length | wc -c
