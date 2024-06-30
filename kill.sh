#!/usr/bin/env bash
ps -ef|grep 'api.py'|awk '{print $2}'| xargs kill -9