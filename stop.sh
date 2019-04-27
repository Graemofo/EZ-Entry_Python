#!/bin/bash
while read PBASE_PID; do kill PBASE_PID; done < pbase_pid.txt &
while read FACE_PID; do kill PID; done < face_pid.txt &
while read PULL_PID; do kill PULL_PID; done < pull_pid.txt &
