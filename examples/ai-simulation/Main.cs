using UnityEngine;
using System.Collections.Generic;

public class Main : MonoBehaviour
{
    private List<Agent> agents;
    private Simulation simulation;

    void Start()
    {
        agents = new List<Agent>();
        simulation = new Simulation();
        simulation.InitializeAgents(agents);
        simulation.StartSimulation();
    }
}

[System.Serializable]
public class Agent
{
    public float positionX;
    public float positionY;
    public float health;
    public float fitness;
    public NeuralNetwork brain;
}

public class Simulation
{
    public void InitializeAgents(List<Agent> agents)
    {
        // Initialize agents with random positions and brains
        for (int i = 0; i < 10; i++)
        {
            agents.Add(new Agent
            {
                positionX = Random.Range(-10f, 10f),
                positionY = Random.Range(-10f, 10f),
                health = 100f,
                fitness = 0f,
                brain = new NeuralNetwork(2, 3, 1)
            });
        }
    }

    public void StartSimulation()
    {
        // Start the simulation loop
        while (true)
        {
            foreach (var agent in agents)
            {
                // Update agent position and health based on brain output
                agent.positionX += agent.brain.Output(new float[] { agent.positionX, agent.positionY })[0] * 0.1f;
                agent.positionY += agent.brain.Output(new float[] { agent.positionX, agent.positionY })[1] * 0.1f;

                // Simple health decay
                agent.health -= 0.1f;

                // Check for agent death
                if (agent.health <= 0f)
                {
                    agents.Remove(agent);
                }
            }
        }
    }
}

public class NeuralNetwork
{
    public float[] Output(float[] inputs)
    {
        // Simple linear output for demonstration
        return new float[] { inputs[0], inputs[1] };
    }
}