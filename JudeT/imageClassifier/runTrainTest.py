'''
functions used to train and test a model
'''
import torch
from tqdm.auto import tqdm
from typing import Dict, List, Tuple

'''
This function first sets a PyTorch model to training mode and then performs all the necessary 
training steps, including forward pass, loss calculation, and optimizer step.

Here are the arguments for the function:

- model: The PyTorch model that needs to be trained.
- dataloader: The DataLoader instance that contains the data the model will be trained on.
- loss_fn: The PyTorch loss function that the training process will minimize.
- optimizer: The PyTorch optimizer that helps minimize the loss function.
- device: The target device that the computation will be performed on.

The function returns a tuple containing two metrics for training performance. 
The metrics are the training loss and training accuracy, and are represented in
the form of a tuple.
'''

def training_model(model: torch.nn.Module,
					dataloader: torch.utils.data.DataLoader,
					loss_fn: torch.nn.Module,
					optimizer: torch.optim.Optimizer,
					device: torch.device) -> Tuple[float, float]:
	#turn model on to train
	model.train()

	#we'll need to track loss and accuracy
	training_loss, training_accuracy = 0, 0

	#comb through data in batches
	for batch, (X, y) in enumerate(dataloader):
		
		X, y = X.to(device), y.to(device)

		#forward pass
		y_prediction = model(X)

		#calculate loss
		loss = loss_fn(y_prediction, y)
		training_loss += loss.item()

		#optimizer step
		optimizer.zero_grad()

		loss.backward()

		optimizer.step()

		#calculate accuracy throughout all batches
		y_prediction_class = torch.argmax(torch.softmax(y_prediction, dim=1), dim=1)
		training_accuracy += (y_prediction_class == y).sum().item()/len(y_prediction)

	#retrieve average loss and accuracy for each batch
	training_loss = training_loss / len(dataloader)
	training_accuracy = training_accuracy / len(dataloader)
	return training_loss, training_accuracy

def testing_model(model: torch.nn.Module,
					dataloader: torch.utils.data.DataLoader,
					loss_fn: torch.nn.Module,
					device: torch.device) -> Tuple[float, float]:
	#model in evaluation 
	model.eval()

	#we'll need to track testing loss and tesing accuracy
	testing_loss, testing_accuracy = 0,0

	#inference mode on
	with torch.inference_mode():
		#go though data laoder batches
		for batch, (X, y) in enumerate(dataloader):
			X, y = X.to(device), y.to(device)

			#forward pass
			test_prediction = model(X)

			#calculate loss
			loss = loss_fn(test_prediction, y)
			testing_loss += loss.item()

			#calculate accuracy
			testing_prediction_labels = test_prediction.argmax(dim=1)
			testing_accuracy += ((testing_prediction_labels == y).sum().item()/len(testing_prediction_labels))

	testing_loss = testing_loss / len(dataloader)
	testing_accuracy = testing_accuracy / len(dataloader)
	return testing_loss, testing_accuracy


'''
This process involves passing a PyTorch model through both 
the training and testing functions for a certain number of 
epochs, training and testing the model in the same epoch loop.

This function requires the following arguments:

- model: A PyTorch model that will undergo training and testing.
- training_dataloader: contains the training data for the model.
- testing_dataloader: contains the testing data for the model.
- optimizer: A PyTorch optimizer that will minimize the loss function during training.
- loss_fn: A PyTorch loss function that will calculate the loss on both the training and testing datasets.
- epochs: An integer value indicating the number of epochs for which the model should be trained.
- device: The device where the computation will take place, either "cuda" or "cpu".

returns a dictionary:

For each epoch, this dictionary contains a list of values for training and testing loss, 
as well as training and testing accuracy metrics. The dictionary has the following structure: 

- Training loss: a list of values for training loss across epochs.
- Testing loss: a list of values for testing loss across epochs.
- Training accuracy: a list of values for training accuracy across epochs.
- Testing accuracy: a list of values for testing accuracy across epochs.

'''
def train (model: torch.nn.Module,
			training_dataloader: torch.utils.data.DataLoader,
			testing_dataloader: torch.utils.data.DataLoader,
			optimizer: torch.optim.Optimizer,
			loss_fn: torch.nn.Module,
			epochs: int,
			device: torch.device) -> Dict[str, List]:
	#creat a dict for results
	results = {'training_loss': [],
		'training_accuracy': [],
		'testing_loss': [],
		'testing_accuracy': []
	}

	#go through training and testing for number of epochs
	for epoch in tqdm(range(epochs)):
		training_loss, training_accuracy = training_model(model = model,
															dataloader = training_dataloader,
															loss_fn = loss_fn,
															optimizer = optimizer,
															device = device)
		testing_loss, testing_accuracy = testing_model(model = model,
														dataloader = testing_dataloader,
														loss_fn = loss_fn,
														device = device)
		print(
          f"Epoch: {epoch+1} | "
          f"training_loss: {training_loss:.4f} | "
          f"training_accuracy: {training_accuracy:.4f} | "
          f"testing_loss: {testing_loss:.4f} | "
          f"testing_accuracy: {testing_accuracy:.4f}"
      	)

	return results
