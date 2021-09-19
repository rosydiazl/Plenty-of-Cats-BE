#!/bin/bash
# TOKEN="15e037f3d315dbdd0f1fc458814324d533c5e07f" USERID="24" PROFILEID="48" sh curl-scripts/likes/create.sh 

curl "http://localhost:8000/likes/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "likes": {
      "user_id": "'"${USERID}"'",
      "profile_id": "'"${PROFILEID}"'"
    }
  }'

echo
