import unittest
from unittest import TestCase
import requests
import json
import os

with open(os.path.join(os.getcwd(), '../test-config.json')) as config:
    baseUrl = json.load(config)['baseUrl']


class FileApiTests(TestCase):
    def test_upload_file(self):
        """uploads a file with dummy data"""
        url = baseUrl + "upload-file/"
        send_json = {"name": "test-file-1.txt",
                     "folder": "test",
                     "topics": [
                         "first",
                         "second"
                     ]}
        r = requests.post(url, json=send_json)
        expected_json = {
            "message": "new file added with name test-file-1.txt"
        }
        self.assertEqual(r.json, expected_json)

    @unittest.skip("not implemented")
    def test_download_file(self):
        pass
        # download a file by filename

    @unittest.skip("not implemented")
    def test_delete_file(self):
        url = baseUrl + "delete-file/"
        send_json = {"name": "test-file-1.txt",
                     "folder": "test",
                     }
        r = requests.post(url, json=send_json)
        expected_json = {
            "message": "file deleted by name test-file-1.txt"
        }
        self.assertEqual(r.json, expected_json)
        pass
        # delete a file by filename and folder
