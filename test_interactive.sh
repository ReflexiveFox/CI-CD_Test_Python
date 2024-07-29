#!/usr/bin/expect -f

set timeout -1

spawn python app.py

expect "Enter your choice: "
send "1\r"
expect "Enter a name: "
send "Tester\r"
expect "Hello Tester!\r"

expect "Enter your choice: "
send "2\r"
expect "Enter first number: "
send "3\r"
expect "Enter second number: "
send "6\r"
expect "The sum of 3 and 6 is 9"

expect "Enter your choice: "
send "21039\r"

expect "Enter your choice: "
send "6\r"

expect eof
