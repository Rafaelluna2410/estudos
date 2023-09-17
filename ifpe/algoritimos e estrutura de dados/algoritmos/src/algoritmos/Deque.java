package algoritmos;

public interface Deque {


	    // Adiciona um elemento no início do deque.
	    void addFirst(int element);

	    // Adiciona um elemento no final do deque.
	    void addLast(int element);

	    // Remove e retorna o elemento do início do deque. Retorna null se o deque estiver vazio.
	    int removeFirst();

	    // Remove e retorna o elemento do final do deque. Retorna null se o deque estiver vazio.
	    int removeLast();

	    // Retorna o elemento do início do deque sem removê-lo. Retorna null se o deque estiver vazio.
	    int getFirst();

	    // Retorna o elemento do final do deque sem removê-lo. Retorna null se o deque estiver vazio.
	    int getLast();

	    // Retorna o número de elementos no deque.
	    int size();


}
