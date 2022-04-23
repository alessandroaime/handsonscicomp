#!/bin/bash

get_basename () {
  FILENAME="${1##*/}"
  echo "${FILENAME%%.*}"
}

get_extension () {
  FILENAME="${1##*/}"
  if [[ $FILENAME == *"."* ]]
  then
    echo "${FILENAME##*.}"
  else
    echo ""
  fi
}
