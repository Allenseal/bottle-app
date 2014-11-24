HOME_PATH=/home/bottle

cp -r $HOME_PATH/bottle-build/web-app $HOME_PATH
sudo chgrp -R www $HOME_PATH/web-app
sudo chmod g+rw $HOME_PATH/web-app
mkdir $HOME_PATH/web-app/logs

cd $HOME_PATH/bottle-build
mysql -u root -p < schema.sql

# Set init.d
sudo cp $HOME_PATH/bottle-build/init.d/* /etc/init.d
sudo cp $HOME_PATH/bottle-build/nginx-conf/* /etc/nginx/conf.d
sudo mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.backup
sudo chmod u+x /etc/init.d/uwsgi-bottle
sudo update-rc.d nginx defaults
sudo update-rc.d uwsgi-bottle defaults

#sudo service uwsgi-bottle start
#sudo service nginx restart
