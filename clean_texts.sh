#!/usr/bin/env bash

for f in texts/*.txt; do 
  sed -i s:‘:\': $f
  sed -i s:’:\': $f
done
