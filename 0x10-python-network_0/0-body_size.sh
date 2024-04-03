#!/bin/bash
# obtain the size in byte of HTTP header for a given URL
curl -s "$1" | wc -c
