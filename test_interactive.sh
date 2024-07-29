
#!/usr/bin/expect -f

# Set timeout to 10 seconds for all expect commands
set timeout 10

# Start the interactive program
spawn python interactive.py

# First interaction: Choose option 1 (Greet)
expect {
    "Enter your choice: " {
        send "1\r"
    }
    timeout {
        puts "Timeout while waiting for choice prompt"
        exit 1
    }
}

# Enter name after choosing Greet
expect {
    "Enter your name: " {
        send "Tester\r"
    }
    timeout {
        puts "Timeout while waiting for name prompt"
        exit 1
    }
}

# Expect the greeting message
expect {
    "Hello, Tester!\r"
    timeout {
        puts "Timeout while waiting for greeting"
        exit 1
    }
}

# Second interaction: Choose option 2 (Add Numbers)
expect {
    "Enter your choice: " {
        send "2\r"
    }
    timeout {
        puts "Timeout while waiting for choice prompt"
        exit 1
    }
}

# Enter first number
expect {
    "Enter first number: " {
        send "3\r"
    }
    timeout {
        puts "Timeout while waiting for first number prompt"
        exit 1
    }
}

# Enter second number
expect {
    "Enter second number: " {
        send "4\r"
    }
    timeout {
        puts "Timeout while waiting for second number prompt"
        exit 1
    }
}

# Expect the sum result
expect {
    "The sum is: 7.0\r"
    timeout {
        puts "Timeout while waiting for sum result"
        exit 1
    }
}

# Third interaction: Choose option 3 (Calculate Factorial)
expect {
    "Enter your choice: " {
        send "3\r"
    }
    timeout {
        puts "Timeout while waiting for choice prompt"
        exit 1
    }
}

# Enter the number for factorial
expect {
    "Enter a non-negative integer: " {
        send "5\r"
    }
    timeout {
        puts "Timeout while waiting for factorial prompt"
        exit 1
    }
}

# Expect the factorial result
expect {
    "The factorial of 5 is: 120\r"
    timeout {
        puts "Timeout while waiting for factorial result"
        exit 1
    }
}

# Fourth interaction: Choose option 4 (Calculate Fibonacci)
expect {
    "Enter your choice: " {
        send "4\r"
    }
    timeout {
        puts "Timeout while waiting for choice prompt"
        exit 1
    }
}

# Enter the number for Fibonacci
expect {
    "Enter a non-negative integer: " {
        send "5\r"
    }
    timeout {
        puts "Timeout while waiting for Fibonacci prompt"
        exit 1
    }
}

# Expect the Fibonacci result
expect {
    "The Fibonacci sequence up to 5 is: \[0, 1, 1, 2, 3, 5\]\r"
    timeout {
        puts "Timeout while waiting for Fibonacci result"
        exit 1
    }
}

# Fifth interaction: Choose option 6 (Exit)
expect {
    "Enter your choice: " {
        send "6\r"
    }
    timeout {
        puts "Timeout while waiting for choice prompt"
        exit 1
    }
}

# End of file (EOF) expected
expect eof
