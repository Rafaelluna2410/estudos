package algoritmos;



public class ListCircle {

	
	private Node head;
	private Node tail;
	private int size;
	
	
public void add(int value) {

		if(this.head == null) {
		this.head = new Node(value);	
		this.tail = this.head;	
		}else {
		
		Node node = new Node(value);
		
		node.previos = this.tail;
		this.tail.setNext(node);
		this.tail = node;
		this.tail.setNext(this.head);
		this.head.setPrevios(this.tail);
		}
		
		this.size++;
		
}
		

public void add(int value, int index) {
	int currentIndex=0 ;
	Node currentNode = this.head;

	for(currentNode.getValue(); currentNode.getNext() != this.head; currentNode = currentNode.getNext()) {
		
		if(currentIndex == index){
			
			currentNode.setValue(value);
			
		}
		
		currentIndex++;
		
	}
}


public int getSize() {
	
	
	return this.size;
}



public void addSorte(int value) {
	
	Node novo = new Node(value);
	Node current = this.head;
	
	
	while(current.getNext() !=null) {
		
		if(value < current.getValue()) {
			
			novo.setNext(current);
			novo.setPrevios(current.getPrevios());
			current.getPrevios().setNext(novo);
			break;
		}
		current = current.getNext();
		
	}
	
	this.size++;
	
}

public void swap(int one, int two) {

	Node indexOne = null;
	Node indexTwo = null;
	int index=0;
	Node current = this.head;
	
	for(int i =0; i < this.size; i++) {
	
		if(one == index) {
			
			indexOne = current;
			
		}else if (two == index){
			
			indexTwo = current;
		}	
		
	index++;
	current = current.getNext();
		
	}
	
	int aux = indexTwo.getValue();
	indexTwo.setValue(indexOne.getValue());
	indexOne.setValue(aux);
	
	
}


public void reverse() {
	
	Node first = this.head;
	Node last = this.tail;
	
	int aux;
	
	for(int i=0; i < this.size/2 ; i++) {
		
		aux = last.getValue();
		last.setValue(first.getValue());
		first.setValue(aux);
		
		
		first = first.getNext();
		last = last.getPrevios();
		
	}

}



public void remove(int index) {
	Node currentNode = this.head;
	
	for(int i =0; i< this.getSize(); i++) {
		
		if(i ==index-1) {
			
			currentNode.setNext(currentNode.getNext().getNext());
			currentNode.getNext().setPrevios(currentNode);
			
		}else {
			
			currentNode = currentNode.getNext();
		}
				
	}
	
	this.size--;
	
}

public int getValue(int index) {
	Node node = this.head;
	
	for(int i=0; i < this.getSize(); i++) {
	if(i == index) {
		return node.getValue();
		
	}	
		
		node = node.getNext();
	}
	
	throw new RuntimeException("index invalid");
	
	
}

private class Node{
	
	private int value;
	private Node next;
	private Node previos;
	
	
	public Node(int value) {
		
		this.value = value;
	}
		
	
	public void setValue(int value) {
		
		this.value = value;
	}
	
	public int getValue() {
		
		return this.value;
	}
		
	public void setNext(Node node) {
		
		
		this.next = node;
	}
	
	public Node getNext() {
		
		return this.next;
	}
	
	public void setPrevios(Node node) {
		
		
		this.previos = node;
	}
	
	
	public Node getPrevios() {
			
	return this.previos;
	}
	
		
	}
	
}
