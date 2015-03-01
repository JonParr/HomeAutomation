#!/usr/bin/env bash
set -e

echo Starting connection to lamp...
python SmartPlug/lampConnection.py

ADDR=$(ifconfig | grep -A1 wlan0 | grep "inet addr" | cut -f 2 -d ':' | cut -f 1 -d ' ')

echo Starting php server at ${ADDR}..

cd WebInterface && php -S 0.0.0.0:8000


