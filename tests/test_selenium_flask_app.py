import unittest
from selenium import webdriver
import time
from threading import Thread
import requests
from app import app  # Import the Flask app

class TestFlaskApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Start the Flask app in a separate thread
        cls.flask_thread = Thread(target=app.run, kwargs={'use_reloader': False})
        cls.flask_thread.start()

        # Wait for the server to start
        time.sleep(2)

        # Setup Selenium WebDriver (e.g., Chrome)
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

        # Stop the Flask server
        cls.flask_thread.join()

    def test_home_page(self):
        driver = self.driver
        # Go to the Flask app home page
        driver.get("http://localhost:5000/")

        # Check if the page contains the expected text
        print(driver.page_source)
        self.assertIn("Hello, Flask!", driver.page_source)

    def test_post_json(self):
        # Send a POST request to the /echo endpoint
        url = "http://localhost:5000/echo"
        json_data = {"message": "Hello from test!"}

        # Send POST request with JSON data
        response = requests.post(url, json=json_data)

        # Assert the status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert the response JSON matches the sent data
        self.assertEqual(response.json(), json_data)

if __name__ == '__main__':
    unittest.main()
