from flask import Blueprint, request, jsonify
import pdfplumber
import io

resume_bp = Blueprint('resume_bp', __name__)

@resume_bp.route('/analyze-resume', methods=['POST'])
def analyze_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    resume_file = request.files['resume']

    if resume_file.filename == '':
        return jsonify({"error": "Empty file name"}), 400
    
    extracted_text = ""
    with pdfplumber.open(io.BytesIO(resume_file.read())) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text() or ""

    if not extracted_text.strip():
        extracted_text = "Could not extract text. The PDF might be scanned or image-based."
    
    # Now read the PDF resume file
    analysis = {
        "summary": "This is a mock analysis of your resume",
        "skill_match": ["Communication", "Teamwork", "Python"],
        "missing_skills": ["Docker", "CI/CD", "System Design"],
        "recommendations": [
            "Add mesureable achievements.",
            "Include a project section.",
            "Highligh your technical skills in bullet points."
        ],
    }

    return jsonify({
        "resume_text_preview": extracted_text[:500],
        "analysis": analysis
    })