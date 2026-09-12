import hashlib

def find_secret_key(input, n_zeros) -> int:
    num = 0
    md5_hash = hashlib.md5(input.encode())
    cur_hex_start = md5_hash.hexdigest()[:n_zeros]
    leading_zeros = n_zeros * "0"

    while cur_hex_start != leading_zeros:
        num += 1
        cur_input = input + str(num)
        md5_hash = hashlib.md5(cur_input.encode())
        cur_hex_start = md5_hash.hexdigest()[:n_zeros]

    return num
