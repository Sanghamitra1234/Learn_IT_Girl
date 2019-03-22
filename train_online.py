from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

# from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core import utils, train, run
from rasa_core.training import interactive


logger = logging.getLogger(__name__)


def train_agent():
    return train.train_dialogue_model(domain_file="domain.yml",
                                      stories_file="data/stories.md",
                                      output_path="models/dialogue",
                                      kwargs={"batch_size": 50,
                                              "epochs": 200
                                              })


if __name__ == '__main__':
    # logging.basicConfig(level='INFO')
    utils.configure_colored_logging(loglevel="INFO")
    # interpreter = RasaNLUInterpreter('./models/nlu/default/Game_bot')
    agent = train_agent()
    online.run_online_learning(agent)
    # run_online_trainer(ConsoleInputChannel(), interpreter)
