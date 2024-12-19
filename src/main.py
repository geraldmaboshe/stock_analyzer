#!/usr/bin/env python
import sys
from crew import StockAnalyzerCrew
import agentops
from typing import Optional

agentops.init(default_tags=['crewai', 'agentstack'])


def run(inputs: Optional[dict] = None):
    """
    Run the crew.
    """

    if inputs is None:
        # Prompt the user for a URL
        url = input("Enter the URL to scrape (default: https://finance.yahoo.com/): ")
        if not url:
            url = 'https://finance.yahoo.com/'
        inputs = {
            'url': url
        }
    print(f"Using URL: {inputs['url']}")
    return StockAnalyzerCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
    }
    try:
        StockAnalyzerCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        StockAnalyzerCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
    }
    try:
        StockAnalyzerCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


if __name__ == '__main__':
    run()