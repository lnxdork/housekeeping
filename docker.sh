# Setting up docker community on CentOS7
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum update -y
yum install -y docker-ce
systemctl enable docker && systemctl start docker && systemctl status docker

# docker images will fail if user is not a member of the docker group
sudo usermod -aG docker cloud_user
# need to login again to enable changes
# /bin/bash

# Set up a storage driver
docker info | grep Storage

# WARNING: the devicemapper storage-driver is deprecated, and will be removed in a future release.
# WARNING: devicemapper: usage of loopback devices is strongly discouraged for production use.
#          Use `--storage-opt dm.thinpooldev` to specify a custom block storage device.

sudo cd /etc/docker/ 
sudo touch daemon.json
sudo echo " \
{ \
  "storage-driver": "overlay2" \
}" >> daemon.json

systemctl stop docker.service && systemctl start docker.service

docker image pull httpd # where do we control a pull from?
docker images

docker container run -d --name lnxdorkweb -p 80:80 httpd

docker ps

docker container inspect lnxdorkweb | grep IPAddr

# make sure it works
curl $IPADDR

# logging drivers
docker logs lnxdorkweb

docker stop lnxdorkweb
docker rm lnxdorkweb

# Change to syslog
# vim /etc/rsyslog # uncomment syslog
# ModLoad imudp
# UDPServerRun 514

sudo systemctl restart rsyslog.service

# update the daemon.json with logging info
sudo echo "{ 
  "log-driver": "syslog",
  "log-opts": {
	"syslog-address": "udp://$IPADDR:514"
	}
}" >> daemon.json

systemctl stop docker.service && systemctl start docker.service
