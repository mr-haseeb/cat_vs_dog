import os
import pandas as pd

csv_path = 'data.csv'
images_dir = 'PetImages/'


labeled_images = []
for subdir, dirs, files in os.walk(images_dir):
    for img in files:
        image_path = os.path.join(subdir, img)
        label = subdir.split('/')[-1]
        print(label)
        labeled_images.append([image_path, label])
df = pd.DataFrame(labeled_images, columns=['images', 'labels'])
df.to_csv(csv_path, encoding='utf-8', index=False)

def
