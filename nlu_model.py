from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu import config  # To load all the config files
from rasa_nlu.model import Trainer, Metadata, Interpreter


def train_nlu(data, config_file, model_dir):
    training_data = load_data(data)
    configuration = config.load(config_file)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='Game_Bot')


def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/Game_Bot')
    print(interpreter.parse("Hi"))


if __name__ == '__main__':
    # if already trained, dont train it again, ptherwise dont comment it out
    train_nlu('./data/data.json', 'config.yml', './models/nlu')
    run_nlu()
