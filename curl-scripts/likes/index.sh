#!/bin/bash
# TOKEN="15e037f3d315dbdd0f1fc458814324d533c5e07f" USERID="24" PROFILEID="48" sh curl-scripts/likes/index.sh 

curl "http://localhost:8000/likes/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
