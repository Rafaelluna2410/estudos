package algoritmos;

public interface filas {

//	Adiciona um elemento atrás da fila
	public void offer(String element);
	
//	Obtém o elemento da frente, sem retirá-lo
	public String peek();
	
//	Obtém o elemento da frente e retira-o
	public String poll();
		
//	Obtém o tamanho da fila
	public int getSize();
	
	
}
