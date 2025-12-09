from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from database.db import db, get_db_uri
from ai.ai_routes import ai_bp
from ai.resume_routes import resume_bp
from router.comment_bp import comment_bp

app = Flask(__name__)
CORS(app)  # allow all origins; safer to restrict later
app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(ai_bp, url_prefix='/ai')
app.register_blueprint(resume_bp, url_prefix='/ai')
app.register_blueprint(comment_bp, url_prefic="/api")

# Projects model
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    tech_stack = db.Column(db.Text)
    github_url = db.Column(db.String(255))
    live_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Comment Model
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()


# Test route
@app.route("/")
def home():
    return "Welcome to the Portfolio Backend!"

# Get all projects
@app.route("/projects", methods=['GET'])
def get_projects():
    projects = Project.query.all()
    output = []
    for project in projects:
        output.append({
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'tech_stack': project.tech_stack,
            'github_url': project.github_url,
            'live_url': project.live_url,
            'created_at': project.created_at
        })
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
