import cv2
import numpy as np
import time
import os

IMAGEM_PATH = 'images/zuky.jpeg' 
IMAGE_BLUE_OUTPUT = 'resultImages/result_blue.jpg'
IMAGE_GRADIENT_OUTPUT = 'resultImages/result_gradient.jpg'
IMAGE_GREEN_DIAGONAL_OUTPUT = 'resultImages/result_green_diagonal.jpg'
IMAGE_OPTIMIZED_GRADIENT_OUTPUT = 'resultImages/result_optimized_gradient.jpg'

def load_image(path):
    if not os.path.exists(path):
        print(f"ERROR: File not found at path: {path}")
        return None

    image = cv2.imread(path, cv2.IMREAD_COLOR)

    if image is None:
        print(f"ERROR: Could not load the image from {path}.")
        return None
    
    print(f"Image loaded successfully. Dimensions: {image.shape} (Height, Width, Channels)")
    return image

def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0) 

def save_image(name, image):
    cv2.imwrite(name, image)
    print(f"Result saved as '{name}'.")

# -----------------------------------------------------

original_image = load_image(IMAGEM_PATH)
if original_image is None:
    exit()

height, width, channels = original_image.shape

# -----------------------------------------------------

print("\n--- Question 1: Pure Blue Image (SLOW Loops) ---")
blue_image_slow = original_image.copy() 

start_time = time.time()

for y in range(height):
    for x in range(width):
        blue_image_slow[y, x] = (255, 0, 0)

end_time = time.time()
time_q1 = end_time - start_time
print(f"Execution time (Loops): {time_q1:.6f} seconds")

save_image(IMAGE_BLUE_OUTPUT, blue_image_slow)


# -----------------------------------------------------

print("\n--- Question 2: Optimized Solution (FAST NumPy) ---")
blue_image_fast = original_image.copy()

start_time = time.time()

blue_image_fast[:] = (255, 0, 0)

end_time = time.time()
time_q2 = end_time - start_time
print(f"Execution time (NumPy): {time_q2:.6f} seconds")
print(f"Speedup (Q1/Q2): {time_q1/time_q2:.1f}x")


# -----------------------------------------------------

print("\n--- Question 3: Color Gradient (SLOW Loops) ---")
gradient_image_slow = original_image.copy()

start_time = time.time()

for y in range(height):
    for x in range(width):
        blue = x % 256
        green = y % 256
        red = x % 256
        
        gradient_image_slow[y, x] = (blue, green, red)

end_time = time.time()
time_q3 = end_time - start_time
print(f"Execution time (Loops): {time_q3:.6f} seconds")

save_image(IMAGE_GRADIENT_OUTPUT, gradient_image_slow)


# -----------------------------------------------------

print("\n--- Question 4: Modification (Diagonal Green) ---")
green_diagonal_image = np.zeros_like(original_image)

start_time = time.time()

for y in range(height):
    for x in range(width):
        green_value = (x + y) % 256
        green_diagonal_image[y, x, 1] = green_value 

end_time = time.time()
print(f"Execution time (Loops): {end_time - start_time:.6f} seconds")

save_image(IMAGE_GREEN_DIAGONAL_OUTPUT, green_diagonal_image)


# -----------------------------------------------------

print("\n--- Question 5: Optimized Gradient (NumPy) ---")
optimized_gradient_image = np.zeros_like(original_image, dtype=np.uint8)

start_time = time.time()

Y_coords, X_coords = np.mgrid[0:height, 0:width]

B_channel = (X_coords % 256).astype(np.uint8)
G_channel = (Y_coords % 256).astype(np.uint8)
R_channel = (X_coords % 256).astype(np.uint8)

optimized_gradient_image = np.stack([B_channel, G_channel, R_channel], axis=2)

end_time = time.time()
time_q5 = end_time - start_time
print(f"Execution time (Optimized NumPy): {time_q5:.6f} seconds")
print(f"Speedup (Q3/Q5): {time_q3/time_q5:.1f}x")

save_image(IMAGE_OPTIMIZED_GRADIENT_OUTPUT, optimized_gradient_image)


# -----------------------------------------------------

cv2.destroyAllWindows()

print("\n--- EXERCISES COMPLETE ---")
print(f"Check the output files: {IMAGE_BLUE_OUTPUT}, {IMAGE_GRADIENT_OUTPUT}, {IMAGE_GREEN_DIAGONAL_OUTPUT}, {IMAGE_OPTIMIZED_GRADIENT_OUTPUT}")