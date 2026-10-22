

from datasets import load_dataset
import pandas as pd


class HFDatasetLoader:
    """
    Carga un dataset de Hugging Face y lo devuelve
    como un DataFrame de pandas.
    """

    def __init__(self, dataset_id, split="train"):
        """
        Parámetros:
            dataset_id (str): identificador del dataset.
            split (str): partición de datos que se cargará.
        """
        self.dataset_id = dataset_id
        self.split = split

    def load(self):
        """
        Descarga o carga el dataset y devuelve
        sus datos como un DataFrame de pandas.
        """
        dataset = load_dataset(
            self.dataset_id,
            split=self.split
        )

        dataframe = dataset.to_pandas()

        return dataframe
