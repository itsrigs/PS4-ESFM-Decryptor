import sys
import binascii
import os
from Crypto.Cipher import AES

def decrypt_data(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(data)
    return decrypted_data

def describe_esmf_file(file_path, np_communication_id, keygen_erk=None):
    if keygen_erk is None:
        keygen_erk = input("For step two, please provide the 32 digit retail PS4 EID Root Key: ").strip()
    keygen_erk = binascii.unhexlify(keygen_erk)
    keygen_iv = b"\x00" * 16

    with open(file_path, 'rb') as file:
        iv = file.read(16)
        encrypted_data = file.read()
        key = AES.new(keygen_erk, AES.MODE_CBC, keygen_iv).encrypt(np_communication_id.encode('utf-8').ljust(16, b'\x00'))
        decrypted_data = decrypt_data(encrypted_data, key, iv)
        output_filename = os.path.splitext(os.path.basename(file_path))[0] + '.txt'
        with open(output_filename, 'wb') as output_file:
            output_file.write(decrypted_data)
        print(f"Decrypted content saved to {output_filename}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("For step one, please provide the path to the ESFM file alongside the NP communication ID.\nExample format: esfmd.py trop.esfm NPWR12302_00")
    else:
        esmf_file_path = sys.argv[1]
        np_communication_id = sys.argv[2]
        if len(np_communication_id) != 12 or not np_communication_id.endswith("_00"):
            print("Invalid NP communication ID. It must be 12 characters in total, ending with '_00'\nExample: NPWR12302_00")
        else:
            describe_esmf_file(esmf_file_path, np_communication_id)
