import os
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

import Face


class FaceApiClient(object):
    # Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
    # KEY = os.environ.get('FACE_SUBSCRIPTION_KEY')
    KEY = "b5d8f11828cb4b40a4c9ebb725caf4b2"

    # Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
    ENDPOINT ="https://vizbestimageresult.cognitiveservices.azure.com/"
    # os.environ.get('FACE_ENDPOINT')

    def __init__(self):
        self.__client = None

    def __initialize(self):
        if not self.__client:
            # Create an authenticated FaceClient.
            self.__client = FaceClient(self.ENDPOINT, CognitiveServicesCredentials(self.KEY))

    @property
    def client(self):
        if not self.__client:
            self.__initialize()

        return self.__client

    def detect_image_faces(self, image_path):
        response = self.analyze_image(image_path)
        if not response:
            return None

        return response

    def recognize_similar_faces(self, face, all_faces):
        face_ids = [f.face_id for f in all_faces]
        if face_ids:
            response = self.__client.face.find_similar(face.face_id, face_ids=face_ids)
            return response

        return []

    def analyze_image(self, image_path):
        # init on demand
        self.__initialize()
        try:
            # convert local image to stream
            # file_path = image_path.replace('/', '\\')
            with open(image_path, "rb") as image_bytes_stream:
                return self.__client.face.detect_with_stream(image_bytes_stream,
                                                             return_face_attributes=Face.FaceFields.all(),
                                                             detection_model="detection_01", return_face_landmarks=True)

        except Exception as e:
            return None

    def get_most_popular_face_images(self, faces_list):
        biggest_person_group = []
        while faces_list:
            face = faces_list[0]

            cur_group = [face]
            # add all similar faces of the current face
            cur_group.extend(self.recognize_similar_faces(face, faces_list[1:]))
            if cur_group and len(cur_group) > len(biggest_person_group):
                biggest_person_group = cur_group

            # remove all of the current group members from the faces list
            faces_list = [x for x in faces_list if x not in cur_group]
        return biggest_person_group

    @classmethod
    def get_best_resolution_face_image(cls, person_faces, all_faces, face_to_resolution_map):
        best_image = None
        best_resolution = 0

        for face in person_faces:
            # get the detectedFace object form the similarFace list by face_id
            detected_face = next((x for x in all_faces if x.face_id == face.face_id), None)
            if detected_face:
                cur_res = face_to_resolution_map[detected_face.face_id]
                picture_surface_area = cur_res[0] * cur_res[1]
                face_box_surface_area = detected_face.face_rectangle.height * detected_face.face_rectangle.width
                current_resolution = face_box_surface_area / picture_surface_area
                if current_resolution > best_resolution:
                    best_resolution = current_resolution
                    best_image = detected_face

        return best_image
