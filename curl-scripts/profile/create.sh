#!/bin/bash
# TOKEN="700997adfb4b1b4b7e6e0889827514d4dfbaf4fc" NAME="Ford" AGE=5 BREED="RB" BIO="Loves food" IMAGES=pic.png sh curl-scripts/profile/create.sh 

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
      "images": "'"${IMAGES}"'"
    }
  }'

echo
