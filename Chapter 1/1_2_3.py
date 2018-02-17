sec = (42 * 60) + 42
convert = 10 / 1.61
cal = convert / sec

print(sec, 'second') # 42분 42초를 초로 변환
print(convert, 'mile') # 10km를 마일로 변환

print(convert / 42.42, 'mile per minute')
print('Verification :', 0.146421030745488 * 42.42)

print(convert / sec, 'mile per second')
print('Verification :', 0.0024243482139826703 * 2562)
