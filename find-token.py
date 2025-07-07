import re
import sys


def extract_basic_auth_tokens(log_file_path):

    rsl = set()
    
    pattern = re.compile(r'Basic\s+([A-Za-z0-9+/=]+)')

    with open(log_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                token = match.group(0).strip()  # Whole "Basic base64token"
                rsl.add(token)

    return rsl


def get_file_name():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return None


def main():
    file_name = get_file_name()
    if not file_name:
        return
    tokens = extract_basic_auth_tokens(file_name)
    print("Found Basic Auth tokens:")
    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()
