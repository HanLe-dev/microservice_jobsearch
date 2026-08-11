# Ho Gia Han Le and Anton Choo
# Microservice Job Search

from flask import Flask, request, jsonify
app = Flask(__name__)

# Search for job apps from job_data
def search_jobs(key, value, data):
    results = []
    for i, job in enumerate(data):
        if value.lower() in job.get(key).lower():
            results.append(
                {
                    "index": i + 1,
                    "job_app": job
                }
            )
    return results


# The server.
@app.route("/search", methods=["POST"])
def search():
    print("Microservice Job Search is running...")
    request_body = request.get_json()
    search_key = request_body.get("search_key").lower().strip()
    search_value = request_body.get("search_value").lower().strip()
    search_data = request_body.get("search_data")
    if not search_key or not search_value or not search_data:
        return jsonify({"error": "Invalid Search!"}), 400
    print("Data received! Responding...")
    response = search_jobs(search_key, search_value, search_data)
    if not response:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(port=4000)
