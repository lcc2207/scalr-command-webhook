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
fi

if [ $event == "HostUp" ];
 then
  echo "adding $hostname to xxx"
  echo $hostname >>  /opt/hostinfo/infra_hosts
fi

if [ $event == "HostDown" ];
 then
  echo "removing $hostname from xxx"
  sed -i "/$hostname/d" /opt/hostinfo/infra_hosts
fi
