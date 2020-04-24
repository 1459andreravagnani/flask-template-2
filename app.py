from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    pokemons = [
        ['Bulbasaur', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png'],
        ['Charmander', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png'],
        ['Squirtle', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png'],
        ['Pikachu', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png']
    ]
    return render_template(
        'index.html',
        titulo='Pokedex',
        pokemons=pokemons
    )
 
if __name__ == '__main__':
    app.run()