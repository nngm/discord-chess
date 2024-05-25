#!/bin/bash

echo "Please enter your bot token:"
read token

cat <<EOF >__token__.py
token = "$token"
EOF

echo "__token__.py file generated."