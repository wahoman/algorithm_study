def solution(k, dungeons):
    def explore(k,dungeons):
        max_dungeons=0
        for i, dungeon in enumerate(dungeons):
            if k>=dungeon[0]:
                remaining_dungeons = dungeons[:i] + dungeons[i+1:]
                max_dungeons=max(max_dungeons, 1+explore(k-dungeon[1], remaining_dungeons))
        return max_dungeons
    
    return explore(k,dungeons)
                                