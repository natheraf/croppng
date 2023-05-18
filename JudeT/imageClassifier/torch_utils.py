import os
import torchvision
from torchvision import datasets, transforms
import torch
from torch import nn
import build_model, classify_image
from PIL import Image

def get_prediction():
	device = 'cuda' if torch.cuda.is_available() else 'cpu'

	class_names = ["peanuts", "pistachio", "walnuts"]

	#let's get the path that contains the image we want to predict on
	folder_path = 'newData/'  # Specify the folder path here
	file_name = ''
	# List all files in the folder
	files = os.listdir(folder_path)

	for file in files:
		if os.path.isfile(os.path.join(folder_path, file)):
			file_name = file
			break #we break because we only want the first file
	folder_path+=file_name
	img_path = folder_path
	#############################################################
	checkpoint = 'models/model_0.pth' #locate our saved pre-trained model

	data_transform = transforms.Compose([
		  transforms.Resize((120, 120)),
		  
		])

	#define our model
	model = build_model.ImageClassifier(input_shape = 3,
											hidden_units = 10,
											output_shape = len(class_names) 
		).to(device)

	#load up the pre-trained model
	model.load_state_dict(torch.load(checkpoint))

	#run model to recieve prediction
	prediction = classify_image.predict_image(model = model,
					img_path = img_path,
					class_names = ["peanuts", "pistachio", "walnuts"],
					transform = data_transform,
					device = device)
	return prediction