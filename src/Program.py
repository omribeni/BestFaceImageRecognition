# import requests
import json
from collections import defaultdict

from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest
from face_api_client import FaceApiClient
from src.utils import Utils

app = Flask(__name__)
@app.route("/")
def welcome():
    return render_template("index.html")




@app.route("/GetBestImage", methods = ['POST'])
def GetBestImage():
    data = request.get_data()
    if not data:
        raise BadRequest(400, 'Bad input data')
    images = Utils.parse_json_images_data(data)

    if images:
        all_images_faces = []
        face_image_resolution = defaultdict()
        for path in images:
            cur_image_faces = azure_face_api_client.detect_image_faces(path)
            if cur_image_faces:
                img_size = Utils.get_image_resolution(path)
                for face in cur_image_faces:
                    face_image_resolution[face.face_id] = img_size

                # aggregate to faces lists
                all_images_faces.extend(cur_image_faces)

        if all_images_faces:
            temp_faces_list = all_images_faces
            biggest_person_group = get_biggest_person_group(temp_faces_list)

            best_image = find_largest_person_image(biggest_person_group, all_images_faces, face_image_resolution)
            if best_image:
                return json.dumps(best_image.face_id)
            else:
                raise BadRequest('failed retreiving bestImage')
        else:
            return 'No faces found in images'
    else:
        return 'No images given. please pass local images path as requested'


def get_biggest_person_group(faces_list):
    biggest_person_group = []
    while faces_list:
        face = faces_list[0]
        cur_group = azure_face_api_client.recognize_similar_faces(face, faces_list[1:])
        if cur_group and len(cur_group) > len(biggest_person_group):
            biggest_person_group = cur_group
            biggest_person_group.append(face)
            faces_list = [x for x in faces_list if x not in cur_group]
        faces_list = faces_list[1:]
    return biggest_person_group


def find_largest_person_image(person_faces, all_faces, image_resolution):
    best_image = None
    best_resolution = 0

    for fa in person_faces:
        # get the detectedFace object form the similarFace list by face_id
        detected_face = next((x for x in all_faces if x.face_id == fa.face_id), None)
        if detected_face:
            cur_res = image_resolution[detected_face.face_id]
            picture_surface_area = cur_res[0] * cur_res[1]
            face_box_surface_area = detected_face.face_rectangle.height * detected_face.face_rectangle.width
            if face_box_surface_area / picture_surface_area > best_resolution:
                best_resolution = face_box_surface_area / picture_surface_area
                best_image = detected_face
    return best_image



if __name__ == '__main__':
    azure_face_api_client = FaceApiClient()
    app.run()


    # try:
    #     x['c']
    # except Exception as e:
    #     print(f'c does not exist: {str(e)}' + '{0} {1}'.format('asdf', 'a'))
    # finally:
    #     print(1)

