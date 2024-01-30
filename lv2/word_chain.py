def solution(n, words):
    memory=set()
    last_char = words[0][0]
    
    for i,word in enumerate(words):
        if word in memory or word[0] != last_char:
            return [(i%n)+1,(i//n)+1]
        
        last_char=word[-1]
        memory.add(word)
    
    return [0,0]