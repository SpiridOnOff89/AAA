class ChangeStrMixin:
    def __str__(self):
        return self.to_str()


class EmojiMixin:
    emoji_category_dict = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡'
    }

    def __str__(self):
        return f'{self.name}/{self.emoji_category_dict[self.poketype]}'


class Pokemon(EmojiMixin):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def to_str(self):
        return f'{self.name}/{self.poketype}'


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)
