
# Deploy Model ML
gcloud builds submit --tag gcr.io/deploy-model1/fast-api:latest .

gcloud run deploy fast-api:latest \
    --image gcr.io/deploy-model1/fast-api:latest \
    --platform managed \
    --allow-unauthenticated


gcr.io/deploy-model1/

gcloud builds submit --config=cloudbuild.yaml \
  --substitutions=_LOCATION="us-east1",_REPOSITORY="fast-api",_IMAGE="fast-api:latest" .