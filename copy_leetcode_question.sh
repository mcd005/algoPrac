set -eu

QUESTION_NO=$1 
GENERATED_FILE=~/.leetcode/${QUESTION_NO}\.*
echo ${GENERATED_FILE}

NEW_FILENAME=$(cd ~/.leetcode/ && ls ${QUESTION_NO}\.* | sed -e "s/^[1-9][0-9]*\.//" -e "s/\-/\_/g")
echo $NEW_FILENAME

sed -i '/^#/d;/^$/d' ${GENERATED_FILE}

cp -n ${GENERATED_FILE} ./${NEW_FILENAME}