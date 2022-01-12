#!/bin/bash
# sends delete request passed as $1 
curl -s "$1" -X DELETE
