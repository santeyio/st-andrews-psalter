import re

####### Helpers ########

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

def convert_psalm(psalm_file_name, psalm_number):
    reformatted_text = ''
    with open(psalm_file_name, 'r') as psalm:
        reformatted_text += "  '%s': {\n" % str(psalm_number)
        for lnum, line in enumerate(psalm, 0):
            if lnum == 0:
                reformatted_text += "    tone: '%s',\n    text: `\n" % line.rstrip()
            elif lnum == 1:
                continue
            else:
                if '__' in line:
                    line = line.replace('__', '<u>', 1)
                    line = line.replace('__', '</u>', 1)
                regex = re.compile('^  ')
                if regex.search(line):
                    line = line.replace('  ', '&nbsp;&nbsp;', 1)
                line = line.rstrip() + "<br/>\n"
                reformatted_text += line
        reformatted_text += "    `,\n"
        reformatted_text += "  },\n"
    return reformatted_text

####### Script ########

psalm_num = 1

with open('../psalm_num', 'r') as f:
    for line in f:
        psalm_num = int(line)

psalm_num -= 1

with open('_out.js', 'w') as outf:
    count = psalm_num # int(raw_input('>>> '))
    outf.write('module.exports.Psalms = {\n')
    for i in range(1, count + 1):
        if i == 23:
            append_text1 = convert_psalm('psalm_023_1', i)
            append_text2 = convert_psalm('psalm_023_6', i)
            outf.write(append_text1)
            outf.write(append_text2)
        else:
            append_text = convert_psalm('psalm_' + pad_with_zeros(i), i)
            outf.write(append_text)
    outf.write('};\n')
