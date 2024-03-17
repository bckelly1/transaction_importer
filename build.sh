#!/bin/bash

docker build . -t transaction_importer
docker compose up -d


