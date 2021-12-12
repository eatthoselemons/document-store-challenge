from unittest import TestCase
import json
import requests
import os

with open(os.path.join(os.getcwd(), '../test-config.json')) as config:
    baseUrl = json.load(config)['baseUrl']


class BasicApiTests(TestCase):
    def setUp(self) -> None:
        # file 1
        url = baseUrl + "upload-file/"
        send_json = {"name": "test-file-1.txt",
                     "folder": "test",
                     "topics": [
                         "first",
                         "second"
                     ]}
        r = requests.post(url, json=send_json)

        # file 2

        url = baseUrl + "upload-file/"
        send_json = {"name": "test-file-2.txt",
                     "folder": "test",
                     "topics": [
                         "hello"
                     ]}
        r = requests.post(url, json=send_json)

        # file 3

        url = baseUrl + "upload-file/"
        send_json = {"name": "test-file-3.txt",
                     "folder": "other",
                     "topics": [
                         "first",
                         "last"
                     ]}
        r = requests.post(url, json=send_json)
        # upload test files

    def test_get_all_topics(self):
        """get list of every topic in the database"""
        url = baseUrl + "all-topics/"
        r = requests.get(url)
        expected_json = {
            "all topics": [
                "first",
                "second",
                "last"
            ]
        }
        self.assertEqual(r.json, expected_json)

    def test_search_for_files_by_folder(self):
        """Searches for all files that are inside a folder that is sent via json"""
        url = baseUrl + "search-folder/"
        search_json = {"folder": "test"}
        r = requests.post(url)
        expected_json = {
            "matching files": [
                "test-file-1.txt",
                "test-file-2.txt"
            ]
        }
        self.assertEqual(r.json, expected_json)

    def test_search_for_files_by_topic(self):
        """Searches for all files that match a topic, topic is sent via json"""
        url = baseUrl + "search-topic/"
        search_json = {"topic": "first"}
        r = requests.post(url)
        expected_json = {
            "matching files": [
                "test-file-1.txt",
                "test-file-3.txt"
            ]
        }
        self.assertEqual(r.json, expected_json)
