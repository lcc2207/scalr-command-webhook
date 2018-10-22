#!/bin/bash

hostname=$1
ipaddress=$2
event=$3
scalr_server_id=$(echo $4 | jq '.SCALR_EVENT_SERVER_ID')

echo '-=-=-=-=-=-=-'
echo $hostname $ipaddress $event
echo '-=-=-=-=-=-=-'

if [ $event == "BeforeInstanceLaunch" ];
 then
  echo "Add host to XXX"
  echo $scalr_server_id >> /opt/hostinfo/ids_hosts
#  curl --data "host_config_key=16522fa0ee61399df56889b2b3c247f3" http://35.202.229.8:80/api/v2/job_templates/9/callback/
fi

if [ $event == "HostUp" ];
 then
  echo "adding $hostname to xxx"
  echo $hostname >>  /opt/hostinfo/infra_hosts
#  curl --data "host_config_key=16522fa0ee61399df56889b2b3c247f3" http://35.202.229.8:80/api/v2/job_templates/8/callback/
fi

if [ $event == "HostDown" ];
 then
  echo "removing $hostname from xxx"
  sed -i "/$hostname/d" /opt/hostinfo/infra_hosts
#  curl --data "host_config_key=16522fa0ee61399df56889b2b3c247f3" http://35.202.229.8:80/api/v2/job_templates/8/callback/
fi
