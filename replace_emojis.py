import re
import emoji
from emoji import EMOJI_DATA

def replace_with_emoji(sentence, debug=False):
    """
    Replaces words in a sentence with corresponding emojis if available.

    Args:
        sentence (str): The input sentence to process.
        debug (bool): Flag to toggle debug print statements. Default is False.

    Returns:
        str: The sentence with words replaced by emojis where applicable.
    """
    # Define regex pattern to extract tokens (letters, hyphens, and underscores)
    pattern = r'\b[A-Za-z_-]+\b'  # Match whole words (using word boundaries)
    
    # Find all tokens in the sentence (case-insensitive) and store them as lowercase
    tokens = set(re.findall(pattern, sentence.lower()))  # Use set for unique tokens, case-insensitive
    if debug:
        print("Tokens:", tokens)

    emoji_sentence = sentence
    for token in tokens:
        match = ''
        
        # Find emoji matching according to ideal order of match cases
        for emoji_char, data in EMOJI_DATA.items():
            # Exact match
            if token == data.get("en", "").strip(':'):
                match = data.get("en", "")
            # Starts with match
            elif token.startswith(data.get("en", "").strip(':')):
                match = data.get("en", "")
            # Alias match
            elif any(token == alias.strip(':') for alias in data.get("alias", [])):
                match = next((alias for alias in data.get("alias", []) if token == alias.strip(':')), None)
            
            if match:
                sub = re.sub(rf'{match.strip(":")}', rf'{match}', token)
                if debug:
                    print(f"Emoji Found: {emoji_char}, Token: {token}, Match: {match}, Sub: {sub}")
                
                # Replace token with emoji using re.sub with case insensitivity
                emoji_sentence = re.sub(rf'\b{token}\b', sub, emoji_sentence, flags=re.IGNORECASE)
                
                # Convert the shortcodes to actual emojis using emoji.emojize with language='alias'
                emoji_sentence = emoji.emojize(emoji_sentence, language='alias')
                
                break  # No need to search EMOJI_DATA further for this token
    
    return emoji_sentence

if __name__ == '__main__':
    # Example sentence
    sentence = "I love Pizza pizza, cats, bobcats, ants, pigs, croissants, and bread thumbs_up thumbsup PIzzaaaa re-Pizzaaaaa!"

    # Get the emoji-replaced sentence
    emoji_sentence = replace_with_emoji(sentence, debug=True)

    # Print the result
    print(sentence)
    print(emoji_sentence)