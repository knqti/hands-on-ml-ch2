from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tarfile
import urllib.request


def load_housing_data() -> pd.DataFrame:
    tarball_dir = Path('datasets')
    tarball_path = tarball_dir / 'housing.tgz'
    if not tarball_dir.is_dir():
        tarball_dir.mkdir(parents=True, exist_ok=True)

    if not tarball_path:
        url = 'https://github.com/ageron/data/raw/main/housing.tgz'
        urllib.request.urlretrieve(url, tarball_path)

        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path='datasets')

    return pd.read_csv('datasets/housing/housing.csv')

def explore_data(dataframe):
    print(dataframe.head())
    print(dataframe.info())
    print(dataframe['ocean_proximity'].value_counts())
    print(dataframe.describe())

    dataframe.hist(bins=50, figsize=(12, 8))
    plt.show()

def shuffle_and_split_data(dataframe, test_ratio) -> tuple[list, list]:
    shuffled_indices = np.random.permutation(len(dataframe))
    test_set_size = int(len(dataframe) * test_ratio)

    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]

    return dataframe.iloc[test_indices], dataframe.iloc[train_indices]

if __name__ == '__main__':
    housing_df = load_housing_data()

    # explore_data(housing_df)

    test_set, train_set = shuffle_and_split_data(housing_df, test_ratio=0.2)
