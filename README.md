# Bottle with UWSGI+Nginx Quick Build

Building bottle application with api samples and sqlalchemy object.

# Usage

  1. Run commands with user who have `sudo`.

        sh install_server.sh
     
  2. You can find an user 'bottle'.
     Bottle application is in `/home/bottle/web-app`.

  3. Start UWSGI and Nginx

        sudo service uwsgi-bottle start
        sudo service nginx restart
