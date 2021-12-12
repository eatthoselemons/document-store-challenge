from unittest import TestCase
import requests
import json
import os

with open(os.path.join(os.getcwd(), '../test-config.json')) as config:
    baseUrl = json.load(config)['baseUrl']


class FileApiTests(TestCase):
    def upload_file(self):
        """uploads a file with dummy data"""
        files = {'upload_file': open('../test-file-1.txt', 'r')}
        url = baseUrl.concat("upload-file/")
        send_json = { "name": "test-file-1.txt",
                 "folder": "test",
                 "topics": [
                     "first",
                     "second"
                 ]}
        r = requests.post(url, files=files, json=send_json)
        expected_json = {
            "message": "new file added with name test-file-1.txt"
        }
        self.assertEqual(r.json, expected_json)

    def download_file(self):
        pass
        # download a file by filename

    def delete_file(self):
        url = baseUrl.concat("delete-file/")
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

