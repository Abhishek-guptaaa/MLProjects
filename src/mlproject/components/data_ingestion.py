# import os
# import sys
# from mlproject.logger import logging
# from mlproject.exception import CustomException
# import pandas as pd
# from dataclasses import dataclass
# from src.mlproject.utils import read_sql_data
# from sklearn.model_selection import train_test_split
# from src.mlproject.components.model_trainer import ModelTrainer
# from src.mlproject.components.data_transformation import DataTransformation

# @dataclass
# class DataIngestionConfig:
#     train_data_path: str=os.path.join('artifacts',"train.csv")
#     test_data_path: str=os.path.join('artifacts',"test.csv")
#     raw_data_path: str=os.path.join('artifacts',"data.csv")

# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config = DataIngestionConfig()

#     def initiate_data_ingestion(self):
#         try:
#             # Use raw string or replace backslashes with forward slashes
#             data_path = r'D:\MLPROJECTS\notebook\data\data.csv'
        
            
#             df = pd.read_csv(data_path)
#             logging.info("Reading completed from the data file")

#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

#             df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
#             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
#             train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
#             test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

#             # Return the paths to be unpacked in the main script
#             return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

#         except Exception as e:
#             logging.info("Data initialization has failed")
#             raise CustomException(e, sys)



import os
import sys
from ..logger import logging
from ..exception import CustomException
import pandas as pd
from dataclasses import dataclass
from ..utils import read_sql_data
from sklearn.model_selection import train_test_split
from .model_trainer import ModelTrainer
from .data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # Use raw string or replace backslashes with forward slashes
            data_path = r'D:\MLPROJECTS\notebook\data\data.csv'
            
            df = pd.read_csv(data_path)
            logging.info("Reading completed from the data file")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            # Return the paths to be unpacked in the main script
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.info("Data initialization has failed")
            raise CustomException(e, sys)

