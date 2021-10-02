# import opencv
import cv2
# import numpy
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
# import Client from twilio API
from twilio.rest import Client

model = load_model(
    '/Users/aishaandatt/Downloads/ANIMAL_WILDHACKS/alert.h5')
# To read webcam
video = cv2.VideoCapture(0)
# Type of classes or names of the labels that we considered
name = ['antelope',
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
# To execute the program repeatedly using while loop
while(1):
    success, frame = video.read()
    cv2.imwrite("image.jpg", frame)
    img = image.load_img("image.jpg", target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    pred = model.predict_classes(x)
    p = pred[0]
    # print(pred)
    cv2.putText(frame, "predicted  class = "+str(name[p]), (100, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

    pred = model.predict_classes(x)
    if pred[0] == 2:
        # twilio account ssid
        account_sid = 'AC4c30xxxxxxx'
        # twilo account authentication toke
        auth_token = 'd22xxxxxx'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body='Danger!. Wild animal is detected, stay alert',
                from_=' +12293515154',  # the free number of twilio
                to='+919149492527')
        print(message.sid)
        print('Danger!!')
        print('Animal Detected')
        print('SMS sent!')
        # break
    else:
        print("No Danger")
       # break
    cv2.imshow("image", frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

video.release()
cv2.destroyAllWindows()
