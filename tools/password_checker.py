import re

def check_password_strength(password: str) -> str:
    """Cek kekuatan password berdasarkan kriteria dasar."""
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error:
        return "Lemah: Password harus minimal 8 karakter."
    if digit_error:
        return "Lemah: Password harus mengandung angka."
    if uppercase_error:
        return "Lemah: Password harus mengandung huruf besar."
    if lowercase_error:
        return "Lemah: Password harus mengandung huruf kecil."
    if symbol_error:
        return "Lemah: Password harus mengandung simbol khusus."
    return "Kuat: Password sudah memenuhi kriteria keamanan."

def main():
    print("=== Password Strength Checker ===")
    password = input("Masukkan password untuk dicek: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
