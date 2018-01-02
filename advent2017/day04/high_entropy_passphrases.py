def is_passphrase_valid(passphrase):
    words = passphrase.replace('\n', '').split(' ')
    words_tested_already = []
    for word in words:
        if word in words_tested_already:
            return False
        words_tested_already.append(word)
    return True


def how_many_passphrases_are_valid(phrases):
    valid_phrases = 0
    for phrase in phrases:
        if is_passphrase_valid(phrase) is True:
            valid_phrases += 1
    return valid_phrases


if __name__ == '__main__':
    phrases = open('passphrases.txt').readlines()
    print(how_many_passphrases_are_valid(phrases))