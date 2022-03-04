set -eu

QUESTION_NO=$1 

NEW_FILENAME=$(cd ~/.leetcode/ && ls ${QUESTION_NO}\.* | sed -e "s/^[1-9][0-9]*\.//" -e "s/\-/\_/g")
echo $NEW_FILENAME

cp -n ~/.leetcode/${QUESTION_NO}\.*  ./${NEW_FILENAME}