import time,os
def test():
	i=0
	while i<10:
		os.system('echo %s >> /tmp/a.log' %i)
		time.sleep(1)
		i+=1
