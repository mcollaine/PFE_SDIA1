import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
from dataset import *
from unet import *
from tqdm import tqdm

# Settings
num_classes = 121  # Number of classes for the 10K classification
in_channels = 3  # Number of channels dans les images d'entrée (3 pour RGB, 1 pour niveau de gris)
out_channels = 1  # Nombre de classes dans la segmentation
batch_size = 16  # Batch size for the training and validation dataset
learning_rate = 0.001
num_epochs = 9
training_root_dir = r"C:\Users\marie\PycharmProjects\Unet3\Dataset_multi\Training"
validation_root_dir = r"C:\Users\marie\PycharmProjects\Unet3\Dataset_multi\Validation"
image_folder = "Frame"
mask_folder = "Masks"
transform = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])


# Creating of the Unet model
model = UNet(in_channels, out_channels)

# Defining of the loss function
criterion = nn.CrossEntropyLoss()

# Choosing of the optimizer
optimizer = optim.Adam(model.parameters(), lr=learning_rate)


# Creating of the training and the validation datasets with DataLoader
train_dataset = CustomSegmentationDataset(training_root_dir, image_folder, mask_folder, transform)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_dataset = CustomSegmentationDataset(validation_root_dir, image_folder, mask_folder, transform)
val_loader = DataLoader(val_dataset, batch_size=batch_size)

# Training
for epoch in tqdm(range(num_epochs)):
    model.train()
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        print(outputs.shape, labels.shape)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    # Validation and calculating of the loss function for the validation
    model.eval()
    with torch.no_grad():
        for inputs, labels in val_loader:
            outputs = model(inputs)
            val_loss = criterion(outputs, labels)

    print(f'Epoch [{epoch + 1}/{num_epochs}] - Training Loss: {loss.item():.4f}, Validation Loss: {val_loss.item():.4f}')

# Saving the trained model
torch.save(model.state_dict(), 'unet_segmentation_model.pth')
