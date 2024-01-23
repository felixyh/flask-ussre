from app import app

# The following function in microblog.py creates a shell context that adds the database instance and models to the shell session, use 'flask shell'
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
    