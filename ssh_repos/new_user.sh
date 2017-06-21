#!/usr/bin/expect
#USAGE: ./add_user.sh ADDRESS USER PASSWORD USERNEW
#EXAMPLE: ./add_user.sh 172.30.14.102 admn admn newguy
set address [lindex $argv 0]
set admin [lindex $argv 1]
set password [lindex $argv 2]
set user_new [lindex $argv 3]
spawn ssh -t $admin@$address 
expect '#'
send "$password\r";
expect '#'
send "sudo useradd $user_new\r"
expect '#'
send "$password\r";
expect '#'
send "exit\r"
expect eof