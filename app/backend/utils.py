from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

def load_model():

    # Charger le modèle pré-entraîné GPT-2
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Charger et prétraiter les données d'entraînement
    training_data = "../app/data/data.txt"
    train_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=training_data,
        block_size=128
    )

    # Configurer les paramètres d'entraînement
    training_args = TrainingArguments(
        output_dir="./chatbot_finetuned",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
        num_samples=len(train_dataset)
    )

    # Configurer le modèle pour fine-tuning
    config = GPT2Config.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name, config=config)

    # Créer le Trainer et démarrer le fine-tuning
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
        train_dataset=train_dataset,
    )

    trainer.train()
