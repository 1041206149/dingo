from dingo.config import InputArgs
from dingo.exec import Executor


def classify_topic():
    input_data = {
        "input_path": "../../test/data/test_sft_jsonl.jsonl",
        "dataset": {
            "source": "local",
            "format": "jsonl",
            "field": {
                "content": "question"
            }
        },
        "executor": {
            "prompt_list": ["PromptClassifyTopic"],
            "result_save": {
                "bad": True,
                "good": True
            }
        },
        "evaluator": {
            "llm_config": {
                "LLMClassifyTopic": {
                    "key": "",
                    "api_url": "",
                }
            }
        }
    }
    input_args = InputArgs(**input_data)
    executor = Executor.exec_map["local"](input_args)
    result = executor.execute()
    print(result)


if __name__ == '__main__':
    classify_topic()
