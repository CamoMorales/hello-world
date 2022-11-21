Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> words = ["231", "20", "-45", "99"]
>>> map(int, words)
<map object at 0x0000021D95537010>
>>> words
['231', '20', '-45', '99']
>>> words = list(map(int, words))
>>> words
[231, 20, -45, 99]
