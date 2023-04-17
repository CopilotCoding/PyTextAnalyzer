import tokenize

def extract_comments(file_path):
    with open(file_path, 'rb') as f:
        tokens = tokenize.tokenize(f.readline)
        comments = [token.string.strip() for token in tokens
                    if token.type == tokenize.COMMENT]
    with open('output.py', 'w') as f:
        for comment in comments:
            f.write(comment + '\n')

if __name__ == '__main__':
    extract_comments('source_code.py')
