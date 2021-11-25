from io import BytesIO
import numpy as np
# import tensorflow as tf
from PIL import Image
# from tensorflow.keras.applications.imagenet_utils import decode_predictions

# model = None

# def load_model():
#     model = tf.keras.applications.MobileNetV2(weights="imagenet")
#     print("Model loaded")
#     return model


def predict(image: Image.Image):
    # global model
    # if model is None:
    #     model = load_model()
    img_size=image.size
    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0
    img_resize=image.shape
    # result = decode_predictions(model.predict(image), 2)[0]
    result=[[img_size,img_resize,0.5],]

    response = []
    for i, res in enumerate(result):
        resp = {}
        resp["img_size"] = res[0]
        resp["img_resize"] = res[1]
        resp["confidence"] = f"{res[2]*100:0.2f} %"
        # resp["class"] = res[1]
        # resp["confidence"] = f"{res[]*100:0.2f} %"

        response.append(resp)

    return response


def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image