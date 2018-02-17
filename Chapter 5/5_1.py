import time

def get_time():
	t = time.time() + (60 * 60 * 9)
	hour = ((t % (60 * 60 * 24)) // (60 * 60))
	minute = ((t % (60 * 60 * 24)) % (60 * 60)) // 60
	second = ((t % (60 * 60 * 24)) % (60 * 60)) % 60
	print(round(hour), '시', round(minute), '분', round(second), '초')

def get_days():
	t = time.time() + (60 * 60 * 9)
	days = t // (60 * 60 * 24)
	print(round(days), '일')

get_time()
get_days()
