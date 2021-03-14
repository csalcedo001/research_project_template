#!/bin/bash

if [[ -z $1 ]] ;
then
	echo 'error: missing first argument "old_package_name".'
	exit
fi

if [[ -z $2 ]] ;
then
	echo 'error: missing second argument "new_package_name".'
	exit
fi

OLD_NAME=$1
NEW_NAME=$2

mv $OLD_NAME $NEW_NAME

find . -type f -exec sed -i '' -- "s/$OLD_NAME/$NEW_NAME/g" {} +
