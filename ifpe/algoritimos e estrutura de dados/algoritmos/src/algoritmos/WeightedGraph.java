package algoritmos;

public class WeightedGraph {

    private int[][] adjacencyMatrix;
    private int numVertices;
    private boolean isDirected;

    public WeightedGraph(int numVertices, boolean isDirected) {
        this.numVertices = numVertices;
        this.isDirected = isDirected;
        this.adjacencyMatrix = new int[numVertices][numVertices];
    }

    public void addEdge(int source, int destination, int weight) {
        adjacencyMatrix[source][destination] = weight;

        if (!isDirected) {
            adjacencyMatrix[destination][source] = weight;
        }
    }

    public void removeEdge(int source, int destination) {
        adjacencyMatrix[source][destination] = 0;

        if (!isDirected) {
            adjacencyMatrix[destination][source] = 0;
        }
    }

    public void addOrUpdateEdge(int source, int destination, int weight) {
        if (hasEdge(source, destination)) {
            adjacencyMatrix[source][destination] = weight;

            if (!isDirected) {
                adjacencyMatrix[destination][source] = weight;
            }
        } else {
            addEdge(source, destination, weight);
        }
    }

    public String getGraphRepresentation() {
        StringBuilder graphRepresentation = new StringBuilder();

        for (int i = 0; i < numVertices; i++) {
            for (int j = 0; j < numVertices; j++) {
                graphRepresentation.append(adjacencyMatrix[i][j]).append(" ");
            }
            graphRepresentation.append("\n");
        }

        return graphRepresentation.toString();
    }

    public int getEdgeWeight(int source, int destination) {
        return adjacencyMatrix[source][destination];
    }

    public boolean hasEdge(int source, int destination) {
        return adjacencyMatrix[source][destination] != 0;
    }

    public boolean isDirected() {
        return isDirected;
    }

    public static void main(String[] args) {
        WeightedGraph graph = new WeightedGraph(4, false);

        graph.addEdge(0, 1, 2);
        graph.addEdge(0, 2, 4);
        graph.addEdge(1, 3, 1);
        System.out.println("Original Graph:");
        System.out.println(graph.getGraphRepresentation());

        // Removing edge between 0 and 1
        graph.removeEdge(0, 1);
        System.out.println("Graph after removing edge between 0 and 1:");
        System.out.println(graph.getGraphRepresentation());

        // Adding or updating edge between 1 and 3
        graph.addOrUpdateEdge(1, 3, 5);
        System.out.println("Graph after adding or updating edge between 1 and 3:");
        System.out.println(graph.getGraphRepresentation());
    }
}

