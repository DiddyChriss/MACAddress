# MACAddresss
> Simple app to get company name  from MAC address

## Table of contents
* [Technologies](#technologies)
* [Instruction](#instructions)
* [Status](#status)
* [Contact](#contact)


## Technologies
* Python - version 3.8

## Instructions
#### You can use docker file
#### Or just use requirements.txt to install libraries (pip install -r requirements.txt)
#### Import class from MACAddress.py (from MACAddress import GetDataByMACAddress)
#### Create instances of class ( mac = GetDataByMACAddress())
#### Use function company_name to get name of the company from data (mac.company_name('44:38:39:ff:ef:57'))
#### More security way i to use company_name_headers function with two parameters, MACAddress and security key
#### Your security key, you will find after register on website 'https://macaddress.io/' 
#### Try (mac.company_name_headers('mac address', 'your security key'))

## Status
Finish

## Contact
Created by [DiddyChriss] (http://chriss.pythonanywhere.com/) - feel free to contact me!
