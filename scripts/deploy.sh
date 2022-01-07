#!/bin/bash

# Install jq
curl -L https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 -o /usr/local/bin/jq
chmod a+x /usr/local/bin/jq

# Extract the lambda alias version
aws lambda get-alias --function-name $DEPLOY_LAMBDA_NAME --name $DEPLOY_LAMBDA_ALIAS > lambda-alias.json
# Extract the current version for this lambda alias
CURRENT_LAMBDA_ALIAS_VERSION=$(cat lambda-alias.json | jq -r '.FunctionVersion')

# Create the directory for output
mkdir dist
# Move the directory for source code
cd src
# Compress the source code
zip -r -u -q ../dist/source.zip *
# Move the upper directory
cd ..
# Upload source for lambda function
aws lambda update-function-code --function-name $DEPLOY_LAMBDA_NAME --zip-file fileb://dist/source.zip --publish > update-lambda.json

# Extract last version for lambda function
LATEST_VERSION=$(cat update-lambda.json | jq -r '.Version')
if [[ $CURRENT_LAMBDA_ALIAS_VERSION -ge $LATEST_VERSION ]]; then
  exit 0
fi

# Create appspec file in s3 bucket to create a deployment for AWS CodeDeploy
cat > appspec.yml <<- EOM
version: 0.0
Resources:
  - deployLambda:
      Type: AWS::LAMBDA::FUNCTION
      Properties:
        Name: "$DEPLOY_LAMBDA_NAME"
        Alias: "$DEPLOY_LAMBDA_ALIAS"
        CurrentVersion: "$CURRENT_LAMBDA_ALIAS_VERSION"
        TargetVersion: "$LATEST_VERSION"
EOM
aws s3 ls s3://$S3_BUCKET/
# Upload appspec file in s3 bucket
aws s3 cp ./appspec.yml s3://$S3_BUCKET/codeDeploy/