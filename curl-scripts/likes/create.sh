#!/bin/bash
# TOKEN="d4fa7575bacaae801c7a421d9ef40f0a2a1b6acc" USERID="18" PROFILEID="2" sh curl-scripts/likes/create.sh

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
