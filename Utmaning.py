characterDictionary = {'A' : 0,
                       'a' : 1,
                       'B' : 2,
                       'b' : 3,
                       'C' : 4,
                       'c' : 5,
                       'D' : 6,
                       'd' : 7,
                       'E' : 8,
                       'e' : 9,
                       'F' : 10,
                       'f' : 11,
                       'G' : 12,
                       'g' : 13,
                       'H' : 14,
                       'h' : 15,
                       'I' : 16,
                       'i' : 17,
                       'J' : 18,
                       'j' : 19,
                       'K' : 20,
                       'k' : 21,
                       'L' : 22,
                       'l' : 23,
                       'M' : 24,
                       'm' : 25,
                       'N' : 26,
                       'n' : 27,
                       'O' : 28,
                       'o' : 29,
                       'P' : 30,
                       'p' : 31,
                       'Q' : 32,
                       'q' : 33,
                       'R' : 34,
                       'r' : 35,
                       'S' : 36,
                       's' : 37,
                       'T' : 38,
                       't' : 39,
                       'U' : 40,
                       'u' : 41,
                       'V' : 42,
                       'v' : 43,
                       'W' : 44,
                       'w' : 45,
                       'X' : 46,
                       'x' : 47,
                       'Y' : 48,
                       'y' : 49,
                       'Z' : 50,
                       'z' : 51,
                       'Å' : 52,
                       'å' : 53,
                       'Ä' : 54,
                       'ä' : 55,
                       'Ö' : 56,
                       'ö' : 57,
                       ' ' : 58,
                       '.' : 59,
                       '!' : 60,
                       '?' : 61,
                       ',' : 62,
                       ':' : 63,
                       ';' : 64,
                       '-' : 65}

reverseCharacterDictionary  = {v: k for k, v in characterDictionary.items()}

encodedMessage = "17333132 2053318 11252068 1115241 7315111 3953260 17942971 16830916 16845253 2267853 16836799 16847227 5143591 8455603 " \
"4904353 7767233 10852315 7316224 7890160 11347979 10311436 11382352 10311568 2621785 10767543 4989451 10890079 4989451 16934359 6291228 " \ 
"2698043 11220563 16404207 16680413 16705879 10122513 4904329 10102049 16439078 11220563 4921791 11392363 16681443 10799125 7881184 6844275 " \ 
"12331397 12617287 4989457 2604373 10190326 16785640 2113785 2757439 6617921 16950987 731940 17128594"

# Transformerar ett meddelande i sin helhet till numerisk kod utifrån icke-överlappande quadgram (sekvens av 4 tecken).
def encodeMessage(message):
    encodedMessage = ""
    quadgrams = generateQuadgrams(message)
    for quadgram in quadgrams:
        encodedMessage += encodeQuadgram(quadgram) + " "
    return encodedMessage[:-1]

# Delar upp ett meddelande till individuella, icke-överlappande quadgram.
def generateQuadgrams(message):
    padding = (4 - len(message) % 4) % 4
    message += ' ' * padding

    quadgrams = []
    for i in range(int(len(message)/4)):
        quadgrams.append(message[4*i : 4*(i+1)])
    return quadgrams

# Transformerar ett enskilt quadgram till en numerisk motsvarighet.
def encodeQuadgram(quadgram):
    num = 0
    for i in range(4):
        num += characterDictionary[quadgram[i]] * pow(66, i)
    return str(num)

# Krypterar ett enskilt quadgram till varje teckens egna motsvarighet, enligt ordboken ovan. OBS! Används bara för att försöka säkerställa korrekthet – den har ingen del av kodningen av ett meddelande.
def encryptQuadgram(quadgram):
    s = ""
    for i in range(4):
        s += str(characterDictionary[quadgram[i]]) + " "
    return s[:-1]

# Nedan kommer ett förslag på kodskelett för att avkoda ett kodat meddelande. Det är fritt fram att definiera nya funktioner eller att ta bort de man inte tycker passar.

# Avkodar ett kodat meddelande i sin helhet till klartext. Den bör reversera 'encodeMessage()' ovan.
def decodeMessage(code):
    cleartext = ""

    # TODO

    return cleartext

# Avkodar ett individuellt kodat quadgram. Den bör reversera 'encodeQuadgram()' ovan.
def decodeQuadgram(number):
    quadgram = ""

    # TODO

    return quadgram

print(encodedMessage)
print(decodeMessage(encodedMessage))
