#!/bin/sh

while test 1 # infinite loop
do
    nc -l 192.168.43.202 4040 > /tmp/4040.log

    # check for start
    grep start /tmp/4040.log > /dev/null

    if test $? -eq 0 
    then
        systemctl suspend
    else
        # check for stop
        grep stop /tmp/4040.log > /dev/null

        if test $? -eq 0 
        then
            echo Stop
        fi
    fi
done
