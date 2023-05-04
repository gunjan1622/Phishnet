import torch

import torch.nn as nn
import torch.nn.functional as F

def load_model(model, model_path):
    model.load_state_dict(torch.load(model_path))
    return model