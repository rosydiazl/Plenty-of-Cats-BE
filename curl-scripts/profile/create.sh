#!/bin/bash
# TOKEN="c1bd351f83f4ff039f0f399d23bdf05b76cbf9d7" NAME="Ford" AGE="10" BREED="Cat" BIO="dsdsd" IMAGE="ddfsfsd" sh curl-scripts/profile/create.sh 

curl "http://localhost:8000/profiles/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "profile": {
      "name": "'"${NAME}"'",
      "age": "'"${AGE}"'",
      "breed": "'"${BREED}"'",
      "bio": "'"${BIO}"'",
      "image": "'"${IMAGE}"'"
    }
  }'

echo
