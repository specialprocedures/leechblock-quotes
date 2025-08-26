#!/bin/bash
# Usage: ./deploy.sh <GCP_PROJECT_ID> [REGION]
# Example: ./deploy.sh my-gcp-project us-central1

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <GCP_PROJECT_ID> [REGION]"
  exit 1
fi

PROJECT_ID="$1"
REGION="${2:-europe-west2}"
SERVICE_NAME="leechblock-quotes"
IMAGE="gcr.io/$PROJECT_ID/$SERVICE_NAME"

# Build and push the container image
gcloud builds submit --project "$PROJECT_ID" --tag "$IMAGE"

# Deploy to Cloud Run with minimal resources and concurrency

gcloud run deploy "$SERVICE_NAME" \
  --image "$IMAGE" \
  --platform managed \
  --region "$REGION" \
  --memory 256Mi \
  --cpu 1 \
  --concurrency 1 \
  --max-instances 1 \
  --allow-unauthenticated \
  --port 5000

echo "\nDeployed! Visit the Cloud Run service in the GCP Console to get your URL."
