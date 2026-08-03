# Search Jobs Microservice

## Description

The Search Jobs Microservice is part of the Job Application Tracker project. It allows the main program to search existing job applications based on a specified attribute. 
The microservice performs a case-insensitive search and returns all matching job applications in JSON format.

The microservice supports searching by the following attributes:

- `company`
- `title`
- `status`

The service is implemented using Python and Flask.

---

# Communication Contract:
### Base URL: http://127.0.0.1:4000
### Endpoint: /search
### Method: POST
```
 
```
## How to Programmatically Request Data
The Job Application Tracker sends a POST request to this microservice whenever the user wants to search for an application.

The request is sent to the endpoint:
```
POST http://127.0.0.1:4000/search
```
The request must include a JSON object with three pieces of information:

- `search_key` – the field to search by. It can be `company`, `title`, or `status`.
- `search_value` – the value the user wants to search for. The search is not case-sensitive, so "Google" and "google" produce the same results.
- `search_data` – the list of job applications that the microservice will search through.


### Example Request

```json
{
    "search_key": "company",
    "search_value": "google",
    "search_data": [
        {
            "company": "Google",
            "title": "Software Engineer Intern",
            "date": "07/13/2026",
            "status": "Applied"
        },
        {
            "company": "Microsoft",
            "title": "Software Engineer",
            "date": "07/10/2026",
            "status": "Interviewing"
        }
    ]
}
```
The following Python code shows how another program can make this request:
### Example Python Request

```python
import requests

# Call the Microservice Job Search
def main():
    job_data = [
        {
            "company": "Google",
            "title": "Software Engineer Intern",
            "date": "07/13/2026",
            "status": "Applied"
        },
        {
            "company": "Microsoft",
            "title": "Data Analyst Intern",
            "date": "07/13/2026",
            "status": "Interviewing"
        },
        {
            "company": "Amazon",
            "title": "Backend Developer",
            "date": "07/13/2026",
            "status": "Offer"
        }
    ]
    value = input("Please enter name of a company: ")
    response = requests.post(
        url="http://127.0.0.1:4000/search",
        json={
            "search_key": "company",
            "search_value": value,
            "search_data": job_data
        }
    )

```

---

## How to Programmatically Receive Data

When matching job applications are found, the microservice returns HTTP status code **200** and a JSON array containing each matching application.

### Example Response

```json
[
    {
        "index": 1,
        "job_app": {
            "company": "Google",
            "title": "Software Engineer Intern",
            "date": "07/13/2026",
            "status": "Applied"
        }
    }
]
```

### Example Python Code to Receive the Response

```python
    response = requests.post(
        url="http://127.0.0.1:4000/search",
        json={
            "search_key": "company",
            "search_value": value,
            "search_data": job_data
        }
    )
    if response.status_code != 200:
        print (response.json().get("error"))
    print (response.json())
```

---

## Error Responses

### Invalid Request

If one or more required fields are missing or empty, the microservice returns:

Status Code

```
400 Bad Request
```

Response

```json
{
    "error": "Invalid Search!"
}
```

### No Matching Results

If no job applications match the search criteria, the microservice returns:

Status Code

```
404 Not Found
```

Response

```json
{
    "error": "Not Found"
}
```

---

# UML Sequence Diagram



---



