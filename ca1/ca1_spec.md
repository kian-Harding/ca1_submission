% Cloud Technologies CA1

**Deadline:** as displayed on Moodle

**Weight:** 30%

# Aim

You will design and implement a suite of cloud services for a provided case study on AWS. (As per module descriptor).
This will be primarily based around infrastructure as code. 

# System description

Files uploaded to an S3 bucket should trigger a Python Lambda function employing Amazon Rekognition to detect Celebrities in the picture and store the picture's name and detected celebrities in DynamoDB. 

Note 1: Rekognition is a just one of a suite of services available in AWS that allows you to include AI services easily in your own programs. We will study it and others in class so that you are comfortable trying out and using new services yourself.

Note 2: If you are interested in something else instead of celebrity-spotting, like spotting wildlife, trains, ships, art etc feel free to do a similar example. 

# Deliverables

<<<<<<< HEAD:cloud_technologies_ca1.md
## Case study description (10%)

Description of your case study following approval and feedback `description.txt`.

## CloudFormation file (35%)
=======
## CloudFormation file (30%)
>>>>>>> 00a37f8 (ca1):ca1_spec.md

The CloudFormation file should setup all resources needed.
File should be named `ca1_template.yaml`.

<<<<<<< HEAD:cloud_technologies_ca1.md
## Setup file (15%)
=======
## Lambda function (30%)

The lambda function file should be called recogniser.py.

## Setup file (10%)
>>>>>>> 00a37f8 (ca1):ca1_spec.md

The setup file should create a stack from your cloudformation file, and should be called `setup.ps1`.
It should carry out any other setup activities pre/post the stack creation. 

## Demonstration script (10%)

Script that will show your system in operation. `demo.ps1`
You may need to include other resources (e.g. other scripts / programs / data files).

## Teardown file (10%)

The teardown file `teardown.ps1` should remove all resources created, including calling `aws cloudformation delete-stack` on the stack created. 
If you have made S3 buckets you should delete their contents first. 

## Development process (10%)

Use of version control evidenced by Git commits.

# Checking your submission for compliance

Your work should be checked using the `ca1_checks.ps1` file that will check your submission for compliance with the required files and naming.
Files that are mis-named or in the wrong format will receive a zero mark.

# How to submit your work

You will submit your work by means of a Git zip file.
This will encapsulate the changes you've made relative to the starting repository in a single file.

## Submission to Moodle

Submit *ONLY* your git patch file named *exactly* `ca1_submission.zip` to Moodle.
Do not alter the filename. 

# Feedback

Summary feedback will be given on Moodle.
Verbal feedback is available on request.
