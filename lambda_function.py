name: Deploy Static Website to S3

on:
  push:
    branches:
      - main  # Trigger deploy when pushing to main branch

jobs:
  deploy:
    name: Upload Static Files to S3
    runs-on: ubuntu-latest

    steps:
      # Step 1: Checkout your repository code
      - name: Checkout repository
        uses: actions/checkout@v4

      # Step 2: Sync all static files to your S3 bucket
      - name: Deploy static site to S3
        uses: jakejarvis/s3-sync-action@v0.5.1
        with:
          args: --delete
        env:
          AWS_S3_BUCKET: ${{ secrets.S3_BUCKET_NAME }}
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_REGION: ${{ secrets.AWS_REGION }}
          SOURCE_DIR: .  # Upload everything in the repo root (index.html, style.css, images/)
