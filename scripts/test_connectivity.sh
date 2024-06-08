#!/bin/bash

echo "Testing connectivity to RDS instance..."
mysql -h cli-db-vrishank.clmiomuk2ofd.ap-south-1.rds.amazonaws.com -u admin -pYourPassword -e "SHOW DATABASES;"
