# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
import os

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

if __name__ == "__main__":

    KEY = os.environ['FACE_SUBSCRIPTION_KEY']

    # Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
    # This endpoint will be used in all examples in this quickstart.
    ENDPOINT = os.environ.get('FACE_ENDPOINT')

    __client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    __client.face.detect_with_stream()