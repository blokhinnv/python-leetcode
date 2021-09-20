# swagger-client
This is a simple API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0-oas3
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
topic = 'topic_example' # str | 

try:
    api_response = api_instance.api_problems_topic_get(topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_problems_topic_get: %s\n" % e)

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.GraphqlQuery() # GraphqlQuery | GraphQL query (optional)

try:
    api_response = api_instance.graphql_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->graphql_post: %s\n" % e)

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
problem = 'problem_example' # str | 
body = swagger_client.TestSubmission() # TestSubmission | Solution to test (optional)

try:
    api_response = api_instance.problems_problem_interpret_solution_post(problem, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->problems_problem_interpret_solution_post: %s\n" % e)

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
problem = 'problem_example' # str | 
body = swagger_client.Submission() # Submission | Solution to test (optional)

try:
    api_response = api_instance.problems_problem_submit_post(problem, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->problems_problem_submit_post: %s\n" % e)

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = swagger_client.Id() # Id | Either submission id (int) or interpretation id (string)

try:
    api_response = api_instance.submissions_detail_id_check_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->submissions_detail_id_check_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://leetcode.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**api_problems_topic_get**](docs/DefaultApi.md#api_problems_topic_get) | **GET** /api/problems/{topic}/ | 
*DefaultApi* | [**graphql_post**](docs/DefaultApi.md#graphql_post) | **POST** /graphql | 
*DefaultApi* | [**problems_problem_interpret_solution_post**](docs/DefaultApi.md#problems_problem_interpret_solution_post) | **POST** /problems/{problem}/interpret_solution/ | 
*DefaultApi* | [**problems_problem_submit_post**](docs/DefaultApi.md#problems_problem_submit_post) | **POST** /problems/{problem}/submit/ | 
*DefaultApi* | [**submissions_detail_id_check_get**](docs/DefaultApi.md#submissions_detail_id_check_get) | **GET** /submissions/detail/{id}/check/ | 

## Documentation For Models

 - [BaseSubmissionResult](docs/BaseSubmissionResult.md)
 - [Difficulty](docs/Difficulty.md)
 - [GraphqlQuery](docs/GraphqlQuery.md)
 - [GraphqlQueryVariables](docs/GraphqlQueryVariables.md)
 - [GraphqlQuestion](docs/GraphqlQuestion.md)
 - [GraphqlQuestionDetail](docs/GraphqlQuestionDetail.md)
 - [GraphqlResponse](docs/GraphqlResponse.md)
 - [Id](docs/Id.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Interpretation](docs/Interpretation.md)
 - [OneOfGraphqlResponseData](docs/OneOfGraphqlResponseData.md)
 - [OneOfid](docs/OneOfid.md)
 - [OneOfinlineResponse200](docs/OneOfinlineResponse200.md)
 - [Problems](docs/Problems.md)
 - [Stat](docs/Stat.md)
 - [StatStatusPair](docs/StatStatusPair.md)
 - [Submission](docs/Submission.md)
 - [SubmissionId](docs/SubmissionId.md)
 - [SubmissionResult](docs/SubmissionResult.md)
 - [TestSubmission](docs/TestSubmission.md)
 - [TestSubmissionResult](docs/TestSubmissionResult.md)

## Documentation For Authorization


## cookieCSRF

- **Type**: API key
- **API key parameter name**: csrftoken
- **Location**: URL query string

## cookieSession

- **Type**: API key
- **API key parameter name**: LEETCODE_SESSION
- **Location**: URL query string

## headerCSRF

- **Type**: API key
- **API key parameter name**: x-csrftoken
- **Location**: HTTP header

## referer

- **Type**: API key
- **API key parameter name**: Referer
- **Location**: HTTP header


## Author

pv.safronov@gmail.com
