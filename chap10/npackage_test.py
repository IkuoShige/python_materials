"""名前空間パッケージのインポート"""

import sys
sys.path.append('dir1')
sys.path.append('dir2')

import npack.abc
import npack.xyz

npack.abc.func()
npack.xyz.func()
