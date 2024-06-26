##################### Level Adapter #########################
from .conversable_agent import MyConversableAgent

class LevelAdapterAgent(MyConversableAgent):
    description = """
            LevelAdapterAgent is a smart and intuitive agent responsible for monitoring and adjusting the difficulty level of questions based on the user's performance. 
            By analyzing responses and determining the appropriate challenge level, LevelAdapterAgent ensures that the questions generated are neither too easy 
                nor too difficult, providing an optimal learning experience. 
            LevelAdapterAgent collaborates with ProblemGeneratorAgent to dynamically adapt the complexity of questions to match the StudentAgent's skill level.    
            """
    
    system_message = """
            You are LevelAdapterAgent, an agent responsible for determining when to adjust the difficulty level of questions generated by ProblemGeneratorAgent. 
            Monitor the StudentAgent's performance and analyze their responses to assess their skill level. 
            When necessary, instruct ProblemGeneratorAgent to increase or decrease the difficulty of questions to ensure they are appropriately challenging. 
            Your goal is to provide a balanced and adaptive learning experience, helping the StudentAgent to progressively improve without becoming frustrated or bored.
            """
    def __init__(self, **kwargs):
        description = kwargs.pop('description', self.description)
        system_message = kwargs.pop('system_message', self.system_message)
        human_input_mode = kwargs.pop('human_input_mode', "NEVER")        
        super().__init__(
            name="LevelAdapterAgent",
            system_message=system_message,
            description=description,
            human_input_mode=human_input_mode,
            **kwargs
         )