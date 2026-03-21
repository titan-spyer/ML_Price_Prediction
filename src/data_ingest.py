import os
from abc import ABC, abstractmethod
import zipfile

import pandas as pd


# An abstract class for Data Ingestor.
class DataIngestor(ABC):
    @abstractmethod
    def ingest_data(self, file_path: str) -> pd.DataFrame:
        '''Abstract method to ingest data from a given file path.'''
        pass

# Implement a concern class for zip.
class ZipIngestor(DataIngestor):
    def ingest_data(self, file_path: str) -> pd.DataFrame:
        '''Ingest data from a zip file.'''
        '''Finding the file path'''
        if not os.path.exists(file_path):
            raise FileNotFoundError('File not found.')

        '''Checking if the file is a zip file'''
        if not file_path.endswith('.zip'):
            raise ValueError('File is not a zip file.')

        '''Extracting the zip file'''
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall('data')

        os_extracted = os.listdir('data')
        csv_file = [f for f in os_extracted if f.endswith('.csv')]

        if len(csv_file) == 0:
            raise ValueError('No CSV file found in the zip file.')
        if len(csv_file) > 1:
            raise ValueError('More than one CSV file found in the zip file.')

        csv_file = csv_file[0]
        csv_file_path = os.path.join('data', csv_file)

        '''Reading the CSV file'''
        df = pd.read_csv(csv_file_path)

        return df


# Implement the class for Data Ingest Factory.
class DataIngestFactory:
    @staticmethod
    def get_ingestor(file_type: str) -> DataIngestor:
        '''Return the appropriate DataIngestor based on the file type.'''
        if file_type == 'zip':
            return ZipIngestor()
        else:
            raise ValueError('Invalid file type.')


if __name__ == '__main__':
    # file_path = "Data.zip"

    # # Determine the extension
    # file_extension = os.path.splitext(file_path)[1]

    # # Appropiate Data ingestor.
    # data_ingestor = DataIngestFactory.get_ingestor(file_extension[1:])

    # # Ingest the data.
    # df = data_ingestor.ingest_data(file_path)

    # # The df contains the data extracted from csv
    # print(df)
    pass