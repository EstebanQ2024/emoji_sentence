To use, only one function needs to be imported:

**from replace_emojis import replace_with_emoji**

    """
    Replaces words in a sentence with corresponding emojis if available.

    Args:
        sentence (str): The input sentence to process.
        debug (bool): Flag to toggle debug print statements. Default is False.

    Returns:
        str: The sentence with words replaced by emojis where applicable.
    """

Emoji data is taken from the EMOJI_DATA dictionary of the emoji library.

Three match cases are used:
- Exact match of a word to emoji 'EN' language description
- Emoji 'EN' description matches the beggining of a word
- Exact match of a word with emoji 'alias'

Example:

I love omnipotent a Pizza pizza, cats, bobcats, ants, pigs, croissants, and bread thumbs_up thumbsup PIzzaaaa re-Pizzaaaaa!

I love 🕉️nipotent 🅰️ 🍕 🍕, 🐱s, bobcats, 🐜s, 🐷s, 🥐s, and 🍞 👍 👍 🍕aaa re-Pizzaaaaa!


--

**For additional debugging print statements:**

Setting keyword arg debug=True will output information about the words (tokens) extracted from the text, and the emoji matches and substitutions.

Example:

Tokens: {'re-pizzaaaaa', 'bobcats', 'a', 'i', 'love', 'thumbs_up', 'croissants', 'omnipotent', 'cats', 'ants', 'pigs', 'bread', 'pizzaaaa', 'pizza', 'thumbsup', 'and'}

Emoji Found: 🅰️, Token: a, Match: :a:, Sub: :a:

Emoji Found: 👍, Token: thumbs_up, Match: :thumbs_up:, Sub: :thumbs_up:

Emoji Found: 🥐, Token: croissants, Match: :croissant:, Sub: :croissant:s

Emoji Found: 🕉️, Token: omnipotent, Match: :om:, Sub: :om:nipotent

Emoji Found: 🐈, Token: cats, Match: :cat:, Sub: :cat:s

Emoji Found: 🐜, Token: ants, Match: :ant:, Sub: :ant:s

Emoji Found: 🐖, Token: pigs, Match: :pig:, Sub: :pig:s

Emoji Found: 🍞, Token: bread, Match: :bread:, Sub: :bread:

Emoji Found: 🍕, Token: pizzaaaa, Match: :pizza:, Sub: :pizza:aaa

Emoji Found: 🍕, Token: pizza, Match: :pizza:, Sub: :pizza:

Emoji Found: 👍, Token: thumbsup, Match: :thumbsup:, Sub: :thumbsup:

I love omnipotent a Pizza pizza, cats, bobcats, ants, pigs, croissants, and bread thumbs_up thumbsup PIzzaaaa re-Pizzaaaaa!

I love 🕉️nipotent 🅰️ 🍕 🍕, 🐱s, bobcats, 🐜s, 🐷s, 🥐s, and 🍞 👍 👍 🍕aaa re-Pizzaaaaa!
