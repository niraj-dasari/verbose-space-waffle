from haystack.nodes import FARMReader
model = "deepset/roberta-base-squad2"
reader = FARMReader(model, use_gpu=True)

reader.train( data_dir='./data', train_filename="dev-v2.0.json", use_gpu=True, n_epochs=1, save_dir="my_model" )

reader.save('roberta_base_squad2')
