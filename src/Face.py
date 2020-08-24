class FaceFields(object):
    AGE = "age"
    GENDER = "gender"
    HEAD_POSE = "headPose"
    SMILE = "smile"
    FACIAL_HAIR = "facialHair"
    GLASSES = "glasses"
    EMOTION = "emotion"
    HAIR = "hair"
    MAKEUP = "makeup"
    OCCLUSION = "occlusion"
    ACCESSORIES = "accessories"

    @classmethod
    def all(cls):
        return [
            cls.AGE, cls.GENDER, cls.HEAD_POSE, cls.SMILE, cls.FACIAL_HAIR, cls.GLASSES, cls.EMOTION, cls.MAKEUP,
            cls.HAIR, cls.OCCLUSION, cls.ACCESSORIES
        ]
