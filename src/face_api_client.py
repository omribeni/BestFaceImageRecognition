import os
from collections import defaultdict

import PIL
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials


class FaceApiClient(object):

    # Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
    KEY = os.environ.get('FACE_SUBSCRIPTION_KEY')

    # Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
    ENDPOINT = os.environ.get('FACE_ENDPOINT')
    def __init__(self):
            self.__client = None


    def detect_image_faces(self,image_path):
        response = self.analyze_image(image_path)
        if not response:
            return None
        return response


    def recognize_similar_faces(self ,face, all_faces):
        face_ids = [f.face_id for f in all_faces]
        if face_ids:
            response = self.__client.face.find_similar(face.face_id ,face_ids=face_ids)
            return response
        return []


    def analyze_image(self, image_path):
        # init on demand
        self.__initialize()
        try:
            # convert local image to stream
            file_path = image_path.replace('/', '\\')
            with open(file_path, "rb") as image_bytes_stream:
                return self.__client.face.detect_with_stream(image_bytes_stream,return_face_attributes=["age","gender","headPose","smile","facialHair","glasses","emotion","hair","makeup","occlusion","accessories"], detection_model="detection_01", return_face_landmarks=True)
        except Exception as e:
            return None


    @property
    def client(self):
        if not self.__client:
            self.__initialize()

        return self.__client


    def __initialize(self):
        if not self.__client:
            # Create an authenticated FaceClient.
            self.__client = FaceClient(self.ENDPOINT, CognitiveServicesCredentials(self.KEY))






