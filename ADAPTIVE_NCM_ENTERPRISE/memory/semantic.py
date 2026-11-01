class SemanticMemory:
    def __init__(self):
        self.knowledge_base = {}

    def search_similar(self, query: str, top_k: int = 3):
        return [{"doc_id": "SEM-01", "score": 0.89, "text": f"Semantic content for '{query}'"}]
