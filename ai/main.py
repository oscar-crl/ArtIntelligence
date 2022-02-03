import os
import tensorflow as tf
import imageLoader
import StyleContent
from utils import tensor_to_image
import tensorflow_hub as hub

os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img


def fuse_images(content_path, style_path):
    content_image = load_img(content_path)
    style_image = load_img(style_path)

    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    tensor_to_image(stylized_image).save('./tmp.jpg')


try:
    loadedImages = imageLoader.imageLoader('apple')
    fuse_images(loadedImages[0].path, loadedImages[1].path)
    for x in range(2, len(loadedImages)):
        fuse_images('download/nice/tmp.jpg', loadedImages[x].path)


except ValueError:
    print(ValueError)



