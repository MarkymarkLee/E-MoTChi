# Taiwan-LLaMa v2.0 
This model is for bi-directional translation of emoji and traditional chinese.
We choose Taiwan-LLM-13B-v2.0-chat as our base model, and use OpenAccess-AI-Collective/atolotl to finetune it.

## Setting Up Environment
Follow the instructions of ![https://github.com/OpenAccess-AI-Collective/axolotl] to set up the environment correctly.

## Training
Before training, you may need to create/modify a yml file to set up finetune configuration.
There are some examples under directory `yml`, the often adjusted parameters are
* datasets
* output_dir
* lora_r (rank of QLORA)
* mocro_batch_size
* num_epochs

After you have a yml file, you can use the following command to start training!
`./train.sh $<path_to_yml>`

## Inference
After you finetune a model, you can then inference some output to verify the performance.
To inference, you just need to modify the inference.sh and then execute it.
Common parsers:
* `--to_emoji`: Optional. If set, the model would inference on the task `chinese to emoji`.
* `--algo_to_chinese`: Optional, If set, the model would inference on the task `algorithm generated emoji to chinese`.
* `--gpt_to_chinese`: Optional, If set, the model would inference on the task `gpt generated emoji to chinese`.
* `--base_model_path`: Required. Path to the `Taiwan-LLM-13B-v2.0-chat`.
* `--peft_path`: Required. Path to the adapter model.
* `--test_data_path`: Required. Path to the test data path, which includes `id`, chinese`, `emoji-gpt`, `emoji-algo`, four keys per dictionary.
* `--output_path`: Required. You can redirect it to your desire directory.

The following command would start inference!
`./inference.sh $<path_to_peft_model>`

## Peft Model
You can download two models with the following commands
* Chinese to Emoji
`gdown "https://drive.google.com/uc?export=download&id=1EkMvXgbDGPgvDzDH6EJN_2DRWKDVzqD0"`
* Emoji to Chinese
`gdown "https://drive.google.com/file/d/1yuSaH2mP511l0h67tSTRlMS1Bb7O-OKt/view?usp=sharing"`