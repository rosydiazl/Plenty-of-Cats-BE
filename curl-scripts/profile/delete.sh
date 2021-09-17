#!/bin/bash
# TOKEN="f7fc21a20196a17b49f35ce07feba2f37277b927" ID="3" sh curl-scripts/profile/delete.sh 

curl "http://localhost:8000/profiles/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
