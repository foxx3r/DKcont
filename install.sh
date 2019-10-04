#!/usr/bin/env bash
clear
echo "checking if you have pip installed on your machine: "
sleep 1
if [[ ! -e /usr/bin/pip3 ]]
then
  clear
  echo -e "checking if you have pip installed on your machine: \033[01;31not\033[0;0m"
  sleep 1
  echo "installing pip3..."

  if [[ -e /usr/bin/apt ]]
  then
    sudo apt-get install python3-pip -y > /dev/null
    echo "pip3 was successfully installed"
  elif [[ -e /usr/bin/yum ]]
  then
    sudo yum -y install python3-pip > /dev/null
    echo "pip3 was successfully installed"
  elif [[ -e /usr/bin/pacman ]]
  then
    sudo pacman -S python3-pip -y
    echo "pip3 was successfully installed"
  elif [[ -e /sdcard ]]
  then
    pkg install python -y > /dev/null
    echo "pip3 was successfully installed"
  else
    echo "your operating system is not supported by this script :("
    exit 1
  fi
else
  clear
  echo -e "checking if you have pip installed on your machine: \033[01;32mOk\033[0;0m"
fi

echo "installing the dependencies"
sleep 2
echo "[####] 25 %"
pip3 install wikipedia > /dev/null
echo "[######] 50 %"
pip3 install art --no-warn-script-location > /dev/null
echo "[##########] 100 %"
sleep 1
echo "you are ready to use the script"
