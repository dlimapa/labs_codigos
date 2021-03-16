import dotenv
import os

#Efetivamente carrega os valores do arquivo .env
dotenv.load_dotenv(dotenv.find_dotenv())

print("User: " + os.getenv("username"))
print("Senha: " + os.getenv("senha"))
