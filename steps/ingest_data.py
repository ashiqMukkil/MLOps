import logging

import pandas as pd
from zenml import step

class IngestData:
    def __init__(self,data_path: str) -> None:
        self.data_path = data_path

    def get_data(self):
        logging.info(f"Ingesting data from path {self.data_path}")
        return pd.read_csv(self.data_path)

@step
def ingest_data(data_path: str) -> pd.DataFrame:
    """
    Ingesting data from path
    """
    try:
        return IngestData(data_path=data_path).get_data()
    except Exception as exp:
        logging.error(f"Ingesting data failed with error {exp}")

##1,16