import os
import string
import re

with open('Ursula K Le Guin.md', 'r') as f:
    tao_te_ching_md_raw = f.read()

chapter_pattern = re.compile(r'# (?P<chapter>[\d]{1,2})[ ]*\n##[ ]*(?P<chapter_name>(?:[ ]*\w+)*)[ ]*\n(?P<text>[^#]*)')
chapter_matches = re.findall(chapter_pattern, tao_te_ching_md_raw)
# Create the SUMMARY.md
foldername = lambda num, name: '{0}_{1}'.format(num, name.lower().replace(' ', '_'))
linkname = lambda num, name: '{0} - {1}'.format(num, name)
summary_line = lambda num, name: '* [{0}]({1}/README.md)'.format(linkname(num, name), foldername(num, name))
with open('SUMMARY.md', 'w') as f:
    f.write('# SUMMARY\n')
    for match in chapter_matches:
        f.write(summary_line(match[0], match[1]) + '\n')
for num, name, text in chapter_matches:
    new_folder = foldername(num, name)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    with open(new_folder + '/README.md', 'w') as f:
        f.write('# {0} - {1}\n\n'.format(num, name))
        f.write(text)

