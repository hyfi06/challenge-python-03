# Resolve the problem!!
import re

def run():
    # Start coding here
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        text =f.read()
        messenge = re.findall('[a-z]+', text)
        print(''.join(messenge))

if __name__ == '__main__':
    run()
