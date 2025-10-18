from Wine_Quality_Prediction.config.configuration import ConfigurationManager
from Wine_Quality_Prediction.components.model_trainer import ModelTrainer
from Wine_Quality_Prediction import logger




STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()