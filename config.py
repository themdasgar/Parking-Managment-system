class Config:
    SECRET_KEY = 'mera-secret-key-Asgar@802219'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:TUMHARA_PASSWORD@localhost/parking_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
  from app.auth import auth_bp
      app.register_blueprint(auth_bp)
    