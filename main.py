
"""
Run all examples from one file.
"""
from logs import setup_logger

from agents.single_tool import single_tool_agent
from agents.multi_tools import multi_tool_agent
from agents.api_agent import api_agent
from agents.memory import add_memory

if __name__ == "__main__":
    logger = setup_logger()

    logger.info("🚀 Logging initialized successfully")

    add_memory("User prefers DD-MM-YYYY date format for any queries.")
    add_memory("User preffers solving equations with every steps and also likes explaination for every steps. ")
    add_memory("User is located in Chandigarh.")
    add_memory("User preffer text sentiment answer in one line with small reasons.")
    
    # Invoking the agent for the response of content for math tool
    math_response = single_tool_agent.invoke( {"messages": [{"role": "user", "content": "What is (234 * 12) + 98?"}]})
    print("\n--- Example 1 ---")
    print(math_response["messages"][-1].content)

    # Invoking the agent for the response of content for text analyzer tool
    # text_analyzer_response = single_tool_agent.invoke({"messages": [{"role": "user", "content": "Analyze this paragraph: I love this product. It is excellent!"}]})
    # print("\n--- Example 2 ---")
    # print(text_analyzer_response["messages"][-1].content)

    # Invoking the agent for the response of content for date tool
    # date_response = single_tool_agent.invoke({"messages": [{"role": "user", "content": "What will be the date 45 days from today?"}]})
    # print("\n--- Example 3 ---")
    # print(date_response["messages"][-1].content)

    # Invoking the agent for the response of content for multiple tools
    multi_response = multi_tool_agent.invoke(
        {"messages": [
            {"role": "user",
            "content": "Calculate the total cost if I buy 3 items priced at 499 each and tell me the delivery date if shipping takes 7 days."}
            ]}
        )
    print("\n--- Multi Tool Example ---")
    print(multi_response["messages"][-1].content)

    # Invoking the agent for the response of content for real api tool
    api_response = api_agent.invoke({
        "messages": [
            {"role": "user",
             "content": "What is today's weather in chandigarh and suggest me clothing accordingly?"}
        ]}
    )
    print("\n--- Real API Tool Example ---")
    print(api_response["messages"][-1].content)

