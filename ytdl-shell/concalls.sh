#!/usr/bin/env bash
yt-dl -ciw -a ~/repos/concallviewer/ytdl-shell/pl_concall.txt -o "/home/pi/files/Downloads/ytdl/%(uploader)s/%(title)s -  %(upload_date)s.%(ext)s" --format=bestaudio[ext=m4a] --write-thumbnail --write-info-json --write-automatic-sub --playlist-end 295 --playlist-start 1
# last 5p are non earling call videos
