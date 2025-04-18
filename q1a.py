def morse_translate(text, table):
    # Make all letters uppercase
    text = text.upper()
    
    # 
    morse_chars = map(lambda c: table.get(c, ''), text)
    
    # Join Morse characters with line breaks
    return (morse_chars)
#"\n".join(morse_chars)

