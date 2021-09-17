#!/bin/bash
# TOKEN="13f2f110767c3ba916e2df8806803ff8da747b17" sh curl-scripts/profile/index.sh

curl "http://localhost:8000/profiles/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
