import config
from client import dashVectorClient
from langchain_community.vectorstores import DashVector
from langchain_openai import OpenAIEmbeddings


if __name__ == "__main__":
    # コレクション名を指定
    collection = dashVectorClient.get(config.DASHVECTOR_COLLECTION_NAME)

    # 埋め込みを作成
    embeddings = OpenAIEmbeddings(
        openai_api_key=config.OPENAI_API_KEY,
        model="text-embedding-3-large",
    )

    # 初期化
    vectorstore = DashVector(collection, embeddings, "text")

    # ドキュメントをクエリ
    query = "ロゼワイン"
    simDocScore = vectorstore.similarity_search_with_relevance_scores(query, k=3)
    for simDoc, Score in simDocScore:
        print("類似ドキュメント: ", simDoc.page_content)
        print("類似ドキュメントのスコア: ", Score)
