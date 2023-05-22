if __name__ == '__main__':
    text = 'This is a very long sentence.'
    
    info = {
        'words': (words := text.split()),
        'characters': (chars := len(''.join(words))),
        'avg_char_per_word': round(chars / len(words), 2)
    }
    
    print(info)
    
    name = 'Mario'
    empty_name = ''
    
    if temp_name := empty_name or name:
        print(temp_name)