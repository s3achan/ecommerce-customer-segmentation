import kagglehub
import os
import shutil
# Download latest version
path = kagglehub.dataset_download("carrie1/ecommerce-data")

for file in os.listdir(path):
    shutil.copy(os.path.join(path, file), os.getcwd())