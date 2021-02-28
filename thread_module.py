import threading

def thread_module(list_of_ip, function):
	threads = []

	for ip in list_of_ip:
		a = threading.Thread(target = function, args = (ip,))
		a.start()
		threads.append(a)

	for a in threads:
		a.join()