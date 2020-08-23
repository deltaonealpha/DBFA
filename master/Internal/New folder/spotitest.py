def foo(word):
    if len(word) == 1:
        return [word.lower(), word.upper()]

    return [f"{j}{i}" for j in foo(word[0]) for i in foo(word[1:])]


s = "prev"
print(foo(s))

s = "pause"
print(foo(s))

s = "next"
print(foo(s))


'''
import spotilib
#spotilib.next() 
from SwSpotify import spotify

print("Currently playing:\n", spotify.current()[0])
print(spotify.current()[1])

'''