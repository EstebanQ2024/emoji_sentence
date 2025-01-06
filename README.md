To use, only one function needs to be imported:

from replace_emojis import replace_with_emoji

    """
    Replaces words in a sentence with corresponding emojis if available.

    Args:
        sentence (str): The input sentence to process.
        debug (bool): Flag to toggle debug print statements. Default is False.

    Returns:
        str: The sentence with words replaced by emojis where applicable.
    """

Three match cases are used:
- Exact match of a word to emoji 'EN' language description
- Emoji 'EN' description matches the beggining of a word
- Exact match of a word with emoji 'alias'

Emoji data is from the EMOJI_DATA dictionary of the emoji library-

Example:

I love omnipotent a Pizza pizza, cats, bobcats, ants, pigs, croissants, and bread thumbs_up thumbsup PIzzaaaa re-Pizzaaaaa!

I love 🕉️nipotent 🅰️ 🍕 🍕, 🐱s, bobcats, 🐜s, 🐷s, 🥐s, and 🍞 👍 👍 🍕aaa re-Pizzaaaaa!
