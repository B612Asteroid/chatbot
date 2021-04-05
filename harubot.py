from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter


def train_harubot(data_json, config_file, model_dir):
    training_data = load_data(data_json)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='harubot')


def predict_intent(text):
    interpreter = Interpreter.load('./models/nlu/default/harubot')
    print(interpreter.parse(text))


#train_harubot('./data/data.json', './config.json', './models/nlu')
predict_intent("안녕! 반가워! 너의 취미가 뭐니?")