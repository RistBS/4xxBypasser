echo "installing pip..."
apt install python3-pip
echo "installing libs..."
pip3 install -r requirements.txt
ln -sf $(pwd)/4xxbypasser.py /usr/local/bin/4xxbypasser
echo "done !!!"
