from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  "id": 1,
  "title": "Frontend Developer",
  "location": "Hyderabad, India",
  "salary": "12,00,000"
}, {
  "id": 2,
  "title": "Backend Developer",
  "location": "Hyderabad, India",
  "salary": "10,00,000"
}, {
  "id": 1,
  "title": "App Developer",
  "location": "Delhi, India",
}, {
  "id": 1,
  "title": "Full Stack Developer",
  "location": "Hyderabad, India",
  "salary": "20,00,000"
}]


@app.route("/")
def home():
  return render_template("index.html", jobs=JOBS, header="Jobsite")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
