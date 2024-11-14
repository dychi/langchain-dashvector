import config
from typing import List
from os.path import join, dirname
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import DashVector


def create_docs() -> List[Document]:
    """ドキュメントを作成する関数。

    この関数は、指定されたテキストファイルからドキュメントをロードし、
    テキストを指定されたサイズのチャンクに分割し、各ドキュメントに
    メタデータを追加します。

    Returns:
        List[Document]: 作成されたドキュメントのリスト。
    """
    # テキストローダーを作成
    loader = TextLoader(join(dirname(__file__), "../data/sample.txt"))
    documents = loader.load()
    # テキストを分割するための設定
    text_splitter = CharacterTextSplitter(
        chunk_size=100, chunk_overlap=0, separator="。"
    )
    docs = text_splitter.split_documents(documents)
    # メタデータを設定
    for doc in docs:
        doc.metadata = {
            "source": "sample.txt"
        }  # ローカルPCの絶対パスが使用されるため、sourceを明示的に更新.それ以外のmetadataを付与することも可能
    return docs


if __name__ == "__main__":
    print("コレクションを作成し、ドキュメントを追加します")

    # 埋め込みを作成
    embeddings = OpenAIEmbeddings(
        openai_api_key=config.OPENAI_API_KEY,
        model="text-embedding-3-large",
    )

    # ドキュメントを作成
    docs = create_docs()
    for document in docs:
        print("ドキュメント: ", document.page_content)

    # コレクションを作成し、ドキュメントを追加
    vectorstore = DashVector.from_documents(
        docs,
        embeddings,
        collection_name=config.DASHVECTOR_COLLECTION_NAME,  # collection_nameを指定(add_texts関数をwrapしているため)
    )

    # テキストを追加するサンプル
    # texts = ["foo", "bar", "baz"]
    # metadatas = [{"key": i} for i in range(len(texts))]
    # ids = ["0", "1", "2"]

    # vectorstore.add_texts(texts, metadatas=metadatas, ids=ids)
