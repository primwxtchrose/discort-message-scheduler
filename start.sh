#!/bin/bash

# Activate the local Python installation if necessary
PYTHON_EXEC="/home/container/.local/bin/python3"

# Fallback to system Python if local one doesn't exist
if [ ! -x "$PYTHON_EXEC" ]; then
    PYTHON_EXEC=$(which python3)
fi

# Final fallback (least preferred)
if [ ! -x "$PYTHON_EXEC" ]; then
    PYTHON_EXEC="/usr/bin/python3"
fi

# Run the bot
exec "$PYTHON_EXEC" /home/container/main.py
