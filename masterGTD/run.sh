nohup gunicorn --reload masterGTD.wsgi > /dev/null 2> ~/error.log &
