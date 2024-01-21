from mlProject import *
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.evaluate_model()
        except Exception as e:
            raise e

if __name__ =="__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        raise e
        
