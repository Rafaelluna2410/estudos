package algoritmos;

public class listCircle {

	
	private Node head;
	private Node tail;
	private int size;
	
	
public void addValue(int value) {

		if(this.head == null) {
		this.head = new Node(value);	
		this.tail = this.head;	
		}
		
		Node node = new Node(value);
		
		node.previos = this.tail;
		this.tail.setNext(node);
		this.tail = node;
		this.tail.setNext(this.head);
		this.head.setPrevios(this.tail);
		
		this.size++;
		
}
		

public void addValue(int value, int index) {
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


public void removeValue(int index) {
	Node currentNode = this.head;
	
	for(int i =0; i< this.getSize(); i++) {
		
		if(i ==index-1) {
			
			currentNode.setNext(currentNode.getNext().getNext());
			currentNode.getNext().setNext(currentNode);
			
		}else {
			
			currentNode = currentNode.getNext();
		}
		
		this.size--;
		
	}
	
	
	
}



private class Node{
	
	private int value;
	private Node next;
	private Node previos;
	
	
	public Node(int value) {
		
		this.value = value;
	}
		
	
	public void setValue(int value) {
		
		this.setValue(value);
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
