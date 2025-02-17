#!/bin/bash
#get occurences of ERROR in logfile
grep -oE 'ERROR' server_log.txt | sort | uniq -c
