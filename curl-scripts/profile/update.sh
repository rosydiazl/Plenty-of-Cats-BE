#!/bin/bash
# TOKEN="f7fc21a20196a17b49f35ce07feba2f37277b927" ID="2" NAME="Lisa" AGE="11" BREED="Cat" BIO="Loves" IMAGE="Lol" sh curl-scripts/profile/update.sh

curl "http://localhost:8000/profiles/${ID}/" \
  --include \
  --request PATCH \
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
