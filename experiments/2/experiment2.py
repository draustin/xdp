from subprocess import check_output, Popen, PIPE, run
import json

run(['pandoc', 'test.md', '-o', 'test.html'])
ast = json.loads(check_output(['pandoc', 'test.md', '-t', 'json']))