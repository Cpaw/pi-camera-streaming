#!/usr/bin/env bash

echo 'Install python libraries'
pip3 install git+https://github.com/dpallot/simple-websocket-server.git --user
pip3 install netifaces --user
pip3 install flask --user

echo 'Enable camera'
sudo raspi-config nonint do_camera 0

echo 'Disable camera red led'
echo 'disable_camera_led=1' | sudo tee -a /boot/config.txt

echo 'Reboot after 3s'
sleep 3
sudo systemctl reboot
