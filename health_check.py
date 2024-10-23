
import subprocess
from agents.modular_agents import DependencyRepairAgent, RuntimeErrorAgent, CredentialRepairAgent

def run_health_check():
    # Run the main program and capture errors in a log
    try:
        subprocess.run(['python', 'main.py'], check=True)
        print("Program ran successfully.")
    except subprocess.CalledProcessError as e:
        error_message = str(e)
        print(f"Error encountered: {error_message}")

        # Modular agent checks
        dep_agent = DependencyRepairAgent()
        runtime_agent = RuntimeErrorAgent()
        cred_agent = CredentialRepairAgent()

        # Try to auto-repair
        if dep_agent.resolve_dependency_issue('error.log'):
            print("Dependency issue fixed. Retrying...")
        elif runtime_agent.handle_runtime_error(error_message):
            print("Runtime error fixed. Retrying...")
        elif cred_agent.check_and_update_credentials("API_NAME"):
            print("Credential issue fixed. Retrying...")
        else:
            print("Unknown issue. Needs manual intervention.")

run_health_check()
