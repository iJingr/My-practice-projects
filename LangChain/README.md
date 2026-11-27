# LangChain 练习 · 构建最简单聊天助手

终端里的多轮聊天机器人：带记忆、带历史裁剪、带流式输出、能清空。模型走 DeepSeek（OpenAI 兼容协议）。

## 环境

| 项 | 值 |
|---|---|
| Python | 3.11.2（项目自带 `.venv`，由 uv 管理） |
| 依赖 | langchain 1.5.2 / langchain-core 1.8.4 / langchain-deepseek 1.2.1 / python-dotenv 1.2.4 |
| 密钥 | 项目根目录 `.env`：`DEEPSEEK_API_KEY`、`DEEPSEEK_BASE_URL`（**已被 .gitignore 排除，不入库**） |

## 启动

```bash
cd LangChain
.venv\Scripts\python.exe src\module01\work_chat_bot.py
```

进入后一次输入一行：

- 普通文字 → 发给孩子模型，流式打印回答
- `clear` → 清空历史（保留系统提示）
- `quit` → 退出
- 直接回车 → 跳过，不发请求

## 代码结构

`src/module01/work_chat_bot.py`

| 方法 | 作用 |
|---|---|
| `__init__` | 建模型客户端；初始化 `self.messages`，第 0 条是 SystemMessage |
| `_trim_history` | 超过 `MAX_HISTORY = 10` 组（20 条）时裁掉最早对话，**始终保留第 0 条系统提示** |
| `chat` | 普通对话：追加用户消息 → `invoke` → 追加 AI 回复 → 裁剪 → 返回文本 |
| `chat_stream` | 流式对话：`yield` 每段增量，循环结束后把累加结果作为一条 AIMessage 记入历史 |
| `clear_history` | 只留第 0 条，其余清空 |
| `__main__` | CLI 主循环：一条输入分四类分支 |

## 关键设计

- **记忆靠清单，不靠模型**：模型本身无状态，每轮把 `self.messages` 全量发过去，它“重读”历史才有上下文。
- **裁剪按组**：一问一答是一组，`MAX_HISTORY = 10` 组；裁完仍是 `System → Human → AI …` 的交替结构。
- **流式只交增量**：`chat_stream` 里 `yield` 的每段只是增量，屏幕上要 `print(chunk, end='', flush=True)`，否则会攒成一坨或一行一段。

## 已知边界（面试会问）

1. 流式被中途打断（Ctrl+C / break）时，`for` 之后的历史写入不会执行 → 半截回答丢失，下一轮清单里出现两条连续的 `HumanMessage`，模型会把旧问题再答一遍。
2. `self.messages` 挂在实例上：两个用户共用一个实例会串台。要多用户得每会话一个实例，或把历史存到外部（DB / Redis）。
3. 裁剪只保留最近 10 组，早期信息会丢。想留长记忆需要另做摘要式压缩。
