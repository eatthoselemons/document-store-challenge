#error catching
trap_msg='s=${?}; echo "${0}: Error on line "${LINENO}": ${BASH_COMMAND}"; exit ${s}'
set -uo pipefail
trap "${trap_msg}" ERR


source ../../setup/config.shlib

# read config file
dbpassword=$(getConfigVar ../../setup/config.cfg localDatabasePassword)

export PGPASSWORD=$dbpassword

psql -h localhost -U postgres documentStore -c "\dt"


export PGPASSWORD=

