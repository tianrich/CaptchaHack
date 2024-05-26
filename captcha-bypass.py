import cv2
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the path for tesseract executable if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Update this path based on your Tesseract installation

# Load the image and convert it to grayscale
image_path = 'path/to/your/image.png'  # Update this path to your image file
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(gray)

# Check if the text contains the required class
if 'g-recaptcha' in text:
    print("g-recaptcha found in image text")

    # Set up Selenium WebDriver (Make sure to have the appropriate driver installed, e.g., chromedriver)
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update this path to your WebDriver
    driver.get('http://example.com')  # Update this URL to your target webpage

    try:
        # Wait until the recaptcha is loaded and interact with it if necessary
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'g-recaptcha'))
        )

        # Find and click the submit button
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[data-action='submit']")
        submit_button.click()

        print("Submit button clicked")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
else:
    print("g-recaptcha not found in image text")
