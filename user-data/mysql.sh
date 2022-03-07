sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo systemctl enable docker
sudo service docker status
sudo usermod -a -G docker ec2-user
sudo usermod -a -G docker $USER
sudo mkdir data
sudo docker run -d -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 -v ${pwd}/data:/var/lib/mysql mysql:5.7