import itertools


# maximum number of consecutive download errors allowed
max_errors = 5
# current number of consecutive download errors
num_errors = 0

for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download(url)
    if html is None:
        # received an error trying to download this webpage
        num_errors += 1
        if num_errors == max_errors:
            # reached maximum number of consecutive errors so exit
            break
    else:
        # success - can srape the result
        num_errors = 0