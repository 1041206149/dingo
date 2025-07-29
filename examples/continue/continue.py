from dingo.config import InputArgs
from dingo.exec import Executor


def exec_first():
    input_data = {
        "input_path": "../../test/data/test_local_jsonl.jsonl",
        "dataset": {
            "source": "local",
            "format": "jsonl",
            "field": {
                "id": "id",
                "content": "content"
            }
        },
        "executor": {
            "eval_group": "sft",
            "end_index": 1,
            "result_save": {
                "bad": True,
                "good": True
            }
        }
    }

    input_args = InputArgs(**input_data)
    executor = Executor.exec_map["local"](input_args)
    result = executor.execute()
    print(result)


def exec_second():
    input_data = {
        "input_path": "../../test/data/test_local_jsonl.jsonl",
        "dataset": {
            "source": "local",
            "format": "jsonl",
            "field": {
                "id": "id",
                "content": "content"
            }
        },
        "executor": {
            "eval_group": "sft",
            "start_index": 1,
            "result_save": {
                "bad": True,
                "good": True
            }
        }
    }

    input_args = InputArgs(**input_data)
    executor = Executor.exec_map["local"](input_args)
    result = executor.execute()
    print(result)


if __name__ == '__main__':
    exec_first()
    exec_second()
