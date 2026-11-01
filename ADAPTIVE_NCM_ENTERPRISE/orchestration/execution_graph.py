class ExecutionGraph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, agent_name: str):
        if agent_name not in self.nodes:
            self.nodes.append(agent_name)
            self.edges[agent_name] = []

    def add_edge(self, from_agent: str, to_agent: str):
        self.edges[from_agent].append(to_agent)
