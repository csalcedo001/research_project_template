import os
import torchvision.datasets
import torchvision.transforms as transforms

available_datasets = ["mnist", "celeba", "cifar10", "svhn"]

def load_dataset(dataroot, dataset_name, image_size, num_channels, **kwargs):
    if dataset_name not in available_datasets:
        raise Exception("Unsupported dataset '{}'. Available datasets: '{}''.".format(
            dataset_name, "', '".join(available_datasets)
        ))


    if dataset_name == 'mnist':
        dataset_function = torchvision.datasets.MNIST
    elif dataset_name == 'celeba':
        dataset_function = torchvision.datasets.CelebA
    elif dataset_name == 'cifar10':
        dataset_function = torchvision.datasets.CIFAR10
    elif dataset_name == 'svhn':
        dataset_function = torchvision.datasets.SVHN



    if num_channels not in [1, 3]:
        raise Exception("Given number of channels ({}) is unsupported. Only 1 or 3 channels can be used.".format(
            num_channels
        ))

    channel_transform = transforms.Lambda(lambda x: x)

    if num_channels == 1 and dataset_name != 'mnist':
        channel_transform = transforms.Grayscale()
    elif num_channels == 3 and dataset_name == 'mnist':
        channel_transform = transforms.Lambda(lambda x: x.repeat(3, 1, 1))



    transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.CenterCrop(image_size),
        transforms.ToTensor(),
        channel_transform,
        transforms.Normalize((0.5,), (0.5,)),
    ])

    dataset = dataset_function(root=os.path.join(dataroot, dataset_name), transform=transform, **kwargs)

    return dataset
