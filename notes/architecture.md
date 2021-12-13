## Database Tables in PlantUML
<code>
@startjson
{
    "documents": [
        "title",
        "folder" : [
            "folder_name"
        ],
        "topics": [
            "topic id many to many": [
                "topic_name",
            ]
        ]
    ]
}
@endjson
</code>

#### Markdown View:
- documents
  - title
  - folder
  - topics
- folders
  - folder_name
- topic ids
  - document id
  - topic id
- topic names
  - topic_name
