from mlProject import *
from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transformation Stage"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_splitting()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        raise e