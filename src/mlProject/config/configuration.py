from mlProject.constants import *
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.utils.common import read_yaml, create_directories

class ConfigurationManager:
    def __init__(
            self,
            config_filename = CONFIG_FILE_PATH,
            params_filename = PARAMS_FILE_PATH,
            schema_filename = SCHEME_FILE_PATH
    ):
        self.config = read_yaml(config_filename)
        self.params = read_yaml(params_filename)
        self.schema = read_yaml(schema_filename)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config