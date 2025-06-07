import hashlib

def hash_password(password: str) -> str:
    """Hash password menggunakan SHA256."""
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

def main():
    print("=== Password Hasher (SHA256) ===")
    password = input("Masukkan password: ")
    hashed = hash_password(password)
    print(f"Hash SHA256: {hashed}")

if __name__ == "__main__":
    main()
