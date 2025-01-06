    """
    Replaces words in a sentence with corresponding emojis if available.

    Args:
        sentence (str): The input sentence to process.
        debug (bool): Flag to toggle debug print statements. Default is False.

    Returns:
        str: The sentence with words replaced by emojis where applicable.
    """

Three match cases are used:
- Word exact match to emoji in 'EN' language
- Emoji 'EN' description matchs the beggining of a word
- Exact match of word with emoji 'alias'

Emoji data is from the EMOJI_DATA dictionary of the emoji library-

Example:

I love omnipotent a Pizza pizza, cats, bobcats, ants, pigs, croissants, and bread thumbs_up thumbsup PIzzaaaa re-Pizzaaaaa!

I love 🕉️nipotent 🅰️ 🍕 🍕, 🐱s, bobcats, 🐜s, 🐷s, 🥐s, and 🍞 👍 👍 🍕aaa re-Pizzaaaaa!
