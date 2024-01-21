import pandas as pd
from sklearn.model_selection import train_test_split
from mlProject.config.configuration import DataTransformationConfig
from mlProject import *

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info('Train test split started')
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)