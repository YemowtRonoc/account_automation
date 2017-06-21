#!/bin/bash
ADMIN_USERNAME=$1
ADMIN_PASSWORD=$2
REPO_SERVER=$3
USER_NAME=$4
BOOL_DEV=$5

INITIALS=""
for word in $USER_NAME; do
    INITIALS="$INITIALS${word:0:1}"
done

if [ "$BOOL_DEV" == "True" ]; then
    ./ssh_repos/new_user_dev.exp "$REPO_SERVER" "$ADMIN_USERNAME" "$ADMIN_PASSWORD" "$INITIALS"
else
    ./ssh_repos/new_user.exp "$REPO_SERVER" "$ADMIN_USERNAME" "$ADMIN_PASSWORD" "$INITIALS"
fi
