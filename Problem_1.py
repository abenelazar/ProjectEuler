def skipped_sum(n, p):
	instances = p/n
	return n*instances*(instances+1)/2

print skipped_sum(3, 999) + skipped_sum(5, 999) - skipped_sum(15, 999)