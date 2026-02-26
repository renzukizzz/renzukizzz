# This script creates empty dataset folders

import os

# Specify the folders to create
folders = ['dataset1', 'dataset2', 'dataset3']

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f'Created folder: {folder}')