class EpisodicMemory:
    def __init__(self):
        self.episodes = []

    def store_episode(self, episode: dict):
        self.episodes.append(episode)
