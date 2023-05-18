import torch
from pathlib import Path

def save_model (model: torch.nn.Module,
				save_directory: str,
				model_name: str):

	save_directory_path = Path(save_directory)
	save_directory_path.mkdir (parents = True, exist_ok = True)

	assert model_name.endswith('.pth') or model_name.endswith('.pt')
	model_saved_path = save_directory_path / model_name

	torch.save(obj=model.state_dict(),
	             f=model_saved_path)