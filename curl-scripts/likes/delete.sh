#!/bin/bash
# TOKEN="f7fc21a20196a17b49f35ce07feba2f37277b927" ID="3" sh curl-scripts/profile/delete.sh
# TOKEN 1c36a8218db850aeaf9a6d418e9051ed49ca5bc6
# USER ID = 24
# USER PROFILE ID = 47

curl "http://localhost:8000/likes/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
