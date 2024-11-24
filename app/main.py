import asyncio
from database import db  # Importa a instância de conexão do banco

async def main():
    # Chama a função de conexão ao banco
    await db.connect()
    
    # Aqui você pode adicionar outras operações que interagem com o banco de dados
    print("Agora você pode realizar consultas ou operações no banco de dados.")
    
    # Após as operações, desconecte-se
    await db.disconnect()

if __name__ == "__main__":
    asyncio.run(main())  # Executa a função main de forma assíncrona
