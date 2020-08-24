# import json
#
#
# class Face(object):
#
#     def __init__(self, detectedFace):
#
#
#     @classmethod
#     def __to_dict(cls, obj):
#         return obj.__dict__
#
#     def to_dict(obj):
#         return json.loads(json.dumps(obj, default=lambda o: o.__dict__))
#
#     @property
#     def face_id(self):
#         return self.__face_id
#
#     @property
#     def face_landmarks(self):
#         return self.__face_landmarks
#
#     @property
#     def face_attributes(self):
#         return self.__face_attributes
#     #
#     # @property
#     # def smile(self):
#     #     return self.__smile
#     #
#     # @property
#     # def emotion(self):
#     #     return self.__emotion
#     #
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # def print_name(self):
#     #     print(self.__name)
#     #
#     # @classmethod
#     # def print_age(cls):
#     #     print(cls.age)