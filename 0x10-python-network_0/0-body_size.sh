#!/bin/bash
#script to show the size of download body
curl -s -o /dev/null -w '%{size_download}\n' "$1"
