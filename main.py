from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        raise e
    
STAGE_NAME = "Data Validation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed")
    except Exception as e:
        raise e
    
STAGE_NAME = "Data Transformation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed")
    except Exception as e:
        raise e
    

STAGE_NAME = "Model Trainer Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed")
    except Exception as e:
        raise e

STAGE_NAME = "Model Evaluation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed")
    except Exception as e:
        raise e
    

