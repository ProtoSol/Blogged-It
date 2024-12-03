from bloggedit import db, login_manager, app # We use __main__ to import the database
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    # Relationship between User and Post
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def get_reset_token(self, expires_sec=1800):  # 30 minutes
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})  # No need to decode

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=1800)['user_id']  # Validate expiry time
        except Exception:
            return None
        return User.query.get(user_id)
        
    # We will be using Hashing for image and password
    
    def __repr__(self): # repr is short for representation how the object will be printed
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    
    # Relationship between User and Post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"