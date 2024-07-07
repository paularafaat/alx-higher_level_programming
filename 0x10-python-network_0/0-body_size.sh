#!/bin/bash
#script to show the size of download body
url=$1
curl -s -o /dev/null -w '%{size_download}\n' "$url"
