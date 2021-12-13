# document-store-challenge
Challenge to implement a document store

# Prerequisites
You will need these installed:
`docker, postgresql, python3, pip`

# Setup
clone this project
Put your password and secret key into a file named `config.cfg` in the `setup/` folder, with the format:
```
localDatabasePassword=<random password here>
secretKey=<random key here>
```
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

cd into `setup` and run:
`
$ bash update-database.sh
$ bash create-user-django.sh
$ start-django.sh
`

You now should be up and running, you can go run the unittests now
(`bash run-automated-tests.sh` inside the `test` folder)
