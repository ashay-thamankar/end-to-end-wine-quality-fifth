import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
from mlProject.config.configuration import ModelTrainerConfig
import os
from mlProject import *
from mlProject.utils.common import evaluate_models
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config  = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]
        models = self.config.model_to_loop
        model_p = self.config.model_params
        logger.info(f"Models parameters are ready to print")
        print(models)
        print(model_p)
        # print(model_p.keys())
        # # print((model_p.values()).keys())
        # print(model_p.values())

        model_report, temp_score, temp_model = evaluate_models(x_train=train_x, y_train=train_y, x_test=test_x, y_test=test_y, models=models, params=model_p)

        print(model_report)
        
        best_model_score = max(sorted(model_report.values()))

        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
            ]

        best_model = models[best_model_name]
        print(f"printing best model from model trainer {best_model} and its temp score {temp_score}")

        logging.info(f"Best model is {best_model_name} and its r2 score is {best_model_score}")
    

        # lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ration, random_state=42)

        # lr.fit(train_x, train_y)

        joblib.dump(temp_model, os.path.join(self.config.root_dir, self.config.model_name))