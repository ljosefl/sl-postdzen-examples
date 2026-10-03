import logging
from ai_agent import AIAgent

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting AI Agent for routine tasks")

    # Example task: generate a report
    ai_agent = AIAgent()
    report = ai_agent.generate_report()
    logging.info(f"Generated report: {report}")

    # Example task: process logs
    logs = ["Error in module A", "Warning in module B"]
    processed_logs = ai_agent.process_logs(logs)
    logging.info(f"Processed logs: {processed_logs}")

if __name__ == "__main__":
    main()