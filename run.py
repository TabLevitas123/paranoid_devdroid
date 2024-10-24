
import importlib

# Load all agents from the 'agents' directory dynamically, along with the newly specified agents
def load_agents():
    agents = {}
    # List of newly specified agent modules
    new_agent_modules = [
        'collaborative_marvin', 'communication_protocol', 'core', 'dynamic_exploration_marvin', 
        'efficiency_vs_accuracy', 'expert_panel', 'fix_errors', 'goal_oriented_marvin', 
        'health_check', 'long_term_memory_marvin', 'marvin_orchestration', 'meta_learning_marvin', 
        'monitoring.performance_monitoring_marvin', 'multi_agent_marvin', 'multi_stage_marvin', 
        'multi_stage_task_handling', 'nested_task_marvin', 'performance_tracking_marvin', 
        'predictive_optimization_marvin', 'real_time_awareness_marvin', 'resource_efficient_marvin', 'roastmaster'
    ]

    # Adding the agents from the agents directory dynamically
    agent_modules = [
        'adaptive_task_complexity', 'agent_collaboration', 'agent_collaboration_analytics', 
        'agent_learning', 'agent_llm_integration', 'agent_logging', 'autonomous_system_scaling', 
        'bottleneck_detection', 'cognitive_knowledge_fusion', 'cognitive_synergy', 
        'cross_system_integration', 'decision_tree_construction', 'decision_tree_execution', 
        'deep_strategy_orchestration', 'ecosystem_optimization', 'energy_optimization', 
        'global_awareness', 'hierarchical_task_handling', 'interrogator_enhanced', 
        'llm_feedback_loop', 'llm_strategy_optimization', 'llm_task_breakdown', 
        'long_term_task_memory', 'memory_garbage_collection', 'meta_learning', 
        'metasystemic_consciousness', 'modular_agents', 'multi_agent_task_orchestration', 
        'multi_agent_task_prioritization', 'neural_cognitive_evolution', 'performance_monitoring', 
        'predictive_task_preprocessing', 'real_time_feedback_learning', 'real_time_resource_allocation', 
        'reinforcement_learning', 'roastmaster_2_0', 'roastmaster_2_1', 'roastmaster_enhanced', 
        'role_specialization', 'self_governance', 'self_optimization_feedback', 
        'self_replicating_agent_ecosystem', 'self_reprogramming', 'system_self_replication', 
        'task_complexity_scoring', 'task_flow_automation', 'task_simulation'
    ]

    # Combine all agents
    all_agent_modules = agent_modules + new_agent_modules

    for module in all_agent_modules:
        try:
            imported_module = importlib.import_module(f"agents.{module}")
            agents[module] = getattr(imported_module, 'Agent')()
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Failed to load {module}: {str(e)}")
    
    return agents

# Main function to assign and handle tasks
def marvin_task_prompt():
    print("Welcome to Marvin's Full System. Please provide a task:")
    task = input("Insert task description: ")

    agents = load_agents()
    
    # Select the appropriate agents dynamically based on task
    selected_agents = [agent for agent_name, agent in agents.items() if agent.can_handle_task(task)]
    
    if selected_agents:
        print(f"Selected agents: {[agent.__class__.__name__ for agent in selected_agents]}")
        for agent in selected_agents:
            result = agent.handle_task(task)
            print(f"Agent {agent.__class__.__name__} result: {result}")
    else:
        print("No suitable agent found for this task.")

if __name__ == "__main__":
    marvin_task_prompt()
