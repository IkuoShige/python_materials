# 前回実行時の日付と時刻を表示

import os.path
import pickle
import datetime

CONFIG_FILE = 'config.dat'

previous = None

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'rb') as f:
        previous = pickle.load(f)
        print('前回：', previous)
        pass
else:
    print('本プログラムを実行するのは初めてですね。')

# いろいろな処理

current = datetime.datetime.now()

with open(CONFIG_FILE, 'wb') as f:
    pickle.dump(current, f)
