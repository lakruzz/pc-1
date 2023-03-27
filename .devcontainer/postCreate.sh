#!/usr/bin/env bash

git config --local --add include.path ../.gitconfig

curl -L https://github.com/planetscale/cli/releases/download/v0.131.0/pscale_0.131.0_linux_amd64.deb --output /tmp/pscale_0.131.0_linux_amd64.deb
sudo dpkg -i /tmp/pscale_0.131.0_linux_amd64.deb
rm /tmp/pscale_0.131.0_linux_amd64.deb

cat <<EOF > $(git rev-parse --show-toplevel)/tmp/mysql.list
### THIS FILE IS AUTOMATICALLY CONFIGURED ###
# You may comment out entries below, but any other modifications may be lost.
# Use command 'dpkg-reconfigure mysql-apt-config' as root for modifications.
#deb http://repo.mysql.com/apt//ubuntu/ focal mysql-apt-config
deb http://repo.mysql.com/apt//ubuntu/ focal mysql-8.0
deb http://repo.mysql.com/apt//ubuntu/ focal mysql-tools
#deb http://repo.mysql.com/apt//ubuntu/ focal mysql-tools-preview
#deb-src http://repo.mysql.com/apt//ubuntu/ focal mysql-8.0
EOF

sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 3A79BD29
sudo mv /tmp/mysql.list /etc/apt/sources.list.d/mysql.list

sudo apt-get update
sudo apt-get install -y mysql-client
