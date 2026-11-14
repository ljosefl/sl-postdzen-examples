from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import AgentAction, AgentFinish
from langchain.agents import AgentExecutor, initialize_agent, Tool

class AccessControlAgent:
    def __init__(self, llm):
        self.llm = llm
        self.tools = self._setup_tools()
        self.agent = initialize_agent(self.tools, self.llm, agent="zero-shot-react-description", verbose=True)

    def _setup_tools(self):
        tools = [
            Tool(
                name="CheckAccess",
                func=self.check_access,
                description="Check if access is allowed based on the provided criteria."
            )
        ]
        return tools

    def check_access(self, criteria):
        # Simulate checking access based on criteria
        if criteria.get("country") == "China" and criteria.get("technology") == "AI Chips":
            return AgentFinish({"output": "Access denied due to export control restrictions."}, "")
        return AgentFinish({"output": "Access granted."}, "")

    def run(self, input_text):
        action = self.agent.plan(input_text)
        if isinstance(action, AgentAction):
            action_output = action.tool_func(**action.tool_input)
            return action_output["output"]
        return self.agent.finish_action()

if __name__ == "__main__":
    llm = OpenAI(temperature=0)
    agent = AccessControlAgent(llm)
    input_text = "Check if access to AI chips is allowed in China."
    result = agent.run(input_text)
    print(result)