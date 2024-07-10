import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    ## all outputs will be saved in architect folder
    train_data_path : str=os.path.join('artifacts', "train.csv")
    test_data_path : str=os.path.join('artifacts', "test.csv")
    raw_data_path : str=os.path.join('artifacts', "raw.csv")

class Dataingestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method or component")
        try:
            df=pd.read_csv("notebook\Data\stud.csv")
            logging.info("read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            

        except:
            pass    