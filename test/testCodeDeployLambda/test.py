LAMBDA_NAME = "testCodeDeployLambda"
# Append module path
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.join(os.getcwd(), "src", LAMBDA_NAME, "main.py"))))
# Import origin function
from main import lambda_handler
# Import json, pyttest
import json, pytest

def test_lambda_handler():
  # Set input file path
  iPath = os.path.join(os.getcwd(), "test", LAMBDA_NAME, "input.json")

  # Check input file existance
  if os.path.exists(iPath) == False:
    pytest.fail("Not found input file to test build")

  # Read json file
  with open(os.path.join(os.getcwd(), "test", LAMBDA_NAME, "input.json")) as jsonFile:
    data = {}
    try:
      data = json.load(jsonFile)
    except:
      pytest.fail()
    assert lambda_handler(data, '')['statusCode'] < 400