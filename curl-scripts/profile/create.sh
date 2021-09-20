#!/bin/bash
# TOKEN="38529e9742ae661e27b53ce040fcfe4916cd0045" NAME="Lise" AGE="6" BREED="df" BIO="sd" sh curl-scripts/profile/create.sh

curl "http://localhost:8000/userprofile/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "profile": {
      "name": "'"${NAME}"'",
      "age": "'"${AGE}"'",
      "breed": "'"${BREED}"'",
      "bio": "'"${BIO}"'"
    }
  }'

echo
