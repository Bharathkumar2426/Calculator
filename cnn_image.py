
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
from tkinter import Tk, filedialog
from tensorflow.keras import layers, models

# Step 1: Select an image from your computer
root = Tk()
root.withdraw()
root.attributes("-topmost", True)
root.update()

file_path = filedialog.askopenfilename(
    parent=root,
    title="Select an Image for CNN Segmentation",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp"),
        ("All files", "*.*")
    ]
)

root.destroy()

if not file_path:
    print("No image selected. Please run the program again.")
    raise SystemExit

print("Selected image:", file_path)

# Step 2: Load and preprocess the image
img = Image.open(file_path).convert("RGB")
original_img = img.copy()
img = img.resize((64, 64))

gray = np.array(
    img.convert("L"), dtype=np.float32
) / 255.0

# Step 3: Create an approximate binary segmentation mask
mask = (gray > gray.mean()).astype(np.float32)

# Prepare input and target arrays
X = gray.reshape(1, 64, 64, 1)
Y = mask.reshape(1, 64, 64, 1)

# Step 4: Build the CNN model
model = models.Sequential([
    layers.Input(shape=(64, 64, 1)),

    layers.Conv2D(
        16, (3, 3), activation="relu", padding="same"
    ),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(
        32, (3, 3), activation="relu", padding="same"
    ),
    layers.UpSampling2D((2, 2)),

    layers.Conv2D(
        16, (3, 3), activation="relu", padding="same"
    ),
    layers.Conv2D(
        1, (1, 1), activation="sigmoid", padding="same"
    )
])

# Step 5: Compile the model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Step 6: Train the CNN
print("\nTraining CNN model...")
model.fit(X, Y, epochs=5, verbose=1)

# Step 7: Predict the segmentation mask
prediction = model.predict(X, verbose=0)
segmented = (
    prediction[0, :, :, 0] > 0.5
).astype(np.uint8)

# Step 8: Display results
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(original_img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap="gray", vmin=0, vmax=1)
plt.title("Approximate Mask")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(segmented, cmap="gray", vmin=0, vmax=1)
plt.title("CNN Predicted Mask")
plt.axis("off")

plt.tight_layout()
plt.show()

print("\nCNN Image Segmentation Completed Successfully!")
