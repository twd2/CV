def has_non_ascii(s):
    for c in s:
        if c >= 128:
            return True
    return False

current_section = b''
with open('README.txt', 'rb') as fin, \
     open('RESUME.txt', 'wb') as fout:
    for line in fin:
        if line.strip() and not line.startswith(b'    '):
            current_section = line.strip()
        if current_section in [b'RELEVANT COURSES', b'WORKSHOPS', b'SELECTED PROJECTS']:
            print('Ignoring', line.rstrip())
            continue
        if has_non_ascii(line) or b'Tongji CTF' in line:
            print('Ignoring', line.rstrip())
            continue
        fout.write(line)