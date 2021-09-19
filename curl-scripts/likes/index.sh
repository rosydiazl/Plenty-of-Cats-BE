#!/bin/bash
# TOKEN="0a5e60a85cfdc61c57f76a934923d9e82150a2a0" sh curl-scripts/likes/index.sh

curl "http://localhost:8000/likes/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
