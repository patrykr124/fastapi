from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def hash_user(password: str):
         return pwd_context.hash(password)
     
    def verify(password: str, hash: str):
         return pwd_context.verify(password, hash)
