# API Docs

The api is pretty basic, as I couldn't figure out how to do vanilla django url parsing I used JSON payloads for searching etc

The public api is at:
`apiexample.ethanlambert.info`

### Api Functions:
`/upload-file/`
`/delete-file/`
`/all-topics/`
`/search-folder/`
`/search-topic/`

### Upload-file
url: `/upload-file/`
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
send payload in form:
`{ 
    "name": <filename>,
    "folder": <folder>
}`
response:
`{"message": "file deleted by name <filename>}`

### All-topics
url: `/all-topics/`
no payload
response:
`{
    "all topics": [
        <list of topics>
    ]
}`

### Search-folder
url: `/search-folder/`
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
send payload in form:
`{"topic": <topic>}`
response:
`{
    "matching files": [
        <list of files>
    ]
}`
