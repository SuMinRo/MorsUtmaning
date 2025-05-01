"""
Denna fil innehåller kompletterande förbättringar som Filip inte hade tänkt på behövdes sedan innan.
Varje segment är separerade med en rad av bindessträck. Kopiera in så som det passar i den aktuella huvudfilen.
"""

#----------------------------------------------------------------------------------------------------------------
"""
Det är tämligen jobbigt att göra en 'reverse look-up' i en Dictionary. Här kommer en rad för att göra en reverserad Dictionary, så att du kan använda den baklänges.
Se bara till att denna rad hamnar *efter* där 'characterDictionary' definieras, annars kommer programmet inte veta *vad* det är som ska reverseras, och det genererar ett fel.

Du behöver inte begripa vad den gör, annat än istället för 'dict[bokstav] = värde', så gör den 'reverseDict[värde] = bokstav'.
T.ex. characterDictionary['A'] = 0 innebär reverseCharacterDictionary[0] = 'A'
"""

reverseCharacterDictionary  = {v: k for k, v in characterDictionary.items()}

#----------------------------------------------------------------------------------------------------------------
