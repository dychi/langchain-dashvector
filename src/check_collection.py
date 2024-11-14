import config
from client import dashVectorClient
from dashvector import DashVectorException

if __name__ == "__main__":
    print("コレクションが存在しているか確認します")

    # コレクションを取得
    collection = dashVectorClient.get(config.DASHVECTOR_COLLECTION_NAME)
    if collection:
        print("コレクションはすでに存在します")
    else:
        print("コレクションを作成")
        # === コレクション作成 ===
        # rsp = dashVectorClient.create(config.DASHVECTOR_COLLECTION_NAME, dimension=1024)
        # if not rsp:
        #     raise DashVectorException(rsp.code, reason=rsp.message)
        # print("レスポンス: ", rsp)
