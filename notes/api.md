# API Docs

The api is pretty basic, as I couldn't figure out how to do vanilla django url parsing I used JSON payloads for searching etc
Because of the need for a payload to fit with convention most requests are **post** requests

The public api is at:
`apiexample.ethanlambert.info`

### Api Functions:
`/upload-file/`
`/delete-file/`
`/all-topics/`
`/search-folder/`
`/search-topic/`

### Upload-file
##### NOTE only takes one file at a time
url: `/upload-file/`
type: `post`
send payload in form:
`{ "name": <filename>,
    "folder": <destination folder>,
    "topics": [
        <list of topics>
    ]       
}`
response:
`{"message": "new file added with name <filename>"}`

### Delete-file
url: `/delete-file/`
type: `post`
send payload in form:
`{ 
    "name": <filename>,
    "folder": <folder>
}`
response:
`{"message": "file deleted by name <filename>}`

### All-topics
url: `/all-topics/`
type: `get`
no payload
response:
`{
    "all topics": [
        <list of topics>
    ]
}`

### Search-folder
url: `/search-folder/`
type: `post`
send payload in form:
`{"folder": <folder>}`
response:
`{
    "matching files": [
        <list of files>
    ]
}`

### Search-topic
url: `/search-topic/`
type: `post`
send payload in form:
`{"topic": <topic>}`
response:
`{
    "matching files": [
        <list of files>
    ]
}`
