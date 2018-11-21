from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb8LQ6gAi1SUQ9s62jRUvujTeQu3yLOtzJOW7mVNAKmyf0d4GDgMe3DcQC0OCgjI3XWcQbOh_-nQX5DSzGy-Tv5pHecNLPbVoUsyszHIY774TnkOcJFM83AVAXkxSqhwUkcHHa-jWtusrKeLey7exe8Kc3nAdtFhZoF-xOF4RVzOwCLBd-DUWRKn_vDyhBac17Ex0A'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()