# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

#Se toma cada elemento del string
#Si es un elemnto de apertura de agrega al stack
#Si es un elemento de cierre, se compara con el último del stack, si coinciden
#Se quita del stack.
#Al final el stack tiene que estar vacio para retornar true, si tiene elementos
#Se retorna false
#Solución válida para LeetCode

class Solution:
    def isValid(self, s: str) -> bool:
        diccionario = {"(":")", "{":"}", "[":"]" }
        tokens = list(s)
        elementosApertura = ('(', '{', '[')
        elementosCierre = (')', '}', ']')
        stack = []
        for token in tokens:
            if token in elementosApertura:
                stack.append(token)
            else:
                if len(stack) >=1:
                    ultimo = stack.pop()
                    temp = diccionario.get(ultimo)
                    if temp != token:
                        return False
                else:
                    return False
        if len(stack) >= 1:
            return False
        return True