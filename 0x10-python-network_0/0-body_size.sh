#!/bin/bash
url=$1
curl -s -o /dev/null -w '%{size_download}\n' "$url"
