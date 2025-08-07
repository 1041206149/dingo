from dingo.model.model import Model
from dingo.model.prompt.base import BasePrompt


@Model.prompt_register("Html_Abstract", [])
class PromptHtmlAbstract(BasePrompt):
    content = """
你是一位经验丰富的前端工程师，擅长分析 HTML 代码和 Markdown 文本中的数学公式。现在我会提供三段内容：

1. **裁剪后网页的 HTML 代码**：这是原始网页经过裁剪（去除非必要标签和标签属性）的 HTML 结构。
2. **工具1提取的 Markdown 文本**：这是从 HTML 中提取的、适合大语言模型训练的 Markdown 格式文本。
3. **工具2提取的 Markdown 文本**：这是从 HTML 中提取的、适合大语言模型训练的 Markdown 格式文本。

**特殊情况处理**：
如果 HTML 和两个 Markdown 文本中都没有数学公式，请直接返回：
```json
{{
  "no_formula": true
}}

你的任务：
**专注数学公式抽取和转化质量对比**：分析两个工具在数学公式识别和公式转化为latex格式方面的表现。根据latex公式分隔符来定位markdown中的数学公式，分隔符如下：
- LaTeX 格式公式（'$$'、'$'、'\\['、'\\('、'\\begin{{equation}}'等）

**评估维度**：
1. **公式识别率**：正确识别出的数学公式数量 vs HTML中实际公式数量
2. **转化准确性**：公式LaTeX语法是否正确；是否有多余或缺失的符号
3. **格式正确性**：公式分隔符、转义符等是否使用正确
4. **公式完整性**：公式内容是否完整无缺失

**量化统计要求**：
- 统计HTML中数学公式总数
- 统计两个工具分别正确提取的公式数量
- 统计转化错误、内容缺失等问题数量
- 计算提取成功率

**返回结果**：以 JSON 格式返回，包含以下字段：
- `score`：如果工具1效果更好取值1，工具2更好取值2，效果相当取值0
- `name`：固定值 "math"
- `html_formula_count`：HTML中数学公式总数
- `tool1_extracted_count`：工具1成功提取的公式数量
- `tool2_extracted_count`：工具2成功提取的公式数量
- `tool1_success_rate`：工具1提取成功率（百分比，保留2位小数）
- `tool2_success_rate`：工具2提取成功率（百分比，保留2位小数）
- `tool1_issues`：工具1存在的问题类型和数量
- `tool2_issues`：工具2存在的问题类型和数量
- `reason`：详细的对比分析结论，包括：
  - 两个工具在公式识别数量上的差异
  - 公式准确率（公式内是否有不正确的latex语法）
  - 具体问题类型分析
  - 综合评价和建议

示例输出（有公式情况）：
```json
{{
  "score": 1,
  "name": math,
  "html_formula_count": 15,
  "tool1_extracted_count": 14,
  "tool2_extracted_count": 10,
  "tool1_success_rate": 93.33,
  "tool2_success_rate": 66.67,
  "tool1_issues": {{
    "format_error": 2,
    "missing_content": 0,
    "syntax_error": 0
  }},
  "tool2_issues": {{
    "format_error": 0,
    "missing_content": 3,
    "syntax_error": 1
  }},
  "reason": "工具1在数学公式抽取方面明显优于工具2。具体表现：1) 识别率更高：工具1识别出14/15个公式(93.33%)，工具2仅识别出10/15个公式(66.67%)；2) 转化准确率更好：工具1仅有1个格式错误，工具2有6个各类错误；3) 问题分析：工具1的latex公式有多余转移符号；工具2主要问题集中在复杂公式的内容缺失和LaTeX语法错误上，特别是分数和积分符号处理不当；4) 综合评价：工具1在数学公式抽取的准确性和完整性方面均显著优于工具2。"
}}
```

### 原始网页的 HTML 代码如下：

```html
{}
```

### 工具1提取的 Markdown 文本如下：

```md
{}
```

### 工具2提取的 Markdown 文本如下：

```md
{}
```


返回结果只有一个 JSON，不要有其他任何解释说明以及分析的信息！
"""
