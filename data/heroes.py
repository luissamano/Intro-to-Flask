import json

class Heroe(object):
    heroes = [
    {
        "superhero":"Spider Man", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Peter Parker",
        "characters":"Peter Parker"
    },
    {
        "superhero":"Captain America", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Steve Rogers",
        "characters":"Steve Rogers"
    },
    {
        "superhero":"Iron Man", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Tony Stark",
        "characters":"Tony Stark"
    },
    ]

    @classmethod
    def get_all(self):
        return self.heroes