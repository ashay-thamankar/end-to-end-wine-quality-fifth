import os
import yaml
from box.exceptions import BoxValueError
import json
from mlProject import logger
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at {path}")

@ensure_annotations
def load_json(path: Path):
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file has been loaded successfully from {path}")
    return content

@ensure_annotations
def save_bin(path: Path, data:Any):
    joblib.dump(value=data, filename=path)
    logger.infok(f'filename has been saved at {path}')

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_KB = round(os.path.getsize(path))
    return f"~ {size_in_KB} KB"

@ensure_annotations
def evaluate_models(x_train, x_test, y_train, y_test, models: ConfigBox, params) -> tuple:
    try:
        report = {}
        logger.info(f"Entered to model evaluation list")

        temp_score = -100 # to store the r2 score
        temp_model = None

        for i in range(len(list(models))):
            model = eval(list(models.values())[i])
            
            param = params[list(models.keys())[i]]

            rs = RandomizedSearchCV(model, param)

            rs.fit(x_train, y_train)

            # model.fit(x_train, y_train)

            model.set_params(**rs.best_params_)
            model.fit(x_train, y_train)

            y_test_pred = model.predict(x_test)

            test_model_r2_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_r2_score
            # report["model_place"] = model 

            if test_model_r2_score > temp_score:
                temp_score = test_model_r2_score
                temp_model = model

        

        return report, temp_score, temp_model

    except Exception as e:
        raise e







