#!/bin/bash
# TOKEN="c1bd351f83f4ff039f0f399d23bdf05b76cbf9d7" ID="1" sh curl-scripts/profile/show.sh

curl "http://localhost:8000/likes/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
