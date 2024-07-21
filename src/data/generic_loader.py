import os

import pandas as pd


def load_data_paths() -> dict:
    # Extract list of data folders
    data_path = os.path.join("data")
    data_path_content = os.listdir(data_path)
    folders = [element for element in data_path_content if "." not in element]

    # Extract datetime to find the most current folder and create path
    folder_datetimes = [
        pd.to_datetime(folder_name[-14:], format="%Y%m%d%H%M%S")
        for folder_name in folders
    ]
    newest_folder_idx = folder_datetimes.index(max(folder_datetimes))
    newest_folder_name = folders[newest_folder_idx]
    newest_folder_path = os.path.join(data_path, newest_folder_name)

    # List all available .csv files in the highest file layer
    newest_folder_content = os.listdir(newest_folder_path)
    curr_files = [
        element for element in newest_folder_content if element[-4:] == ".csv"
    ]

    data_dict = {}

    # Loop through the files,
    for i, file in enumerate(curr_files):
        components = file.split(".")
        components = components[2:-2]

        desc = "_".join(components)

        filename = curr_files[i]
        path = os.path.join(newest_folder_path, filename)

        data_dict[desc] = path

    return data_dict
