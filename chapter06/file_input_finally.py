try:
    f = open('file_not_found_exception', 'w')
    f.read()
except IOError as ioe:
    print('ファイルが見つかりませんでした')
finally:
    f.close()
