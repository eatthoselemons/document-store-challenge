trap_msg='s=${?}; echo "${0}: Error on line "${LINENO}": ${BASH_COMMAND}"; exit ${s}'
set -uo pipefail
trap "${trap_msg}" ERR

# source my config bash lib
source ./config.shlib

# read config file
dbpassword=$(getConfigVar config.cfg localDatabasePassword)
secretKey=$(getConfigVar config.cfg secretKey)

export PGPASSWORD=$dbpassword

echo "
{
  "secret-key": $secretKey,
  "db-password": $dbpassword
}" > secrets.json


# setup and run postgres docker container
echo "starting postgres docker container"
docker run --name postgres-db-document -e POSTGRES_PASSWORD=$dbpassword -p 5432:5432 -d postgres

# should be waiting don't know why
#until [ "`docker inspect -f {{.State.Running}} postgres-db`"=="true" ]; do
#    sleep 0.1;
#done;

sleep 10

# creating the db for the data
echo "creating database"
createdb -h localhost -U postgres -p 5432 -T template0 documentStore

# clear the password
export PGPASSWORD=""