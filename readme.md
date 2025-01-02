# label-studio deployment

## label studio data dir

    ./label-studio-data

## set permission to folder before docker compose up
    chmod -R 777 ./label-studio-data

## file importing

run serve_local_files.sh
disable cors using extension to avoid cors error while importing file.txt

import file.txt
#./script/serve_local_files.sh <directory/with/files> *.jpg