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
            description=request.form['description'],
            img_url=request.form['img_url']
        )
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for('get_items'))
        #return render_template('index.html', message=f'Item added successfully')

    @app.route('/update', methods=['POST'])
    def update():
        id=request.form['id']
        game=Game.query.get(id)
        game.title=request.form['title'],
        game.developer=request.form['developer'],
        game.publisher=request.form['publisher'],
        game.release=request.form['release'],
        game.genre=request.form['genre'],
        game.description=request.form['description'],
        game.img_url=request.form['img_url']
        db.session.commit()
        return redirect(url_for('get_items'))

    @app.route('/edit', methods=['GET'])
    def edit():
        id=request.args.get('id')
        game =Game.query.get(id)
        return render_template('edit.html', game = game)



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')