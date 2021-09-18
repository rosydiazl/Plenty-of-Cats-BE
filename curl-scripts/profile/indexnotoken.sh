#!/bin/bash
# TOKEN="38529e9742ae661e27b53ce040fcfe4916cd0045" sh curl-scripts/profile/indexnotoken.sh

curl "http://localhost:8000/profiles/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
