import asyncio
from prisma import Prisma

class Database:
    def __init__(self):
        self.db = Prisma()

    async def connect(self):
        await self.db.connect()
        print("Conexão bem-sucedida ao banco de dados!")

    async def disconnect(self):
        await self.db.disconnect()
        print("Desconectado do banco de dados.")

# Exemplo de uso da classe Database
db = Database()

async def main():
    await db.connect()  # Chama a função de conexão
    # Aqui você pode chamar outros métodos que interagem com o banco de dados
    await db.disconnect()  # Desconecta após as operações

if __name__ == "__main__":
    asyncio.run(main())
