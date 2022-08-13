# 読み込んだ回数だけ挨拶する（カウントは1から：その２）

n = int(input('挨拶は何回：'))

for i in range(1, n + 1):
    print('No.', i , '：こんにちは。')
