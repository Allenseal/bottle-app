# add steam user
sudo groupadd www
sudo useradd -s /bin/bash -m bottle
echo 'bottle:bottle@www' | sudo chpasswd
sudo usermod -aG www bottle
sudo adduser bottle sudo
sudo sh -c 'echo "bottle    ALL=(ALL:ALL) NOPASSWD:ALL" >>  /etc/sudoers.d/www_sudoers'
sudo chmod 0440 /etc/sudoers.d/www_sudoers

# install zip
sudo apt-get install unzip zip
zip -r bottle-build.zip bottle-build
sudo cp bottle-build.zip /home/bottle
sudo chown bottle /home/bottle/bottle-build.zip
sudo su - bottle -c "unzip bottle-build.zip"
sudo su - bottle -c ". bottle-build/install.sh"
