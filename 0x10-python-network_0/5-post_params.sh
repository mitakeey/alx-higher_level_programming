#!/bin/bash
# POST request with message and display response body
curl -X POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' '$1'
