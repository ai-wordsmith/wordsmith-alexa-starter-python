# Wordsmith Starter Kit for making Alexa Skills with AWS Lambda (Python 2.7)
This repo will jump-start you on the code you need to respond to [Amazon Alexa](https://developer.amazon.com/alexa) Skills requests using [AWS Lambda](https://aws.amazon.com/lambda/) functions.

## Getting Started
1. Clone or download this repo as a zip file
2. Select either the full or simple directories (see below for an explanation of the differences)
3. Update the lambda_function.py file with your Wordsmith credentials
4. If you selected the full template, update remaining custom variables with your information (these are generally denoted by a tag that looks like `<YOUR INFORMATION HERE>`)
5. Create a zip of lambda_function.py and the wordsmith_basic folder and upload it to the Lambda console

## Templates
### Simple
If this is the first time you are developing an Alexa skill, this may be an easier starting point. This template is meant to build a text response from Wordsmith. There is no functionality to support reprompting, sending cards to the Alexa mobile app, requesting help, etc. This is meant _only_ to generate text and send back to Alexa.

### Full
The full template is meant to help enable advanced functionality such as reprompt text, sending cards to the Alexa mobile app, etc. This is not necessary to interact with Alexa but can create a more robust user experience.

## Wordsmith Basic
Included with these templates is a `wordsmith_basic` library. Wordsmith has a full Python SDK available for install using `pip install wordsmith`. However, the full SDK has additional dependencies that may make it challenging to load to a Lambda. To help work around this, the Wordsmith Basic library allows you to generate narrative for a single row of data without any additional dependencies. The library will work with Python 2 or 3, but keep in mind that AWS Lambda only allows Python 2.7.
