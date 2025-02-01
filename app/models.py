# Database models (SQLAlchemy) 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Candidate(db.Model):
    __tablename__ = 'candidates'
    candidate_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_info = db.Column(db.String(255))
    skills = db.Column(db.Text)
    qualifications = db.Column(db.Text)
    experience = db.Column(db.Text)

class JobListing(db.Model):
    __tablename__ = 'job_listings'
    job_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    job_description = db.Column(db.Text)
    required_skills = db.Column(db.Text)
    salary = db.Column(db.String(50))
    status = db.Column(db.Enum('Open', 'Closed'), default='Open')

class TrainingProgram(db.Model):
    __tablename__ = 'training_programs'
    program_id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    skills_covered = db.Column(db.Text)
    institution_partnered = db.Column(db.String(255))

class AssessmentTest(db.Model):
    __tablename__ = 'assessment_tests'
    test_id = db.Column(db.Integer, primary_key=True)
    skill_area = db.Column(db.String(255), nullable=False)
    test_description = db.Column(db.Text)
    performance_metrics = db.Column(db.Text)

class Application(db.Model):
    __tablename__ = 'applications'
    application_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job_listings.job_id'), nullable=False)
    status = db.Column(db.Enum('Pending', 'Accepted', 'Rejected'), default='Pending')

    candidate = db.relationship('Candidate', backref=db.backref('applications', lazy=True))
    job = db.relationship('JobListing', backref=db.backref('applications', lazy=True))
