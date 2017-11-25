#!/bin/bash    
rm -rf /etc/yum.repos.d/CentOS-Base.repo
cd /etc/yum.repos.d/
wget --no-check-certificate https://raw.githubusercontent.com/MuhammadAli0/PY_Projects-/master/iptables/CentOS-Base.repo
yum -y update
yum -y install python*
yum -y install yum-utils 
yum -y install gcc
yum -y install gcc*
yum clean all
yum-builddep python
cd /opt/
mkdir dev
cd dev/
curl -O https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz 
tar -xfz Python-3.5.0.tgz
cd Python-3.5.0
./configure
make
make install
wget  --no-check-certificate  https://pypi.python.org/packages/11/b6/abcb525026a4be042b486df43905d6893fb04f05aac21c32c638e939e447/pip-9.0.1.tar.gz#md5=35f01da33009719497f01a4ba69d63c9
tar -xzf pip-9.0.1.tar.gz
cd pip-9.0.1
python3 setup.py install
python2.7 setup.py install
wget  --no-check-certificate  https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz
tar -xzf Python-2.7.14.tar.xz 
cd Python-2.7.14
./configure
make
make install
wget  --no-check-certificate  https://raw.githubusercontent.com/scalp42/python-2.7.x-on-Centos-5.x/master/install_python27.sh
chmod +x install_python27.sh 
./install_python27.sh 
wget  --no-check-certificate  https://pypi.python.org/packages/11/b6/abcb525026a4be042b486df43905d6893fb04f05aac21c32c638e939e447/pip-9.0.1.tar.gz#md5=35f01da33009719497f01a4ba69d63c9
tar -xzf pip-9.0.1.tar.gz
cd pip-9.0.1
python2.7 setup.py install
python3 setup.py install
wget https://codeload.github.com/pallets/flask/zip/master
unzip master
cd flask-master/
python2.7 setup.py build
python2.7 setup.py install
python3 setup.py build
python3 setup.py install
pip2.7 install flask
pip3 install flask
wget https://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-0.10.4.tar.gz --no-check-certificate
tar -xzf Werkzeug-0.10.4.tar.gz
cd Werkzeug-0.10.4
python3 setup.py install
python2.7 setup.py install
cd ..
wget https://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.7.3.tar.gz --no-check-certificate
tar -xzf Jinja2-2.7.3.tar.gz
cd Jinja2-2.7.3
python3 setup.py install
cd ..
wget https://pypi.python.org/packages/source/i/itsdangerous/itsdangerous-0.24.tar.gz --no-check-certificate
tar -xzf itsdangerous-0.24.tar.gz
cd itsdangerous-0.24
python3 setup.py install
cd ..
wget https://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-0.23.tar.gz --no-check-certificate
tar -zxf MarkupSafe-0.23.tar.gz
cd MarkupSafe-0.23
python3 setup.py install 
cd ..
wget https://pypi.python.org/packages/source/F/Flask/Flask-0.10.1.tar.gz --no-check-certificate
tar -xzf Flask-0.10.1.tar.gz
cd Flask-0.10.1
python3 setup.py install
cd ..
wget https://pypi.python.org/packages/00/39/e0cb46e47f283e56e24107ee36456788106e744be284c998fbe8c7a7096e/click-2.3-py2.py3-none-any.whl#md5=7898be3bf41c91d003dd9cced5a8b183 --no-check-certificate
pip3 install click-2.3-py2.py3-none-any.whl
cd Flask-0.12.2
python2.7 setup.py install
python3 setup.py install
cd /opt/
mkdir ssh_server
cd ssh_server
wget https://raw.githubusercontent.com/MuhammadAli0/PY_Projects-/master/SSHD_Hosts.Allow/ssh_server.zip --no-check-certificate
unzip ssh.py.zip

echo "\n\n\n\n\n\n edit the last line of the code to your machine ip\n"
echo "add this line to  'crontab -e' "
echo "* * * * * python3 /opt/ssh_server/demo.py"

'"

