import logging
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])

    training_data_file = agent.load_data("./data/stories.md")
    path_to_model = './models/dialogue'
    # domain = Domain()
    # keras policy uses LSTM
    #agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])

    agent.train(training_data_file)
    agent.persist(path_to_model)
