from pydantic import BaseSettings

class Settings(BaseSettings):
     database_hostname: str
     database_port: str
     database_password: str 
     database_name: str
     database_username: str
     secret_key: str
     algorithm: str
     access_token_expire_minutes: int
    
     class Config:
         env_file = ".env"
    
    
settings = Settings()


# import os
# from dotenv import load_dotenv
# from pydantic import BaseSettings

# from pathlib import Path
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

# class Settings(BaseSettings):
#     database_hostname: str = os.getenv("DATABASE_HOSTNAME")
#     database_port: str = os.getenv("DATABASE_PORT")
#     database_password: str = os.getenv("DATABASE_PASSWORD") 
#     database_name: str = os.getenv("DATABASE_NAME") 
#     database_username: str = os.getenv("DATABASE_USERNAME") 
#     secret_key: str = os.getenv("SECRET_KEY") 
#     algorithm: str = os.getenv("ALGORITHM") 
#     access_token_expire_minutes: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES") 
#     DATABASE_URL = f"postgresql://{database_username}:{database_password}@{database_hostname}:{ database_port}/{database_name}"

# settings = Settings()
# # from pydantic import BaseSettings

# # class Settings(BaseSettings):
# #     DATABASE_HOSTNAME: str
# #     DATABASE_PORT: str
# #     DATABASE_PASSWORD: str 
# #     DATABASE_NAME= str
# #     DATABASE_USERNAME: str
# #     SECRET_KEY: str
# #     ALGORITHM: str
# #     ACCESS_TOKEN_EXPIRE_MINUTES: str

# #     # database_hostname: str
# #     # database_port: str
# #     # database_password: str 
# #     # database_name= str
# #     # database_username: str
# #     # secret_key: str
# #     # algorithm: str
# #     # access_token_expire_minutes: int
    
# #     class Config:
# #         env_file = ".env"
    
    
# # settings = Settings()  

  