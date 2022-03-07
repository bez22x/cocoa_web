sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo systemctl enable docker
sudo service docker status
sudo usermod -a -G docker ec2-user
sudo usermod -a -G docker $USER
sudo mkdir data
sudo docker run -d -p 27017:27017 -v ${pwd}/data:/data/db mongo