from unittest import TestCase
import json
import requests
import os

with open(os.path.join(os.getcwd(), '../test-config.json')) as config:
    baseUrl = json.load(config)['baseUrl']


class BasicApiTests(TestCase):
    def setUp(self) -> None:
        # file 1
        files = {'upload_file': open('../test-file-1.txt', 'r')}
        url = baseUrl.concat("upload-file/")
        send_json = {"name": "test-file-1.txt",
                     "folder": "test",
                     "topics": [
                         "first",
                         "second"
                     ]}
        r = requests.post(url, files=files, json=send_json)

        # file 2

        files = {'upload_file': open('../test-file-2.txt', 'r')}
        url = baseUrl.concat("upload-file/")
        send_json = {"name": "test-file-2.txt",
                     "folder": "test",
                     "topics": [
                         "hello"
                     ]}
        r = requests.post(url, files=files, json=send_json)

        # file 3

        files = {'upload_file': open('../test-file-3.txt', 'r')}
        url = baseUrl.concat("upload-file/")
        send_json = {"name": "test-file-3.txt",
                     "folder": "other",
                     "topics": [
                         "first",
                         "last"
                     ]}
        r = requests.post(url, files=files, json=send_json)
        # upload test files

    def get_all_topics(self):
        """get list of every topic in the database"""
        url = baseUrl.concat("all-topics/")
        r = requests.get(url)
        expected_json = {
            "all topics": [
                "first",
                "second",
                "last"
            ]
        }
        self.assertEqual(r.json, expected_json)

    def search_for_files_by_folder(self):
        """Searches for all files that are inside a folder that is sent via json"""
        url = baseUrl.concat("search-folder/")
        search_json = {"folder": "test"}
        r = requests.get(url)
        expected_json = {
            "matching files": [
                "test-file-1.txt",
                "test-file-2.txt"
            ]
        }
        self.assertEqual(r.json, expected_json)

    def search_for_files_by_topic(self):
        """Searches for all files that match a topic, topic is sent via json"""
        url = baseUrl.concat("search-folder/")
        url = baseUrl.concat("search-topic/")
        search_json = {"topic": "first"}
        r = requests.get(url)
        expected_json = {
            "matching files": [
                "test-file-1.txt",
                "test-file-3.txt"
            ]
        }
        self.assertEqual(r.json, expected_json)
        pass
