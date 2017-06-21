#!/usr/bin/expect
#USAGE: ./add_user.sh ADDRESS USER PASSWORD USERNEW
#EXAMPLE: ./add_user.sh 172.30.14.102 admn admn newguy
set address [lindex $argv 0]
set user [lindex $argv 1]
set psswrd [lindex $argv 2]
set usrnew [lindex $argv 3]
spawn ssh -t $user@$address 
expect '$'
send "sudo useradd $usrnew\r"
expect "$user:"
send "$psswrd\r";
expect '$'
send "sudo usermod -a -G git $usrnew\r"
expect '$'
send "exit\r"
expect eof