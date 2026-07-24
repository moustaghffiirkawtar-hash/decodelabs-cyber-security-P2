def cypherchar(c):
    shift =4
    cychar=chr((ord(c)-65+shift)%26+65)
    return cychar
def cyphertext(text):
    cytext=""
    for c in text :
        cytext=cypherchar(c)+cytext
    return cytext
def decypherchar(c):
    shift =4
    cychar=chr((ord(c)+65-shift)%26+65)
    return cychar
def decyphertext(text):
    decytext=""
    for c in text :
        decytext=decytext+decypherchar(c)
    return decytext
print(cyphertext("han jisung"))
print(decyphertext(("han jisung")))
