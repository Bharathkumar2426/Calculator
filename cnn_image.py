
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
from tkinter import Tk, filedialog
from tensorflow.keras import layers, models

# Step 1: Select an image from your computer
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an Image",
    initialdir="C:/Users",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp"),
        ("All files", "*.*")
    ]
)

root.destroy()

if not file_path:
    print("No image selected.")
    raise SystemExit

# Step 2: Load and preprocess image
img = Image.open(file_path).convert("RGB")
img = img.resize((64, 64))

gray = np.array(img.convert("L"), dtype=np.float32) / 255.0

# Step 3: Create an approximate mask using thresholding
mask = (gray > gray.mean()).astype(np.float32)

X = gray.reshape(1, 64, 64, 1)
Y = mask.reshape(1, 64, 64, 1)

# Step 4: Build CNN model
model = models.Sequential([
    layers.Input(shape=(64, 64, 1)),
    layers.Conv2D(16, 3, activation="relu", padding="same"),
    layers.MaxPooling2D(2),
    layers.Conv2D(32, 3, activation="relu", padding="same"),
    layers.UpSampling2D(2),
    layers.Conv2D(16, 3, activation="relu", padding="same"),
    layers.Conv2D(1, 1, activation="sigmoid", padding="same")
])

# Step 5: Compile and train CNN
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(X, Y, epochs=5, verbose=1)

# Step 6: Predict segmentation
prediction = model.predict(X, verbose=0)
segmented = (prediction[0, :, :, 0] > 0.5).astype(np.uint8)

# Step 7: Display output
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap="gray")
plt.title("Approximate Mask")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(segmented, cmap="gray")
plt.title("CNN Segmentation")
plt.axis("off")

plt.tight_layout()
plt.show()

print("CNN Image Segmentation Completed Successfully")
