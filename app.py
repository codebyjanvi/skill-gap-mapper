from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined skill requirements for careers
CAREER_SKILLS = {
    "Data Scientist": ["Python", "Machine Learning", "Statistics", "Data Analysis", "SQL", "Data Visualization"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Flask", "Node.js"],
    "Cybersecurity Analyst": ["Networking", "Linux", "Python", "Penetration Testing", "Firewalls", "Risk Assessment"],
    "Product Manager": ["Project Management", "Communication", "Roadmapping", "Stakeholder Management", "Agile", "Analytics"],
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Mathematics"]
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        user_skills = request.form.get("skills", "").split(",")
        user_skills = [skill.strip().title() for skill in user_skills]
        career_goal = request.form.get("career")

        required_skills = CAREER_SKILLS.get(career_goal, [])
        missing_skills = [skill for skill in required_skills if skill not in user_skills]

        result = {
            "career": career_goal,
            "current_skills": user_skills,
            "missing_skills": missing_skills,
            "recommendation": "You should focus on learning: " + ", ".join(missing_skills) if missing_skills else "You already have the required skills!"
        }

    return render_template("index.html", careers=list(CAREER_SKILLS.keys()), result=result)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined skill requirements for careers
CAREER_SKILLS = {
    "Data Scientist": ["Python", "Machine Learning", "Statistics", "Data Analysis", "SQL", "Data Visualization"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Flask", "Node.js"],
    "Cybersecurity Analyst": ["Networking", "Linux", "Python", "Penetration Testing", "Firewalls", "Risk Assessment"],
    "Product Manager": ["Project Management", "Communication", "Roadmapping", "Stakeholder Management", "Agile", "Analytics"],
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Mathematics"]
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        user_skills = request.form.get("skills", "").split(",")
        user_skills = [skill.strip().title() for skill in user_skills]
        career_goal = request.form.get("career")

        required_skills = CAREER_SKILLS.get(career_goal, [])
        missing_skills = [skill for skill in required_skills if skill not in user_skills]

        result = {
            "career": career_goal,
            "current_skills": user_skills,
            "missing_skills": missing_skills,
            "recommendation": "You should focus on learning: " + ", ".join(missing_skills) if missing_skills else "You already have the required skills!"
        }

    return render_template("index.html", careers=list(CAREER_SKILLS.keys()), result=result)

if __name__ == "__main__":
    app.run(debug=True)
