def get_score_state():
    our_score = 0
    enemy_score = 1
    return our_score, enemy_score

def _get_score_state():
    return get_score_state()

score = _get_score_state()
print(score[0])
print(score[1])
