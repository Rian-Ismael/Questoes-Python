def scroll(m):
    if len(m) >= 1:

        for i in range(len(m)):
            m[len(m)-i-1] = m[len(m)-i]

    return m

m = [[  1,  2,  3,  4 ],
     [  5,  6,  7,  8 ],
     [  9, 10, 11, 12 ],
     [ 13, 14, 15, 16 ],
     [ 17, 18, 19, 20 ]]

print(scroll(m))
