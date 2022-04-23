#!/bin/bash

fibonacci() {
  if [[ $1 -lt 0 ]]
  then
    exit 1
  fi

  a=0
  b=1

  for (( i=0; i<$1; i++ ))
  do
    fn=$((a + b))
    a=$b
    b=$fn
  done

  echo "$a"
}
