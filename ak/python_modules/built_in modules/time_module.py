import time

#localtime

x=time.localtime()
print('year=',x.tm_year)
print('month=',x.tm_mon)

#asctime() : human readable time format

print(time.asctime())

#sleep()

print('hello welcome')
print(time.sleep(2.5))
print('this prints after 2.5 sec')

#strftime()

print(time.strftime('%A'))

print(time.strftime('%a'))

# %A : day (string)
# %a : day (short form)

# %B : month
# %d : date
# %D : complete date
# %Y : year
# %H : hour
# %M : min
# %S : sec
# %m : month( int)

print(time.strftime('%a %H:%S %Y'))

