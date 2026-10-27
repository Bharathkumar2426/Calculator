
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
from PIL import Image, ImageDraw

# Step 1: Create a sample image and its ground-truth mask
img = Image.new("RGB", (64, 64), "black")
draw = ImageDraw.Draw(img)
draw.ellipse((16, 16, 48, 48), fill="white")

mask_img = Image.new("L", (64, 64), 0)
mask_draw = ImageDraw.Draw(mask_img)
mask_draw.ellipse((16, 16, 48, 48), fill=255)

# Step 2: Convert images into arrays
X = np.array(img.convert("L"), dtype="float32") / 255.0
Y = np.array(mask_img, dtype="float32") / 255.0

X = X.reshape(1, 64, 64, 1)
Y = (Y > 0.5).astype("float32").reshape(1, 64, 64, 1)

# Step 3: Build CNN model
model = models.Sequential([
    layers.Input(shape=(64, 64, 1)),
    layers.Conv2D(16, 3, activation="relu", padding="same"),
    layers.MaxPooling2D(2),
    layers.Conv2D(32, 3, activation="relu", padding="same"),
    layers.UpSampling2D(2),
    layers.Conv2D(16, 3, activation="relu", padding="same"),
    layers.Conv2D(1, 1, activation="sigmoid", padding="same")
])

# Step 4: Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Step 5: Train the CNN
model.fit(X, Y, epochs=10, verbose=1)

# Step 6: Predict segmentation mask
prediction = model.predict(X)
segmented = (prediction[0, :, :, 0] > 0.5).astype("uint8")

# Step 7: Display results
plt.figure(figsize=(9, 3))

plt.subplot(1, 3, 1)
plt.imshow(X[0, :, :, 0], cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(Y[0, :, :, 0], cmap="gray")
plt.title("Actual Mask")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(segmented, cmap="gray")
plt.title("Predicted Segmentation")
plt.axis("off")

plt.tight_layout()
plt.show()

print("CNN Image Segmentation Completed Successfully")
