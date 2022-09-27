def is_substring(str1, str2):
    for i in range((len(str1)-len(str2))+1):
        aux = 0
        for l2 in str2:
            l1 = str1[i+aux]
            if l2 == str1[i+aux]:
                aux += 1
        if len(str2) == aux:
            return True

    return False
