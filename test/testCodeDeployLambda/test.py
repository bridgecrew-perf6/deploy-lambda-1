# Append module path
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.getcwd() + "/src/testCodeDeployLambda/main.py")))
# Import origin function
from main import lambda_handler

def test_lambda_handler():
  assert lambda_handler({}, '')['statusCode'] < 400