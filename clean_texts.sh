#!/usr/bin/env bash

set -e
set -x

for f in texts/*.txt; do
  sed -i s:‘:\': $f # remove the weird mac quotations so they don't line up
  sed -i s:’:\': $f
  sed -i s:\_:: $f # underlines commonly used for italics, but we don't care about those here
done
