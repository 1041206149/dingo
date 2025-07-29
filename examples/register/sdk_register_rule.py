import re

from dingo.config.input_args import EvaluatorRuleArgs
from dingo.io import Data
from dingo.model.model import Model
from dingo.model.modelres import ModelRes
from dingo.model.rule.base import BaseRule


@Model.rule_register('QUALITY_BAD_RELEVANCE', ['test'])
class CommonPatternDemo(BaseRule):
    """let user input pattern to search"""
    dynamic_config = EvaluatorRuleArgs(pattern = "blue")

    @classmethod
    def eval(cls, input_data: Data) -> ModelRes:
        res = ModelRes()
        matches = re.findall(cls.dynamic_config.pattern, input_data.content)
        if matches:
            res.error_status = True
            res.type = cls.metric_type
            res.name = cls.__name__
            res.reason = matches
        return res


if __name__ == '__main__':
    from dingo.config import InputArgs
    from dingo.exec import Executor

    input_data = {
        "input_path": "../../test/data/test_local_json.json",
        "dataset": {
            "source": "local",
            "format": "json",
            "field": {
                "content": "prediction"
            }
        }
    }
    input_args = InputArgs(**input_data)
    executor = Executor.exec_map["local"](input_args)
    result = executor.execute()
    print(result)
