curl https://bootstrap.pypa.io/get-pip.py -o pip.py
sudo python pip.py
rm pip.py
sudo pip install locustio
echo "Type 'locust --version' and see if installed successfully."
