#!/usr/bin/env bash
set -euo pipefail
mkdir -p results
COLLECTION=../postman/NeoCommerce.postman_collection.json
ENV=../postman/NeoCommerce.postman_environment.json

newman run "$COLLECTION" -e "$ENV" --reporters cli,json --reporter-json-export results/newman_results.json || exit 1

if newman run --help 2>/dev/null | grep -q htmlextra; then
  newman run "$COLLECTION" -e "$ENV" -r htmlextra --reporter-htmlextra-export results/report.html
fi

echo "Done. Results in newman/results/"
