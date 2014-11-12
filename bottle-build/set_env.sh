
# Install packages
sudo apt-get update
sudo apt-get install git build-essential \
  zlib1g-dev libssl-dev libreadline-dev libyaml-dev \
  libcurl4-openssl-dev libpcre3 libpcre3-dev \
  sqlite3 libsqlite3-dev libsasl2-dev nodejs \
  python-software-properties python-setuptools \
  mysql-server libmysqlclient-dev python-dev \
  imagemagick libreoffice\
  postfix curl -y

# Setting python environment
sudo easy_install pip
sudo pip install setuptools --no-use-wheel --upgrade
sudo pip install mysql-python
sudo pip install sqlalchemy uwsgi cython bottle bottle_memcache bottle_sqlalchemy requests pyyaml

# Install memcahced
sudo apt-get install memcached -y

# Import nginx repos & Install
sudo su -c "echo 'deb http://nginx.org/packages/ubuntu/ lucid nginx
deb-src http://nginx.org/packages/ubuntu/ lucid nginx' > /etc/apt/sources.list.d/nginx.list"
sudo apt-get update
sudo apt-get install -y --force-yes nginx

sudo adduser nginx
sudo usermod -aG www nginx

#cp uwsgi
sudo cp /usr/local/bin/uwsgi /usr/local/bin/uwsgi-bottle
