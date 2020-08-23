# import face_api_client
#
#
# class FaceProvider(object):
#
#     def get_biggest_person_group(api_client, faces_list):
#         biggest_person_group = []
#         while temp_faces_list:
#             face = temp_faces_list[0]
#             cur_group = api_client.recognize_similar_faces(face, temp_faces_list[1:])
#             if cur_group and len(cur_group) > len(biggest_person_group):
#                 biggest_person_group = cur_group
#                 biggest_person_group.append(face)
#                 temp_faces_list = [x for x in temp_faces_list if x not in cur_group]
#             temp_faces_list = temp_faces_list[1:]
#         return biggest_person_group
#
#
#
#     def detect_image_faces(self, image_path):
#         response = face_api_client.detect_faces(image_path)
#         if not response:
#             return None
#         return response
#
#
#
#     def find_largest_person_image(person_faces ,all_images_faces, face_image_resolution):
#         best_image = None
#         best_resolution = 0
#
#         for fa in person_faces():
#             # get the detectedFace object form the similarFace list by face_id
#             detected_face = next((x for x in all_images_faces if x.face_id == fa.face_id), None)
#             if detected_face:
#                 cur_res = face_image_resolution[detected_face.face_id]
#                 picture_surface_area = cur_res[0] * cur_res[1]
#                 face_box_surface_area = detected_face.face_rectangle.height * detected_face.face_rectangle.width
#                 if face_box_surface_area / picture_surface_area > best_resolution:
#                     best_resolution = face_box_surface_area / picture_surface_area
#                     best_image = detected_face
#         return best_image
