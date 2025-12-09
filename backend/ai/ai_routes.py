from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

ai_bp = Blueprint('ai_bp', __name__)

personal_info = {
    "name": "Ishita Sharma",
    "role": "Full Stack Developer & AI Enthusiast",
    "skills": ["Python", "Flask", "PostgreSQL", "HTML", "CSS", "JavaScript", "AI projects"],
    "projects": ["AI Portfolio Website", "Chat Application", "Resume Analyzer"],
    "education": "B.Tech in Computer Science",
    "experience": "Internships at XYZ Tech",
    "about": "I am passionate about building AI-powered web applications and interactive portfolios."
}

faq_responses = {
    "who are you": f"I am {personal_info['name']}, a {personal_info['role']}.",
    "what are your skills": f"My key skills are: {', '.join(personal_info['skills'])}.",
    "tell me about your projects": f"My projects include: {', '.join(personal_info['projects'])}.",
    "education": f"My education: {personal_info['education']}.",
    "experience": f"My experience: {personal_info['experience']}.",
    "about": f"{personal_info['about']}"
}

@ai_bp.route('/chat', methods=['POST', 'OPTIONS'])
@cross_origin()
def chat():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200  # Preflight for CORS

    data = request.get_json()
    user_question = data.get("message", "").lower()  # must match React key

    response = "I'm sorry, I don't understand. Can you ask differently?"
    for key, answer in faq_responses.items():
        if key in user_question:
            response = answer
            break

    return jsonify({
        "user_question": user_question,
        "ai_reply": response
    }), 200
