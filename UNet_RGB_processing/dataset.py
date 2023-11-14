import os
import torch
from PIL import Image
from torch.utils.data import Dataset


class CustomSegmentationDataset(Dataset):
    """
    A custom PyTorch Dataset for loading and transforming images for a machine learning model.

    The dataset loads images and their corresponding target data from specified directories,
    applying transformations to the images and converting the target data into tensor format.

    Args:
    - root_dir (str): Path to the directory containing the images and the mask files.
    - image_folder (str): Name of the file containing the images.
    - mask_folder (str): Name of the file containing mask.
    - new_size (tuple[int, int]): The new size (height, width) to which the images are resized.

    Attributes:
    - root_dir (str): Path to the directory containing the images and the mask files.
    - image_folder(str): Directory containing image files.
    - mask_folder (str): Directory containing mask data files.
    - new_size (tuple[int, int]): The target size for image resizing.

    Methods:
    - __len__(): Returns the number of items in the dataset.
    - __getitem__(idx): Retrieves the image and its target at the specified index, applies the necessary transformations to the image,
      and returns both the image and target as tensors.
    """
    classes = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500]
    # classes = torch.tensor(classes)

    def __init__(self, root_dir, image_folder, mask_folder, transform):
        self.root_dir = root_dir
        self.image_folder = image_folder
        self.mask_folder = mask_folder

        self.image_files = [f for f in os.listdir(os.path.join(root_dir, image_folder)) if f.endswith(".png")]
        self.mask_files = [f for f in os.listdir(os.path.join(root_dir, mask_folder)) if f.endswith(".png")]

        self.transform = transform

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        image_path = os.path.join(self.root_dir, self.image_folder, self.image_files[idx])
        mask_path = os.path.join(self.root_dir, self.mask_folder, self.mask_files[idx])

        image = Image.open(image_path)
        mask = Image.open(mask_path)

        if self.transform is not None:
            image = self.transform(image)
            mask = self.transform(mask)

        return image, mask
