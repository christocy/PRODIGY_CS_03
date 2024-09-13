# PRODIGY_CS_03
Password Complexity Checker

## Overview

The **Password Complexity Checker** is a Python tool designed to evaluate the strength of a password based on several criteria. It checks for the password's length, the presence of uppercase and lowercase letters, numbers, and special characters. The tool provides feedback to help users create stronger passwords.

## Features

- **Length Check:** Ensures the password is at least 8 characters long.
- **Lowercase Letters:** Validates the presence of at least one lowercase letter.
- **Uppercase Letters:** Validates the presence of at least one uppercase letter.
- **Numbers:** Checks for at least one numeric digit.
- **Special Characters:** Checks for at least one special character (e.g., @, $, !, etc.).
- **Feedback:** Provides specific feedback if the password does not meet the criteria.

## Installation
To use this tool, you need to have Python installed on your system. This script does not require any external libraries.

1. Clone the repository:
 
 git clone https://github.com/christocy/Password-Complexity-Checker.git
    
2. Navigate to the project directory:

cd Password-Complexity-Checker
 

## Usage
1. Run the script:
python password_complexity_checker.py

2. Enter your password when prompted.

3. Review the feedback provided based on the password's strength.

## Example
Here is how the script might work:

Enter your password: P@ssw0rd

Password is very strong!

## If the password does not meet all criteria, you will receive specific feedback 

Enter your password: abcd 
Password is very weak.
Feedback:
- Password should be at least 8 characters long.
- Password should contain at least one uppercase letter.
- Password should contain at least one number.
- Password should contain at least one special character (e.g., @, $, !, etc.).

 ## This project is licensed under the MIT License.

This project was developed as part of a virtual internship at Prodigy InfoTech.
