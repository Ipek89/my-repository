# Project-001 : Roman Numerals Converter Application (Python Flask) deployed on AWS EC2 with Cloudformation

## Description
The Roman Numerals Converter Application aims to convert the given number to the Roman numerals. The application is to be coded in Python and deployed as a web application with Flask on AWS Elastic Compute Cloud (EC2) Instance using AWS Cloudformation Service. 

## Problem Statement

![Project_001](Project_001_.png)

- Your company has recently started on a project that aims to be one of the most used unit converters and formulas website. Roman Numerals Converter is the part of the project. So you and your colleagues have started to work on the project.

- As a first step of the project, you need to write program that converts the given number (between 1 and 3999) to the roman numerals. The program should convert only from numbers to Roman numerals, not vice versa and during the conversion following notes should be taken into consideration.
   
```
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
- Symbol       Value
- I             1
- V             5
- X             10
- L             50
- C             100
- D             500
- M             1000
- For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.
- Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.
```

- User input can be either integer or string, thus the input should be checked for the followings,

   - The input should be a decimal number within the range of 1 to 3999, inclusively.
   
   - If the input is less then 1 or greater then 3999, user should be warned using the given html template.

   - If the input is string and can not be converted to decimal number, user should be warned using the given html template.

- Example for user inputs and respective outputs

```
Input       Output
-----       ------
3           III
9           IX
58          LVIII
1994        MCMXCIV
-8          Warning with "Not Valid! Please enter a number between 1 and 3999, inclusively."
4500        Warning with "Not Valid! Please enter a number between 1 and 3999, inclusively."
Ten         Warning with "Not Valid! Please enter a number between 1 and 3999, inclusively."
```
   
- As a second step, after you finish the coding, you are requested to deploy your web environment using Python's Flask framework.

- You need to transform your program into web application using the `index.html` and `result.html` within the `templates` folder. Note the followings for your web application.
   
   - User should face first with `index.html` when web app started.

   - User input should be taken via `index.html` using http post method
   
   - If user input is not valid, user should be warned using the `index.html` with template formatting.

   - Conversion result should be displayed using the `result.html` with template formatting. 

- Lastly, after transforming your code into web application, you are requested to push your program to the project repository on the Github and deploy your solution in the development environment on AWS EC2 Instance using AWS Cloudformation Service to showcase your project. In the development environment, you can configure your Cloudformation template using the followings,

   - The application stack should be created with new AWS resources. 

   - The application stack should take the name of your Key Pair as a parameter from the user;

   
   - The application should run on Amazon Linux 2 EC2 Instance

   - EC2 Instance type can be configured as `t2.micro`.

   - Instance launched by Cloudformation should be tagged `Web Server of StackName` 

   - The Web Application should be accessible via web browser and terminal from anywhere.

   - The Application files should be downloaded from Github repo and deployed on EC2 Instance using user data script within cloudformation template. 

   - Roman Numerals Converter Application Website URL should be given as output by Cloudformation Service, after the stack created.

## Project Skeleton 

```
001-roman-numerals-converter (folder)
|
|----readme.md         # Given to the students (Definition of the project)          
|----cfn-template.yml  # To be delivered by students (Cloudformation template)
|----app.py            # To be delivered by students (Python Flask Web Application)
|----templates
        |----index.html  # Given to the students (HTML template)
        |----result.html # Given to the students (HTML template)
```

## Expected Outcome

![Project 001 Snapshot](project-001-snapshot.png)

### At the end of the project, following topics are to be covered;

- Algorithm design

- Programming with Python 

- Web application programming with Python Flask Framework 

- Bash scripting

- AWS EC2 Service

- AWS Security Groups Configuration

- AWS Cloudformation Service

- AWS Cloudformation Template Design

- Git & Github for Version Control System

### At the end of the project, students will be able to;

- improve coding skills using iterables(dict), operators, for-loop, if statements and functions within Python

- improve web programming skills using HTTP GET/POST methods, template formatting, importing packages within Python Flask Framework

- improve bash scripting skills using `user data` section in Cloudformation to install and setup web application on EC2 Instance

- configure AWS EC2 Instance and Security Groups.

- configure Cloudformation template to use AWS Resources.

- use AWS Cloudformation Service to launch stacks.

- use git commands (push, pull, commit, add etc.) and Github as Version Control System.

## Steps to Solution
  
- Step 1: Download or clone project definition from `clarusway-aws-workshop` repo on Github 

- Step 2: Create project folder for local public repo on your pc

- Step 3: Write the Roman Numerals Converter Application in Python

- Step 4: Transform your application into web application using Python Flask framework

- Step 5: Prepare a cloudformation template to deploy your app on EC2 Instance

- Step 6: Push your application into your own public repo on Github

- Step 7: Deploy your application on AWS Cloud using Cloudformation template to showcase your app within your team.

## Notes

- Use the template formatting library `jinja` within Flask framework to leverage from given templates.

- Use given html templates to warn user with invalid inputs

- Customize the application by hard-coding your name for the `developer_name` variable within html templates.

## Resources

- [Python Flask Framework](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

- [Python Flask Example](https://realpython.com/flask-by-example-part-1-project-setup/)

- [AWS Cloudformation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)





# We should update yum package and install AWS CLI v2. (for more information to install AWS CLI V2 please look at https://docs.aws.amazon.com./cli/latest/userguide/install-cliv2-linux.html)

'''bash
sudo yum update -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"


unzip awscliv2.zip
sudo ./aws/install
aws --version
'''

aws account id command
aws sts get-caller-identity --query Account --output text

Creating security group on cli
 aws ec2 create-security-group --group-name my-sg --description "Roman_numbers_sec_grp_ipk "

 We can check the security Group with these commands
 '''bash
 aws ec2 describe-security-groups --filters Name=group-name,Values=my-sg

aws ec2 inbound rules ekleme
aws ec2 authorize-security-group-ingress --group-id sg-0c8c100883b6d2089 --protocol tcp --port 22 --cidr 0.0.0.0/0

open 80 port also 

aws ec2 authorize-security-group-ingress --group-id sg-0c8c100883b6d2089 --protocol tcp --port 80 --cidr 0.0.0.0/0

pulling latest ami
aws ssm.get-parameters

aws ssm get-parameters --names "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2" --query "Parameters[0].Value" --region us-east-1

Now we can run thr instance with CLI command. (Do not forget to create userdata.sh under /home/ec2-user/ folder bfr run this command)
'''bash
touch userdata.sh
vim userdata.sh
#! bin/bash
yum update -y
yum install python3
pip3 install flask
cd /home/ec2-user
FOLDER="https://raw.githubusercontent.com/Ipek89/my-repository/main/projects/001-roman-numerals-converter/roman-numerals-converter-"
wget ${FOLDER}/roman-numerals-converter-app.py
mkdir templates && cd templates
wget ${FOLDER}/templates/index.html
wget ${FOLDER}/templates/result.html
cd ..
python3 roman-numerals-converter-app.py

run userdata sh with this command:
aws ec2 run-instances --image-id ami-0f96c63e39f9144bc --count 1 --instance-type t2.micro --key-name ipek_aws --security-group-ids sg-0c8c100883b6d2089 --tag-specifications 'ResourceType=instance,Tags= [{Key=Name,Value=roman_numbers}]' --user-data file:///home/ec2-user/userdata.sh
