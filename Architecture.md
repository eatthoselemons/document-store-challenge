## Database Tables in PlantUML
<code>
@startjson
{
    "documents": [
        "id",
        "name",
        "location id" : [
            "id",
            "location"
        ],
        "topics": [
            "document id",
            "topic id": [
                "id",
                "name"
            ]
        ]
    ]
}
@endjson
</code>

#### List View:
- documents
  - id
  - name
  - location id
- folders
  - id
  - location
- topic ids
  - document id
  - topic id
- topic names
  - id
  - name