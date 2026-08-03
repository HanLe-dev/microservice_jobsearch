# Ho Gia Han Le


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
    if response.status_code != 200:
        print (response.json().get("error"))
    print (response.json())

if __name__ == "__main__":
    main()