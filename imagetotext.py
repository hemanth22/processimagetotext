import sys
import warnings

# Suppress noisy PyTorch warnings (like the pin_memory warning) when running on CPU
warnings.filterwarnings("ignore", category=UserWarning)

try:
    import easyocr
except ImportError:
    print("Error: The 'easyocr' library is not found in your current Python environment.")
    print("Please install it by running: pip install easyocr torch torchvision")
    sys.exit(1)

def writetofile(results):
    with open("imagetotext.txt", "w") as f:
        for result in results:
            f.write(result + "\n")

def extract_text_from_image(image_path, language='en'):
    """
    Extracts text from an image using EasyOCR.
    This doesn't require any standalone OCR software like Tesseract to be installed
    on your OS, it just relies on the Python package and its downloaded models.
    """
    print("Initializing OCR (this may take a moment to download models on the first run)...")
    
    # Initialize the EasyOCR reader with the specified language
    reader = easyocr.Reader([language])
    
    print(f"Processing image: {image_path}")
    
    try:
        # Read text from the image
        # detail=0 returns only the text (not bounding boxes or confidence scores)
        results = reader.readtext(image_path, detail=0)
        
        print("\n--- Extracted Text ---\n")

        writetofile(results)
        
        if not results:
            print("No text found in the image.")
        else:
            # Join the list of text snippets into a single string
            text = '\n'.join(results)
            print(text)
            
        print("\n----------------------")
        
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python imagetotext.py <path_to_image_file>")
        print("Example: python imagetotext.py my_image.png")
    else:
        image_file = sys.argv[1]
        extract_text_from_image(image_file)
