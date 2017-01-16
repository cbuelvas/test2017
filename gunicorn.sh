#!/bin/bash
 
NAME="Test2017"
FLASKDIR=/home/ubuntu/test2017
SOCKFILE=/home/ubuntu/test2017/sock
USER=root
GROUP=root
NUM_WORKERS=3
 
echo "Starting $NAME"
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your gunicorn
exec /home/ubuntu/venv/bin/gunicorn app:app -b 127.0.0.1:5005 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE
