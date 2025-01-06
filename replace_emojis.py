import re
import emoji
from emoji import EMOJI_DATA

def replace_with_emoji(sentence):
    # Define regex pattern to extract tokens (letters, hyphens, and underscores)
    pattern = r'\b[A-Za-z_-]+\b'  # Match whole words (using word boundaries)
    
    # Find all tokens in the sentence (case-insensitive) and store them as lowercase
    tokens = set(re.findall(pattern, sentence.lower()))  # Use set for unique tokens, case-insensitive
    #Toggle print statement for debugging
    print("Tokens:", tokens)

    emoji_sentence = sentence
    for token in tokens:
        
        match = ''
        
        # Find emoji matching according to ideal order of match cases
        for emoji_char, data in EMOJI_DATA.items():
  
            if token == data.get("en", "").strip(':'): # Exact match
                match = data.get("en", "")
            elif token.startswith(data.get("en", "").strip(':')): # Starts with match
                match = data.get("en", "")
            elif any(token == alias.strip(':') for alias in data.get("alias", [])): # Alias match
                match = next((alias for alias in data.get("alias", []) if token == alias.strip(':')), None)
            
            if match:
                sub = re.sub(rf'{match.strip(":")}',rf'{match}',token)
                #Toggle print statement for debugging
                print(f"Emoji Found: {emoji_char}, Token: {token}, Match: {match}, Sub: {sub}")
                
                # Replace token with emoji using re.sub with case insensitivity
                emoji_sentence = re.sub(rf'\b{token}\b', sub, emoji_sentence, flags=re.IGNORECASE)
                emoji_sentence = emoji.emojize(emoji_sentence, language='alias')
                break  # No need to search further for this token
    
    # Convert the shortcodes to actual emojis using emoji.emojize with language='alias'
    return emoji_sentence

if __name__=='__main__':
    # Example sentence
    sentence = "I love Pizza pizza, cats, bobcats, ants, pigs, croissants, and bread thumbs_up thumbsup PIzzaaaa re-Pizzaaaaa!"

    # Get the emoji-replaced sentence
    emoji_sentence = replace_with_emoji(sentence)

    # Print the result
    print(sentence)
    print(emoji_sentence)