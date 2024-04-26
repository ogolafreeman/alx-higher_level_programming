#!/bin/bash
# Bash script send a request to an URL with curl,
# and displays the size of the body of the response
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

response=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

# Display the size of the response body
echo "Size of the response body: $response bytes"

