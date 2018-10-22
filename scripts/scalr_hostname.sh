#!/bin/bash

scalrhostname="scalr$(echo $((1 + RANDOM % 9))$((1 + RANDOM % 9)))"
echo $scalrhostname
