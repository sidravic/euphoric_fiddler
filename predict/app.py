from fastai.core import download_url
from fastai.basic_train import load_learner
from fastai.vision.image import open_image
import boto3
import os


url = 'https://n.nordstrommedia.com/id/sr3/788c04da-6604-4a83-ac44-1f10b214a97e.jpeg?crop=pad&pad_color=FFF&format=jpeg&w=1660&h=2546'
url2 = 'https://i.ebayimg.com/images/g/csAAAOSwkmJcs409/s-l300.jpg'

download_url(url, dest='lhomme.jpg', show_progress=True, overwrite=False)
download_url(url2, dest='glycolic_facial_cleanser_anthony.jpg', show_progress=True, overwrite=False)


S3_ACCESS_KEY_ID = os.environ['S3_ACCESS_KEY']
S3_SECRET_ACCESS_KEY = os.environ['S3_SECRET_ACCESS_KEY']
BUCKET_NAME = os.environ['MODEL_BUCKET_NAME']


s3_client = boto3.client('s3',
                         aws_access_key_id=S3_ACCESS_KEY_ID,
                         aws_secret_access_key=S3_SECRET_ACCESS_KEY)

#s3_client.download_file(BUCKET_NAME, 'saved_models/internal_v4_subset/export-stage-1', 'export-stage-1')
predict_learner = load_learner(path='.', file='export-stage-1')
img = open_image('lhomme.jpg')
img2 = open_image('glycolic_facial_cleanser_anthony.jpg')
prediction = predict_learner.predict(img)
print(prediction)
