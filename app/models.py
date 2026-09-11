from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='staff')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Slot(db.Model):
    slot_number = db.Column(db.Integer, primary_key=True)
    is_available = db.Column(db.Boolean, default=True)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(20))
    vehicle_type = db.Column(db.String(20))
    entry_time = db.Column(db.DateTime, default=datetime.now)
    exit_time = db.Column(db.DateTime, nullable=True)
    fee = db.Column(db.Numeric(10,2), nullable=True)
    slot_number = db.Column(db.Integer)
    status = db.Column(db.String(10), default='parked')
    
    @auth_bp.route('/dashboard')
@login_required
def dashboard():
    return "Welcome to Dashboard!"

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))