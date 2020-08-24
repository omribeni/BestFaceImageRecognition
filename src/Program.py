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


@app.route("/GetBestImage", methods=['POST'])
def GetBestImage():
    data = request.get_data()
    if not data:
        raise BadRequest(400, 'Bad input data')

    try:
        images = Utils.parse_json_images_data(data)
        if images:
            all_images_faces = []
            face_to_original_image_resolution_map = defaultdict()
            for path in images:
                cur_image_faces = azure_face_api_client.detect_image_faces(path)
                if cur_image_faces:
                    img_size = Utils.get_image_resolution(path)
                    for face in cur_image_faces:
                        face_to_original_image_resolution_map[face.face_id] = img_size

                    all_images_faces.extend(cur_image_faces)

            if all_images_faces:
                temp_faces_list = all_images_faces
                most_popular_person_images = azure_face_api_client.get_most_popular_face_images(temp_faces_list)

                best_image = azure_face_api_client.get_best_resolution_face_image(most_popular_person_images, all_images_faces,
                                                            face_to_original_image_resolution_map)
                if best_image:
                    return json.loads(json.dumps(best_image, default=lambda o: o.__dict__))
                else:
                    return 'failed retrieving bestImage', 400
            else:
                return 'No faces found in images', 400

    except Exception as e:
        return str(e), 400

    else:
        return 'No images given. please pass local images path as requested', 400


if __name__ == '__main__':
    azure_face_api_client = FaceApiClient()
    app.run()
