#build a function that recieves a img path and predicts on that img
import os
import torchvision
from torchvision import datasets, transforms
import torch
from torch import nn
import setup_data, runTrainTest, build_model, utils

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def predict_image(model: torch.nn.Module,
					img_path: str,
					class_names: list[str] = None,
					transform = None,
					device = 'cuda' if torch.cuda.is_available() else 'cpu'):
	image_to_predict = torchvision.io.read_image(str(img_path)).type(torch.float32)
	# divide custom image pixel values by 255 to get them btwn 0,1
	image_to_predict = image_to_predict/255

	if transform:
		image_to_predict = transform(image_to_predict)

	model.to(device)

	#start evaluation
	model.eval()
	with torch.inference_mode():
		#add dimension for batch_szie
		image_to_predict = image_to_predict.unsqueeze(0)

		#make prediction
		image_prediction = model(image_to_predict.to(device))

	#torch.nn.Module returns logits, lets convert it to be readable
	image_prediction_possibilities = torch.softmax(image_prediction, dim = 1)
	#convert to label. (either peanuts, pistachio or walnut)
	image_prediction_label = torch.argmax(image_prediction_possibilities, dim = 1)

	if class_names:
		return (class_names[image_prediction_label.cpu()], (image_prediction_possibilities.max().cpu()) )
	else:
		return (image_prediction_label, (image_prediction_possibilities.max().cpu()) )

'''
data_transform = transforms.Compose([
	  transforms.Resize((120, 120)),
	  
	])
class_names = ["peanuts", "pistachio", "walnuts"]

checkpoint = 'models/model_0.pth'

model = build_model.ImageClassifier(input_shape = 3,
										hidden_units = 10,
										output_shape = len(class_names) 
	).to(device)

model.load_state_dict(torch.load(checkpoint))



predict_image(model = model,
				img_path = 'newData/walnut.jpg',
				class_names = ["peanuts", "pistachio", "walnuts"],
				transform = data_transform,
				device = 'cuda' if torch.cuda.is_available() else 'cpu')

'''