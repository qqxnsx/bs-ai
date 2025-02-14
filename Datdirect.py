##Define data directories
data_dir = "Training"
test_data_dir = "Testing"

##Define class names
class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']
n_classes = len(class_names)

##Define class names
class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']
n_classes = len(class_names)


##Verify paths exist
print(f"Training data path exists: {os.path.exists(data_dir)}")
print(f"Testing data path exists: {os.path.exists(test_data_dir)}")