def solution(text):
    words = text.split(' ')

    new_text = []
    count = 0
    for i in range(len(words)):
        new_text.append(words[i])
        count += 1

        if count == 4:
            count = 0
            new_text.append('\n')
        else:
            new_text.append(' ')

    return ''.join(new_text)


if __name__ == '__main__':
    text = 'Amar é a sabedoria dos loucos e a loucura dos sábios'
    print(solution(text))
