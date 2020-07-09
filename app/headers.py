from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from app import app



prediction_key = "ffdd7ab5e60a4d71aa930e2b813b5b29"
publish_iteration_name = "Iteration1"
ENDPOINT = "https://face-mask-prediction.cognitiveservices.azure.com/"
projectId = "b79cbed0-0df7-48c1-b04c-e8b6af4ed26e"
# prediction_key = "your-prediction key"
# publish_iteration_name = "classifyModel"
# ENDPOINT = "your-endpoint"
# projectId = "your project id"
