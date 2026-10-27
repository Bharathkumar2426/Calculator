
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Generate sample images and segmentation masks
X = np.random.rand(100, 64, 64, 1).astype("float32")
Y = (X > 0.5).astype("float32")

# Build CNN model
model = models.Sequential([
    layers.Input(shape=(64, 64, 1)),

    # Encoder
    layers.Conv2D(16, 3, activation='relu', padding='same'),
    layers.MaxPooling2D(2),

    layers.Conv2D(32, 3, activation='relu', padding='same'),
    layers.MaxPooling2D(2),

    # Decoder
    layers.Conv2D(32, 3, activation='relu', padding='same'),
    layers.UpSampling2D(2),

    layers.Conv2D(16, 3, activation='relu', padding='same'),
    layers.UpSampling2D(2),

    # Pixel-wise segmentation output
    layers.Conv2D(1, 1, activation='sigmoid', padding='same')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(X, Y, epochs=3, batch_size=8)

# Predict segmentation mask
prediction = model.predict(X[:1])
mask = (prediction > 0.5).astype("uint8")

print("Input image shape:", X[:1].shape)
print("Segmentation mask shape:", mask.shape)
print("CNN image segmentation completed successfully.")
