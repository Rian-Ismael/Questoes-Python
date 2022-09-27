def is_substring(str1, str2):
    for i in range((len(str1)-len(str2))+1):
        aux = 0
        for l2 in str2:
            if l2 == str1[i+aux]:
                aux += 1
        if len(str2) == aux:
            return True

    return False


assert is_substring('boiada','oi')
assert not is_substring('casorio', 'casa')
