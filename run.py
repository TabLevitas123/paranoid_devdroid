
from collaborative_marvin import CollaborativeMarvin
from communication_protocol import CommunicationProtocol
from core import CoreSystem
from dynamic_exploration_marvin import DynamicExplorationMarvin
from efficiency_vs_accuracy import EfficiencyVsAccuracy
from expert_panel import ExpertPanel
from fix_errors import ErrorFixer
from goal_oriented_marvin import GoalOrientedMarvin
from health_check import HealthCheck
from long_term_memory_marvin import LongTermMemoryMarvin
from marvin_orchestration import MarvinOrchestration
from meta_learning_marvin import MetaLearningMarvin
from monitoring.performance_monitoring_marvin import PerformanceMonitoringMarvin
from multi_agent_marvin import MultiAgentMarvin
from multi_stage_marvin import MultiStageMarvin
from multi_stage_task_handling import MultiStageTaskHandling
from nested_task_marvin import NestedTaskMarvin
from performance_tracking_marvin import PerformanceTrackingMarvin
from predictive_optimization_marvin import PredictiveOptimizationMarvin
from real_time_awareness_marvin import RealTimeAwarenessMarvin
from resource_efficient_marvin import ResourceEfficientMarvin
from roastmaster import RoastMaster

# Agent initialization
agents = {
    'collaborative': CollaborativeMarvin(),
    'communication': CommunicationProtocol(),
    'core': CoreSystem(),
    'exploration': DynamicExplorationMarvin(),
    'efficiency_vs_accuracy': EfficiencyVsAccuracy(),
    'expert_panel': ExpertPanel(),
    'error_fixer': ErrorFixer(),
    'goal_oriented': GoalOrientedMarvin(),
    'health_check': HealthCheck(),
    'long_term_memory': LongTermMemoryMarvin(),
    'orchestration': MarvinOrchestration(),
    'meta_learning': MetaLearningMarvin(),
    'performance_monitoring': PerformanceMonitoringMarvin(),
    'multi_agent': MultiAgentMarvin(),
    'multi_stage': MultiStageMarvin(),
    'task_handling': MultiStageTaskHandling(),
    'nested_task': NestedTaskMarvin(),
    'performance_tracking': PerformanceTrackingMarvin(),
    'predictive_optimization': PredictiveOptimizationMarvin(),
    'real_time_awareness': RealTimeAwarenessMarvin(),
    'resource_efficient': ResourceEfficientMarvin(),
    'roastmaster': RoastMaster(),
}

def marvin_task_prompt():
    print("Welcome to Marvin's System. Please provide a task:")
    task = input("Insert task description: ")

    # Dynamically select the appropriate agents for the task
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
