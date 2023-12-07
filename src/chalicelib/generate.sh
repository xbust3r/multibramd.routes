#!/bin/bash

USER_NAME=$1

echo "Generando API ROUTES para $USER_NAME ..."
mkdir api
cd api
mkdir $USER_NAME
cd $USER_NAME
touch __init__.py
touch route.py
cd ../..

echo "Generando estructura DDDPY de carpetas para $USER_NAME ..."
mkdir dddpy
cd dddpy
mkdir $USER_NAME
cd $USER_NAME
mkdir domain infrastructure usecase
touch __init__.py
touch domain/$USER_NAME.py
touch domain/${USER_NAME}_exception.py
touch domain/${USER_NAME}_repository.py
touch domain/${USER_NAME}_success.py
touch domain/${USER_NAME}_validation.py
touch infrastructure/__init__.py
touch infrastructure/${USER_NAME}.py
touch infrastructure/${USER_NAME}_cmd_repository.py
touch infrastructure/${USER_NAME}_query_repository.py
touch usecase/__init__.py
touch usecase/${USER_NAME}_factory.py
touch usecase/${USER_NAME}_cmd_schema.py
touch usecase/${USER_NAME}_cmd_usecase.py
touch usecase/${USER_NAME}_query_schema.py
touch usecase/${USER_NAME}_query_usecase.py
touch usecase/${USER_NAME}_usecase.py

echo "terminado"