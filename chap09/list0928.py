# アノテーション付きの関数puts

def puts(n: int, s: str) -> None:
    """n個のsを連続して表示"""
    for _ in range(n):
        print(s, end='')

puts(5, '*')
print()
print(puts.__annotations__)
print()
puts('*', 5)
