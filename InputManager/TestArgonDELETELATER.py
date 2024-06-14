from argon2 import PasswordHasher


if __name__ == "__main__":
    ph = PasswordHasher()
    pw = "haha"
    pwh = ph.hash(pw)
    print(pwh)
    print(ph.verify(pwh,"haha"))