#!/usr/bin/env bash

set -e

cd "$(dirname "$0")/.."

echo ''
echo 'LINTING Python'
echo ''

pylint --recursive=y .

echo ''
echo 'LINTING Yaml'
echo ''
yamllint .

echo ''
echo 'FINISHED LINTING!'
echo ''
