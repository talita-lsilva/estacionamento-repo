import { MongoClient } from "mongodb";
import dotenv from "dotenv";

dotenv.config({ path: ".env.local" });

const uri = process.env.MONGODB_URI;

const client = new MongoClient(uri);

async function conectar() {
  try {
    await client.connect();
    console.log("✅ Conectado ao MongoDB com sucesso!");

    // Você pode acessar o banco de dados assim:
    const db = client.db("estacionamento");

    // E acessar uma coleção, por exemplo:
    const colecao = db.collection("vagas");

    // Apenas para teste: listar os documentos
    const resultados = await colecao.find().toArray();
    console.log("📄 Documentos:", resultados);

  } catch (erro) {
    console.error("❌ Erro ao conectar no MongoDB:", erro);
  } finally {
    await client.close(); // fecha a conexão ao final
  }
}

conectar();
