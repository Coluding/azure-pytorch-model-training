from azureml.core.model import Model
from azureml.core import Workspace, Environment
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice, LocalWebservice


ws = Workspace(subscription_id='41389919-46b1-46b4-819a-f1ccb00cc40c',
                        resource_group='gpu_training',
                        workspace_name='ImageClassification',
                        _location="westeu",
                        )

model = Model(ws, "CarCrashClassifier")

env = Environment.get(workspace=ws, name="image_classifier")
inference_config = InferenceConfig(entry_script="../../../insurance_image_recog/src/model_architecture/inference_run.py",
                                   environment=env)


aci_service_name = "test-deploy"

deployment_config = AciWebservice.deploy_configuration(cpu_cores=2, memory_gb=6)
#deployment_config = LocalWebservice.deploy_configuration(port=8890)

service = Model.deploy(ws, aci_service_name, [model], inference_config, deployment_config, overwrite=True)
service.wait_for_deployment(True)

print(service.state)