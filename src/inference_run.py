import sys
import os
import torch
from PIL import Image
import io
import yaml
import sys
from azureml.core import Workspace, Model

#try:
#    from .insurance_image_recog.src.model_architecture.training.transforms import ImageTransforms
#except ImportError:
#    from insurance_image_recog.src.model_architecture.training.transforms import ImageTransforms

def init():
    global model
    print("model yes---------------------------------------------------")
    ws = Workspace(subscription_id='41389919-46b1-46b4-819a-f1ccb00cc40c',
                   resource_group='gpu_training',
                   workspace_name='ImageClassification',
                   _location="westeu",
                   )
    model = Model(ws, name="CarCrashClassifier")
    print("got model---------------------------------")
    model_path = model.download(exist_ok=True)
    print("download ok")
    model = torch.load(os.path.join(model_path, "data", "model.pth"),
                       map_location=torch.device("cpu"))


def run(data):
    try:
        print("we-------------------------------------------made it ")
        return {"hello": "world"}
    except Exception as e:
        print("exceeeeeeeeeeeeeeeeeeeept")
        return {"exception": e}

