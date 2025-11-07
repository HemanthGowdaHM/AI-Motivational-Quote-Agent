
"""
CLI entry for AI Motivational Quote Agent(Python).
    - Optional args: student name, focus area
    - Write UTF-8 text to gpt_output.txt
    - Robust error message for beginners
"""

import os 
import sys
from pathlib import Path
from datetime import datetime

from openai_client import OpenAIChatClient
from ai_motivational_agent import AIMotivationalQuoteAgent

HEADER = """\
===============================
AI Motivational Quote Agent
TimeStamp:{ts}
===============================

"""

def main( argv:list[str]) -> int:
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set in your environment. ", file=sys.stderr)
        return 1
    
    student_name = argv[1] if len(argv) >= 2 else "student"
    focus_area = argv[2] if len(argv) >= 3 else "DSA and System design"
    
    try:
        # step 1 : create a client to talk to GPT or Gen AI
        client = OpenAIChatClient(model="gpt-4o-mini")
        
        # step 2 : create a specific agent to be invoked ( Motivational agent)
        agent = AIMotivationalQuoteAgent(client)
        
        # step 3 : Invoke the agent to get response
        advice = agent.generate_advice(student_name, focus_area)
        
        # step 4 : If you  get the response write it to a file 
        out_path = Path("gpt_output.text")
        out_path.write_text(HEADER.format(ts=datetime.now()) + advice + "\n", encoding="utf-8")
        print(f"SUCCESS: Wrote teh advice to {out_path.resolve()}")
        
        # step 5 : print the advice on the terminal |
        print("Response received is ....")
        print(advice)
        return 0
    
    except Exception as ex:
        # If something goes wrong catch the exception and show the error
        print(f"ERROR: {ex}", file=sys.stderr)
        # If there is an error you return a non zero value
        return -1
    
if __name__ == "__main__" :
    sys.exit(main(sys.argv))