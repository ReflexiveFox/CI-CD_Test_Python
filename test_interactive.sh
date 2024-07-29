#!/usr/bin/expect -f

set timeout 10
# Start the interactive program
spawn python app.py

# Interaction 1: Greet operation
expect "Enter your choice: "
send "1\r"

# Enter name
expect "Enter a name: "
send "Tester\r"

# Expect greeting message
expect 
{
    "Hello Tester!\r"{}
    timeout 
    {
        puts "Timeout while waiting for greeting"
        exit 1
    }
}

# Interaction 2: Add numbers
expect "Enter your choice: "
send "2\r"

# Enter first number
expect "Enter first number: "
send "3\r"

expect "Enter second number: "
send "6\r"

expect 
{
    "The sum of 3.0 and 6.0 is 9.0" {}
    timeout
    {
        puts "Timeout while waiting for sum result"
        exit 1
    }
}

expect "Enter your choice: "
send "21039\r"

expect "Enter your choice: "
send "6\r"

expect eof
