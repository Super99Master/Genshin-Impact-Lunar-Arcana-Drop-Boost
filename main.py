from pathlib import Path
from read_log import read_log
from calculate_probability import calculate, print_result

data = read_log("/mnt/P/Rayax/Public/Genshin Lunar Arcana/Teather S16.log")

result = calculate(data.get_all())
print_result(result)

for character in data:
    print(character, end=" ")
    print_result(calculate(data[character]))