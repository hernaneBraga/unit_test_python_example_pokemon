import pytest
from pokemon import *

error_msg_on_get_pokemon = 'Failed to retrieve data'
same_height_msg = 'Both Pokémon have the same height'


def test_get_pokemon_by_id():
    assert get_pokemon(1) != error_msg_on_get_pokemon


def test_get_pokemon_by_name():
    assert get_pokemon('pikachu') != error_msg_on_get_pokemon


@pytest.mark.parametrize("wrong_name,msg", [("pikaachu", error_msg_on_get_pokemon),
                                            ("-50", error_msg_on_get_pokemon),
                                            ("Agumon", error_msg_on_get_pokemon),
                                            ("Metal Skull Graymon", error_msg_on_get_pokemon)
                                            ])
def test_error_on_get_pokemon_by_name(wrong_name, msg):
    assert get_pokemon('gaemon') == 'Failed to retrieve data'


@pytest.mark.parametrize("poke1,poke2,result", [
                                            (get_pokemon('pikachu'), get_pokemon('charmander'), 'charmander'),
                                            (get_pokemon('charizard'), get_pokemon('charmander'), 'charizard'),
                                            (get_pokemon('pikachu'), get_pokemon('pikachu'), same_height_msg),
                                            ])
def test_pokemon_height(poke1,poke2,result):
    assert compare_pokemons_height(poke1, poke2) == result
