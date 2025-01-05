from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=LiteLLMModel(model_id="bedrock/anthropic.claude-3-sonnet-20240229-v1:0"))

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
