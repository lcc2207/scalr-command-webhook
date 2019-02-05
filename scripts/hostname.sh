#!/bin/bash

ARRAY=(Dev QA PROD)
ARRNUM=$(( ( RANDOM % 3 )  -1 ))
NUMBER=$(( ( RANDOM % 10 )  + 1 ))
name=${ARRAY[$ARRNUM]}_$NUMBER
echo "{\"hostname\": \"$name\"}"
