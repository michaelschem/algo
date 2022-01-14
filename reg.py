regex_integer_in_range = r"[1-9]\d{4}"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?<=\1)" # Do not delete 'r'.

import re
P = "110000"
P = "552523"

print(re.findall(regex_alternating_repetitive_digit_pair, P))

print(bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)