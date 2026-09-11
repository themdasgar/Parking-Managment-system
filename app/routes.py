body {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
