# API routes 
from flask import request, jsonify
from flask_restful import Resource
from models import db, Candidate, JobListing, TrainingProgram, AssessmentTest, Application

def initialize_routes(api):
    api.add_resource(CandidateResource, '/candidates')
    api.add_resource(JobListingResource, '/job_listings')
    api.add_resource(TrainingProgramResource, '/training_programs')
    api.add_resource(AssessmentTestResource, '/assessment_tests')
    api.add_resource(ApplicationResource, '/applications')

class CandidateResource(Resource):
    def get(self):
        candidates = Candidate.query.all()
        return jsonify([{'id': c.candidate_id, 'name': c.name, 'skills': c.skills} for c in candidates])

    def post(self):
        data = request.get_json()
        new_candidate = Candidate(
            name=data['name'],
            contact_info=data.get('contact_info', ''),
            skills=data.get('skills', ''),
            qualifications=data.get('qualifications', ''),
            experience=data.get('experience', '')
        )
        db.session.add(new_candidate)
        db.session.commit()
        return jsonify({'message': 'Candidate added successfully'})

class JobListingResource(Resource):
    def get(self):
        jobs = JobListing.query.all()
        return jsonify([{'id': j.job_id, 'company': j.company_name, 'description': j.job_description} for j in jobs])

    def post(self):
        data = request.get_json()
        new_job = JobListing(
            company_name=data['company_name'],
            job_description=data['job_description'],
            required_skills=data.get('required_skills', ''),
            salary=data.get('salary', ''),
            status='Open'
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify({'message': 'Job listing added successfully'})

class TrainingProgramResource(Resource):
    def get(self):
        programs = TrainingProgram.query.all()
        return jsonify([{'id': p.program_id, 'name': p.program_name, 'skills': p.skills_covered} for p in programs])

    def post(self):
        data = request.get_json()
        new_program = TrainingProgram(
            program_name=data['program_name'],
            description=data.get('description', ''),
            skills_covered=data.get('skills_covered', ''),
            institution_partnered=data.get('institution_partnered', '')
        )
        db.session.add(new_program)
        db.session.commit()
        return jsonify({'message': 'Training program added successfully'})

class AssessmentTestResource(Resource):
    def get(self):
        tests = AssessmentTest.query.all()
        return jsonify([{'id': t.test_id, 'skill_area': t.skill_area, 'description': t.test_description} for t in tests])

    def post(self):
        data = request.get_json()
        new_test = AssessmentTest(
            skill_area=data['skill_area'],
            test_description=data.get('test_description', ''),
            performance_metrics=data.get('performance_metrics', '')
        )
        db.session.add(new_test)
        db.session.commit()
        return jsonify({'message': 'Assessment test added successfully'})

class ApplicationResource(Resource):
    def get(self):
        applications = Application.query.all()
        return jsonify([{'id': a.application_id, 'candidate': a.candidate_id, 'job': a.job_id, 'status': a.status} for a in applications])

    def post(self):
        data = request.get_json()
        new_application = Application(
            candidate_id=data['candidate_id'],
            job_id=data['job_id'],
            status='Pending'
        )
        db.session.add(new_application)
        db.session.commit()
        return jsonify({'message': 'Application submitted successfully'})
