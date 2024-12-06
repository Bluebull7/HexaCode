def tokenize(script):
    """
    Tokenizes the HexaCode script line by line.
    """
    tokens = []
    for line in script.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):  # Ignore empty lines and comments
            continue
        tokens.append(line.split())
    return tokens

def execute(tokens, print_callback=print):
    """
    Executes tokenized HexaCode commands. Supports a callback for print.
    """
    for token_line in tokens:
        command = token_line[0]
        
        if command == "AFFICHE":
            # Handle AFFICHE (print) command
            content = " ".join(token_line[1:]).strip('"')
            print_callback(content)
        else:
            print_callback(f"Commande inconnue : {command}")
