package algoritmos;

public interface Stack  {

	
	// Adiciona um elemento no topo
	public void push(String element);
	
	// Obtém o elemento do topo, sem retirá-lo
	public String peek();
	
	// Obtém o elemento do topo e retira-o
	public String pop();

	// Obtém o elemento do topo e retira-o
	public int getSize();
	
	
}
