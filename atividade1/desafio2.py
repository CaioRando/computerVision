import cv2
import os

IMAGE_PATH = 'images/zuky.jpeg'
OUTPUT_PATH = 'resultImages/zuky_modified.jpeg'

Y_COORD = 150
X_COORD = 200
NOVA_COR_BGR = [255, 255, 0]

if __name__ == "__main__":
    
    print("=" * 70)
    print("CHALLENGE 2: IMAGE MODIFICATION AND VISUALIZATION")
    print("=" * 70)
    
    try:
        print(f"1. Reading original image: {IMAGE_PATH}")
        image_original = cv2.imread(IMAGE_PATH) 
        
        if image_original is None:
            raise FileNotFoundError(f"ERROR: Could not load image at {IMAGE_PATH}.")

        image_modified = image_original.copy()
        (height, width, _) = image_modified.shape
        
        print(f"2. Modifying pixel at coordinates (y, x) = ({Y_COORD}, {X_COORD}).")
        
        if 0 <= Y_COORD < height and 0 <= X_COORD < width:
            image_modified[Y_COORD, X_COORD] = NOVA_COR_BGR
            print(f"   Pixel successfully changed to BGR: {NOVA_COR_BGR}")
        else:
            print(f"   WARNING: Coordinates ({Y_COORD}, {X_COORD}) are out of image bounds.")

        print(f"3. Saving modified image to: {OUTPUT_PATH}")
        cv2.imwrite(OUTPUT_PATH, image_modified)
        print("   Modified image saved successfully.")

        print("\n4. Displaying images for comparison (Press any key to close):")
        
        cv2.imshow('1 - ORIGINAL IMAGE', image_original) 
        cv2.imshow('2 - MODIFIED IMAGE (Pixel Changed)', image_modified)

        cv2.waitKey(0) 

        cv2.destroyAllWindows() 
        print("Windows closed.")
        
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")