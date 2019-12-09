#!/usr/bin/env bash
sleep 25
celery -A run.celery worker --loglevel=info
