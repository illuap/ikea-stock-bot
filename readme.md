# Setting up Cron Exec

This will cause the program to run every 5 minutes (300 secs)

'''
#!/bin/sh  
while true  
do  
  acd_cli sync  
  sleep 300  
done

'''

sudo chmod +x /usr/local/bin/filenamehere