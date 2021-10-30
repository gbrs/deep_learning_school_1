def process(sentences):
    result = []
    for sentence in sentences:
        s = ''
        for word in sentence.split():
            if word.isalpha():
                s = ' '.join((s, word))
        result.append(s.strip())
    return result


a = ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']
b = process(a)
assert b == ['thousand devils', 'My name is', 'Room costs', ''], "Something is wrong! Please try again"
