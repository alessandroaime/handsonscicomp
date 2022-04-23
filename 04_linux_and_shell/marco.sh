#!/bin/bash

DIR=""

marco () {
  DIR=$PWD
}

polo () {
  if [[ -n $DIR ]]
  then
    cd $DIR
  fi
}
