import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from twilio.rest import Client
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
app = Flask(__name__)
model = load_model(
    "/Users/aishaandatt/Downloads/ANIMAL_WILDHACKS/alert.h5")


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        phone = request.form.get('phone')
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        filepath = os.path.join(basepath, 'uploads', f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)

        img = image.load_img(filepath, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        preds = model.predict(x)

        print("prediction", preds)
        index = ['antelope',
                 'badger',
                 'bat',
                 'bear',
                 'bee',
                 'beetle',
                 'bison',
                 'boar',
                 'butterfly',
                 'cat',
                 'caterpillar',
                 'chimpanzee',
                 'cockroach',
                 'cow',
                 'coyote',
                 'crab',
                 'crow',
                 'deer',
                 'dog',
                 'dolphin',
                 'donkey',
                 'dragonfly',
                 'duck',
                 'eagle',
                 'elephant',
                 'flamingo',
                 'fly',
                 'fox',
                 'goat',
                 'goldfish',
                 'goose',
                 'gorilla',
                 'grasshopper',
                 'hamster',
                 'hare',
                 'hedgehog',
                 'hippopotamus',
                 'hornbill',
                 'horse',
                 'hummingbird',
                 'hyena',
                 'jellyfish',
                 'kangaroo',
                 'koala',
                 'ladybugs',
                 'leopard',
                 'lion',
                 'lizard',
                 'lobster',
                 'mosquito',
                 'moth',
                 'mouse',
                 'octopus',
                 'okapi',
                 'orangutan',
                 'otter',
                 'owl',
                 'ox',
                 'oyster',
                 'panda',
                 'parrot',
                 'pelecaniformes',
                 'penguin',
                 'pig',
                 'pigeon',
                 'porcupine',
                 'possum',
                 'raccoon',
                 'rat',
                 'reindeer',
                 'rhinoceros',
                 'sandpiper',
                 'seahorse',
                 'seal',
                 'shark',
                 'sheep',
                 'snake',
                 'sparrow',
                 'squid',
                 'squirrel',
                 'starfish',
                 'swan',
                 'tiger',
                 'turkey',
                 'turtle',
                 'whale',
                 'wolf',
                 'wombat', 'woodpecker',
                 'zebra',
                 'human']

        print(np.argmax(preds))

        text = "the predicted animal is : " + str(index[np.argmax(preds)])
        if np.argmax(preds) == 11:
            # twilio account ssid
            account_sid = 'AC4cxxxxxx'
            # twilo account authentication toke
            auth_token = '6bf1xxxxxx'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body='Danger!. Wild animal is detected, stay alert',
                    from_='+18125794545',  # the free number of twilio
                    to=phone)
            print(message.sid)
            print('Danger!!')
            print('Animal Detected')
            print('SMS sent!')
        else:
            print("No Danger")
       # break
    return text


if __name__ == '__main__':
    app.run(host='192.168.29.83')
    # debug=True, threaded=False)
