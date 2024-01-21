from mlProject.config.configuration import ConfigurationManager
from mlProject import *
from mlProject.components.data_validation import DataValidation

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        raise e
