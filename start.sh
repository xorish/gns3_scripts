#!/bin/bash
apt-get update
apt-get install -y nano
apt-get install -y net-tools
apt-get install -y iputils-ping
systemctl disable systemd-networkd-wait-online.service
systemctl mask systemd-networkd-wait-online.service