import os
import torch
import multiprocessing
import setup_data, runTrainTest, build_model, utils

from torchvision import transforms

def main ():
	#parameters needed
	NUM_EPOCHS = 15
	BATCH_SIZE = 32
	HIDDEN_UNITS = 10
	LEARNING_RATE = 0.001

	#directories
	training_directory = "data/shelled_nuts_data/train"
	testing_directory = "data/shelled_nuts_data/test"

	#set up a device
	device = 'cuda' if torch.cuda.is_available() else 'cpu'

	#transform data
	data_transform = transforms.Compose([
	  transforms.Resize((120, 120)),
	  transforms.ToTensor()
	])

	#create dataloaders with setup_data
	training_dataloader, testing_dataloader, class_names = setup_data.create_dataloaders(
		training_directory = training_directory,
		testing_directory = testing_directory,
		transform = data_transform,
		batchProcess_size = BATCH_SIZE
	)

	#create model
	model = build_model.ImageClassifier(input_shape = 3,
										hidden_units = HIDDEN_UNITS,
										output_shape = len(class_names) 
	).to(device)

	loss_fn = torch.nn.CrossEntropyLoss()
	#optimizer = torch.optim.Adam(model.parameters(), lr = LEARNING_RATE)
	optimizer = torch.optim.RMSprop(model.parameters(), lr = LEARNING_RATE, alpha=0.99, eps=1e-08)


	# begin training
	runTrainTest.train(model = model,
						training_dataloader = training_dataloader,
						testing_dataloader = testing_dataloader,
						loss_fn = loss_fn,
						optimizer = optimizer,
						epochs = NUM_EPOCHS,
						device = device)
	utils.save_model(model=model,
                 save_directory="models",
                 model_name="ImageClassifier_entopyloss_RMSpropOptimizer.pth")

if __name__ == '__main__':
	main()