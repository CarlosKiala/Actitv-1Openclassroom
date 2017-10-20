from clarifai.rest import Image as ClImage

from clarifai import rest 

from clarifai.rest import ClarifaiApp

import base64

app = ClarifaiApp(api_key  = 'f0c23ca2bb4749918696a845c7b2fb0d')


model = app.models.get('Sorting')

with open("plastic44.jpg","rb") as image_file:
	encoded_string  = base64.b64encode(image_file.read())

image  = app.inputs.create_image_from_base64(encoded_string)

dictionnaire = model.predict([image])

liste = dictionnaire['outputs']

dico  = liste.pop()

dico1 = dico['data']


liste1 = dico1['concepts']

for i in liste1:
	print(i)






