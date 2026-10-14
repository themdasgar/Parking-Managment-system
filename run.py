from app import create_app, db


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    
    
    
    
    
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
