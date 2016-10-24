f = None
try:
	f = open('file_not_found_exception','r')
except FileNotFoundError as ioe:
	print('ファイルがみつかりませんでした')
finally:
	if f:
		f.close()
