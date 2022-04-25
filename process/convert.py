import re

######### Helpers ##########

def pad_with_zeros(num):
    """ takes an int and returns a string with zeros prefixed """
    pad = ''
    if num < 10:
        pad = '00'
    elif num < 100:
        pad = '0'
    else:
        pad = ''

    return pad + str(num)

def write_to_psalm(psalm_num, line):
    with open('out/psalm_' + pad_with_zeros(psalm_num), 'a') as out_line:
        out_line.write(line)

def write_tone(psalm_num):
    user_input = raw_input('(tone) >>> ')
    with open('out/psalm_' + pad_with_zeros(psalm_num), 'a') as out_line:
        out_line.write(user_input)
        out_line.write('\n\n')

def parse_line(line):
    print line
    prepend = ''
    while True:
        user_input = raw_input('>>> ')
        if user_input[0:2] == '  ':
            prepend = '  '
            user_input = user_input[2:]
        if user_input == '':
            prepend = prepend_newline(line, prepend)
            return prepend + line
        if user_input in line:
            prepend = prepend_newline(line, prepend)
            re_user_input = re.compile(user_input)
            matches = re_user_input.findall(line)
            if len(matches) == 1:
                break
            elif len(matches) > 1: # edge case in case multiple matches
                print "**********************************************************************"
                print "***************** GOT DUPLICATE MATCHES ON REGEX *********************"
                print "**********************************************************************"
                return '<<<EDIT>>>' + line
    out = line.replace(user_input, '__' + user_input + '__')
    return prepend + out

def prepend_newline(line, prepend):
    re_verse_num = re.compile('^\d+ ')
    matches = re_verse_num.findall(line)
    if matches:
        prepend = '\n' + prepend
    if 'Glory be to the Father, and to the Son,' in line:
        prepend = '\n' + prepend
    return prepend



############## Script #############

place = 0
psalm_num = 1
count = 0
tplace = 0

with open('saved_place', 'r') as f:
    for line in f:
        place = int(line)

with open('psalm_num', 'r') as f:
    for line in f:
        psalm_num = int(line)

print "------------"
print "Psalm: ", psalm_num - 1
print "------------"

try:
    with open('all_psalms', 'r') as f:
        for lnum, line in enumerate(f, 1):
            tplace = lnum
            if lnum < place:
                continue
            elif 'Psalm ' + str(psalm_num) in line:
                print line
                write_tone(psalm_num)
                psalm_num += 1
                continue
            elif 'Psalm ' + str(psalm_num - 1) in line:
                print 'deleted extra psalm number for ' + str(psalm_num - 1)
                continue
            out = parse_line(line)
            if out:
                write_to_psalm(psalm_num - 1, out)
except (KeyboardInterrupt, EOFError):
    print '\nsaving...\n'

with open('saved_place', 'w') as f:
    f.write(str(tplace))

with open('psalm_num', 'w') as f:
    f.write(str(psalm_num))

print 'exiting...\n'
