#error catching
trap_msg='s=${?}; echo "${0}: Error on line "${LINENO}": ${BASH_COMMAND}"; exit ${s}'
set -uo pipefail
trap "${trap_msg}" ERR

curl -X POST http://apiexample.ethanlambert.info:8000/upload-file/ -H 'Content-Type: application/json' -d '{"name": "test-file-1.txt",
"folder": "test",
"topics": [
   "first",
   "second"
]}'
