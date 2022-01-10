LAMBDA_NAME = "testCodeDeployLambda"
# Append module path
import sys, os, pytest
sys.path.append(os.path.dirname(os.path.abspath(os.path.join(os.getcwd(), "src", LAMBDA_NAME, "main.py"))))
# Import origin function
from main import lambda_handler
# Import json
import json

def test_lambda_handler():
  # Read json file
  try:
    with open(os.path.join(os.getcwd(), "..", LAMBDA_NAME, "input.json")) as jsonFile:
      data = json.load(jsonFile)
      assert lambda_handler(data, '')['statusCode'] < 400
  except: 
    return pytest.ExitCode.TESTS_FAILED