# TASK: Pokemon Interface
import math

from flask import Flask, render_template
import requests


def main():
    """
        Instructions:
        Use the Pokemon API to create a Pokemons flask interface.
        If you have some trouble working with an API look at the Hint below.

        Create a website with the following pages:

            1. Pokemon page (/pokemon/<id>)
                This page displays some information about a pokemon (at least a picture and a name)

            2. By Type (pokemons/bytype/<type>)
                Displays a list of all the pokemons of a given type.

            3. By name (/pokemons/byname/<name>)
                Redirects to the page of this pokemon if it exists, else redirect to the main page.

            4. Main page (/)
                The main page should contain a list of all the pokemons types, each type is clickable and lead to the corresponding bytype page.

            5. All pokemons (/pokemons/all) This page displays a list of all the existing pokemons, this list is a
                bit too large, try to add a pagination feature so that you only display 20 pokemons by page (Hint: play
                with the limit and offset parameters).

        Notes : All the pokemons in the /pokemons/bytype, /pokemons/all and / should be displayed as frames that
            contains a picture of the pokemon and his name. When clicked, this frame leads to the pokemon’s page.

        Good luck.
        Make it pretty!


        Hint:
            If you struggle with the API:
            Every endpoint can be used in two ways, for example:
                - the /pokemon/ can be used to retrieve a list of all the pokemons if nothing comes after the second /
                - the /pokemon/ can be used to retrieve a specific pokemon by specifying its id or its name after the second /, for example: /pokemon/1 (by id) or /pokemon/ditto (by name)

    """
    count = requests.get("https://pokeapi.co/api/v2/pokemon").json()["count"]

    app = Flask(__name__)

    @app.route('/')
    @app.route('/pokemon/<int:page>')
    def pokemon(page=0, limit=20, offset=20):
        ceil = math.floor(count / limit)
        if page > ceil:
            page = ceil
        offset = page * offset
        pokemon_list = requests.get(f"https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit=20").json()["results"]
        for pokemon in pokemon_list:
            info = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon["name"]}').json()
            pokemon.update({
                "pokemon_img": info['sprites']['front_default'],
                "pokemon_id": info["id"],
                "pokemon_types": [pokemon_types["type"]["name"] for pokemon_types in info["types"]]
            })
        return render_template('pokemon.html', page=page, limit=limit, offset=offset, pokemon_list=pokemon_list, ceil=ceil)

    @app.route('/pokemon/byid/<int:pokemon_id>')
    def byid(pokemon_id=0):
        pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}').json()
        pokemon.update({
            "img": pokemon['sprites']['front_default'],
            "name": pokemon["name"],
            "id": pokemon["id"],
            "types": [pokemon_types["type"]["name"] for pokemon_types in pokemon["types"]]
        })
        return render_template('pokemon_id.html', pokemon_id=pokemon_id, pokemon=pokemon)

    @app.route('/pokemon/bytype')
    @app.route('/pokemon/bytype/<pokemon_type>')
    def bytype(pokemon_type="normal"):
        pokemon_of_type = requests.get(f'https://pokeapi.co/api/v2/type/{pokemon_type}').json()["pokemon"]
        for pokemon in pokemon_of_type["pokemon"]:
            info = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon["name"]}').json()
            pokemon.update({
                "pokemon_img": info['sprites']['front_default'],
                "pokemon_id": info["id"],
                "pokemon_types": [pokemon_types["type"]["name"] for pokemon_types in info["types"]]
            })
        return render_template('bytype.html', pokemon_type=pokemon_type, pokemon_of_type=pokemon_of_type)

    @app.route('/pokemon/byname')
    @app.route('/pokemon/byname/<pokemon_name>')
    def byname(pokemon_name=""):
        return render_template('byname.html', pokemon_name=pokemon_name)

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
