#!/bin/bash
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo dnf upgrade -y
# Add required dependencies for the jenkins package
sudo dnf install -y fontconfig java-17-openjdk
sudo dnf install -y jenkins
sudo systemctl daemon-reload
sudo systemctl enable --now jenkins