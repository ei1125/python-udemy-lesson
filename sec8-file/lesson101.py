# tempfile
# 使い終わった後消してくれる

import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# 残らない
with tempfile.TemporaryDirectory() as td:
    print(td)

# 残る
temp_dir = tempfile.mkdtemp()
print(temp_dir)

# $ ls -al /var/folders/8h/l___jm_d0rbcrwjw_mv4sr3w0000gn/T/tmplulihp2x