from flask import render_template, request, redirect, url_for, flash
from models import db, Game # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        # This route should retrieve all items from the database and display them on the page.
        games=Game.query.all()
        return render_template('index.html', games= games)
    
    @app.route('/add', methods=['POST'])
    def add_item():
        new_game = Game(
            title=request.form['title'],
            developer=request.form['developer'],
            publisher=request.form['publisher'],
            release=request.form['release'],
            genre=request.form['genre'],
            description=request.form['description']
            #add img later
        )
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for('get_items'))
        #return render_template('index.html', message=f'Item added successfully')

    @app.route('/update', methods=['POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')