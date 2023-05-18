
'''
To create data loaders that can fetch data and transform them into datasets, use the following `create_dataloader` function parameters:

- training_directory: This parameter specifies the path to the data that the model will use for training.
- testing_directory: This parameter specifies the path to the data that the model will use for testing.
- transform: This parameter uses the torchvision library to transform the data.
- batchProcess_size: This parameter sets the number of samples in each batch for the data loaders.
- num_workers: This parameter determines the number of workers for the data loader.
'''

import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

##get the number of proccessors available 
number_of_processors= os.cpu_count()

def create_dataloaders (
	training_directory: str,
	testing_directory: str,
	transform: transforms.Compose,
	batchProcess_size: int,
	number_of_workers: int=number_of_processors
):
	#utilize ImageFolder to create our dataset
	training_data = datasets.ImageFolder(training_directory, transform=transform)
	testing_data = datasets.ImageFolder(testing_directory, transform=transform)


	'''
	 training_data.classes => returns a list of names of the subfolders in directory.
	 This is used to label our images. All images of peanuts are in the peanut
	 folder and images of walnuts are in the walnut folder...etc
	'''
	class_names = training_data.classes

	training_dataloader = DataLoader (
		training_data,
		batch_size = batchProcess_size,
		shuffle = True,#determines if data should be shuffeled at every epoch. 
		num_workers = number_of_workers,
		pin_memory = True, #specifies whether to use pinned memory for faster data transfer between the CPU and GPU.
	)

	testing_dataloader = DataLoader (
		testing_data,
		batch_size = batchProcess_size,
		shuffle = True,
		num_workers = number_of_workers,
		pin_memory = True,
	)

	return training_dataloader, testing_dataloader, class_names