#error catching
trap_msg='s=${?}; echo "${0}: Error on line "${LINENO}": ${BASH_COMMAND}"; exit ${s}'
set -uo pipefail
trap "${trap_msg}" ERR

curl -X GET http://apiexample.ethanlambert.info:8000/all-topics/ 
