#!/bin/bash
# Script for connectivity testing

# Test connectivity to AWS RDS instance
ping -c 4 <AWS_RDS_ENDPOINT>

# Test database connection (MySQL example)
mysql -h <AWS_RDS_ENDPOINT> -u <DB_USERNAME> -p<DB_PASSWORD> -e "SHOW DATABASES;"
