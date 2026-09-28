from app import create_app, db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    
    
    
    
    
    
    from app.auth import auth_bp
        app.register_blueprint(auth_bp)
    