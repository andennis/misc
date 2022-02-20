#!/bin/bash

db_name="openproject"
attachments_dir="/home/openproject/openproject/files"
cur_date=$(date +"%d-%m-%Y")
backup_dir="/tmp/openproject_backup_${cur_date}"
db_backup_filename="${db_name}_${cur_date}"

while [ $# -gt 0 ]; do
  case "$1" in
    --db-name=*)
      db_name="${1#*=}"
      ;;
    --attachments-dir=*)
      attachments_dir="${1#*=}"
      ;;
    --backup-dir=*)
      backup_dir="${1#*=}"
      ;;
    *)
      printf "Error: Invalid argument: $1\n"
      exit 1
  esac
  shift
done

if [ -z "$db_name" ];
then
  echo "The parameter --db-name is not specified"
  exit 1
fi
if [ -z "$attachments_dir" ];
then
  echo "The parameter --attachments_dir is not specified"
  exit 1
fi
if [ -z "$backup_dir" ];
then
  echo "The parameter --backup_dir is not specified"
  exit 1
fi

if [ ! -d $backup_dir ]; 
then
  mkdir -p $backup_dir/attachments;
fi

echo "-----------Parameters----------------"
echo "OpenProject DB name: $db_name"
echo "OpenProject attachments directory: $attachments_dir"
echo "OpenProject backup directory: $backup_dir"
echo "-------------------------------------"
echo
echo "Backing up DB ${db_name} to ${backup_dir}/${db_backup_filename}"
#su - postgres
#pg_dump ${db_name} > ${backup_dir}/${db_backup_filename}
#logout

echo "Copying attacments to $backup_dir/attachments"
cp -r ${attachments_dir}/* ${backup_dir}/attachments