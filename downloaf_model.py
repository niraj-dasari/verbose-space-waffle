from haystack.nodes import FARMReader 
# Initialise Reader 
model = "deepset/roberta-base-squad2" 
reader = FARMReader(model) 
# Perform fine-tuning 
train_data = "./" 
train_filename = "train.json" 
save_dir = "finetuned_model" 
reader.train(train_data, train_filename, save_dir=save_dir) 
# Load 
finetuned_reader = FARMReader(save_dir)