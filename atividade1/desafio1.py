import cv2
import numpy as np

IMAGE_PATH = 'images/zuky.jpeg'

def calculate_average_color(image):
    (b_mean, g_mean, r_mean, a_mean) = cv2.mean(image)
    return (int(round(b_mean)), int(round(g_mean)), int(round(r_mean)))

def identify_color_dominance(b_avg, g_avg, r_avg):
    colors = {
        "Blue": b_avg,
        "Green": g_avg,
        "Red": r_avg
    }
    
    dominant_color = max(colors, key=colors.get)
    max_value = colors[dominant_color]
    
    dominant_colors = [color for color, value in colors.items() if value == max_value]
    
    if len(dominant_colors) > 1:
        return f"Tie: {', '.join(dominant_colors)} (Value: {max_value})"
    else:
        return f"Dominant: {dominant_color} (Value: {max_value})"

def examine_corners(image):
    (height, width, _) = image.shape
    
    corners = {
        "Top Left": (0, 0),
        "Top Right": (0, width - 1),
        "Bottom Left": (height - 1, 0),
        "Bottom Right": (height - 1, width - 1)
    }

    print("\n" + "=" * 70)
    print("CHALLENGE 1 - Q3: EXAMINING 4 CORNER PIXELS (y, x)")
    print(f"Dimensions: Height={height}, Width={width}")
    print("=" * 70)
    
    for name, (y, x) in corners.items():
        (b, g, r) = image[y, x]
        print(f"[{name}] ({y}, {x}) -> Red (R): {r}, Green (G): {g}, Blue (B): {b}")

if __name__ == "__main__":
    try:
        image = cv2.imread(IMAGE_PATH)
        
        if image is None:
            raise FileNotFoundError(f"ERROR: Could not load image at {IMAGE_PATH}. Check path and filename.")

        examine_corners(image)

        (b_avg, g_avg, r_avg) = calculate_average_color(image)

        print("\n" + "=" * 70)
        print("CHALLENGE 1 - Q4 & Q5: AVERAGE COLOR AND DOMINANCE")
        print("=" * 70)
        
        print(f"Average Image Color (R, G, B): ({r_avg}, {g_avg}, {b_avg})")
        
        dominance_result = identify_color_dominance(b_avg, g_avg, r_avg)
        print(dominance_result)
        
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")