import config
from dashvector import Client

# DashVectorクライアントを初期化
dashVectorClient = Client(
    api_key=config.DASHVECTOR_API_KEY, endpoint=config.DASHVECTOR_ENDPOINT
)
assert dashVectorClient is not None
