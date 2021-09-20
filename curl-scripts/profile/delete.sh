#!/bin/bash
# TOKEN="b2cc5502785f614a4f4eeeb3dc69afcea886c78e" ID="1" sh curl-scripts/likes/delete.sh 

curl "http://localhost:8000/profiles/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
