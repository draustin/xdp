from subprocess import check_output, Popen, PIPE
import json

ast1 = json.loads(check_output(['pandoc', 'test1.md', '-t', 'json']))
ast2 = json.loads(check_output(['pandoc', 'test2.md', '-t', 'json']))

def increase_heading(block, n):
    if block['t'] == 'Header':
        block = block.copy()
        c = block['c'].copy()
        c[0] += n
        block['c'] = c
    return block


ast = {'blocks':ast1['blocks'] + [increase_heading(b, 2) for b in ast2['blocks']], 'pandoc-api-version':ast1['pandoc-api-version'], 'meta':{}}

p = Popen(['pandoc', '-f', 'json', '-o', 'test1+2.html'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout_data, stderr_data = p.communicate(json.dumps(ast).encode())