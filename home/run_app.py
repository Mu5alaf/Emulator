import os
import sys
import django
import time
import base64
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from django.core.files.base import ContentFile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from home.models import App

def run_app(apk_id):
    app = App.objects.get(id=apk_id)
    apk_path = app.apk_path.path 
    print(apk_path)
    
    # Set up desired capabilities using UiAutomator2Options
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'Pixel_4_API_3'  # Ensure this matches your AVD name
    options.app = apk_path  # Path to the APK you want to test
    options.automation_name = 'UiAutomator2'

    # Connect to the Appium server and start a session with the specified options
    driver = webdriver.Remote('http://172.18.112.1:4723', options=options)
    time.sleep(90)  # Wait for app to load
    app.ui_hierarchy = driver.page_source
    
    # Start video recording
    driver.start_recording_screen(video_frames=60)

    # Take the first screenshot
    screenshot_data = driver.get_screenshot_as_png()  # Get screenshot as binary data
    first_screen_filename = f'first_screen_{app.id}.png'
    app.first_screen_path.save(first_screen_filename, ContentFile(screenshot_data))
    
    # Try to find and interact with the button
    try:
        wait = WebDriverWait(driver, 30)
        first_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/digit_7")))
        first_button.click()
        second_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/op_add")))
        second_button.click()
        third_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/digit_8")))
        third_button.click()
        equal_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/eq")))
        equal_button.click()
    except Exception as e:
        print(f"Error finding or clicking the button: {e}")
    
    # Wait for screen change
    time.sleep(2)  
    
    # Take the second screenshot
    screenshot_data = driver.get_screenshot_as_png()  # Get screenshot as binary data
    second_screen_filename = f'second_screen_{app.id}.png'
    app.second_screen_path.save(second_screen_filename, ContentFile(screenshot_data))

    # Stop video recording and save the video
    video_base64 = driver.stop_recording_screen()
    video_data = base64.b64decode(video_base64)
    video_filename = f'recording_{app.id}.mp4'
    app.video_record_path.save(video_filename, ContentFile(video_data)) 

    # Compare the current UI hierarchy with the previous one
    app.screen_changed = driver.page_source != app.ui_hierarchy
    app.save()
    driver.quit()

# Run script
if __name__ == "__main__":
    run_app(int(sys.argv[1]))
