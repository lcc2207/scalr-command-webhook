#!/bin/bash

echo "testing-=-=-==-=-=-=-="
echo $1
echo $2
echo $3
scalrhostname=$(echo $4 | jq '.SCALR_SERVER_HOSTNAME')
echo $scalrhostname
echo "-=-=-=-=-=-=-=-=-=-=-=-=-=-"
