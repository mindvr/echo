#!/usr/bin/env python3

import os
import sys
import threading
import time
import unittest

import requests

# Add the src directory to the path so we can import the echo module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from echo import run_server


class TestEchoHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.port = 8888
        cls.server_thread = threading.Thread(
            target=run_server, 
            args=(cls.port,),
            daemon=True
        )
        cls.server_thread.start()
        time.sleep(0.5)
        cls.base_url = f"http://localhost:{cls.port}"

    def test_put_with_custom_header(self):
        """Test that a PUT request with X-Custom-Header returns the header in the response."""
        header_value = "test-value-put"
        response = requests.put(
            f"{self.base_url}/test-put",
            headers={"X-Custom-Header": header_value}
        )
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["method"], "PUT")
        self.assertEqual(data["path"], "/test-put")
        self.assertIn("X-Custom-Header", data["headers"])
        self.assertEqual(data["headers"]["X-Custom-Header"], header_value)

    def test_post_with_custom_header(self):
        """Test that a POST request with X-Custom-Header returns the header in the response."""
        header_value = "test-value-post"
        response = requests.post(
            f"{self.base_url}/test-post",
            headers={"X-Custom-Header": header_value}
        )
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["method"], "POST")
        self.assertEqual(data["path"], "/test-post")
        self.assertIn("X-Custom-Header", data["headers"])
        self.assertEqual(data["headers"]["X-Custom-Header"], header_value)


if __name__ == "__main__":
    unittest.main()