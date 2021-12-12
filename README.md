# document-store-challenge
Challenge to implement a document store

# Prerequisites
You will need these installed:
`docker, postgresql, python3, pip`

# Setup
clone this project
`cd` into `setup/`
and run `bash install-database.sh`

##### NOTE: if you get container already in use (like from a previous run of this script) `bash delete-containers.sh` will remove the containers made in this setup script

`cd` to the main folder and run:
```
python3 -m venv ./venv/
source venv/bin/activate
python3 -m pip install -r requirements.txt
```
(use `deactivate` to leave the python virtual environment)