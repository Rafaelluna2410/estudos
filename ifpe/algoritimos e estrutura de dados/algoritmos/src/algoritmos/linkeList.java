package algoritmos;

public class linkeList {

	private Node head;
	private Node tail;
	private int size;
	
	public void addValue(int value) {
		if(head == null) {
			this.head = new Node(value);
			this.tail = this.head;
			
		}else {
		
		Node node = new Node(value);
		this.tail.setNode(node);
		this.tail = node;
		}
		
		this.size++;
		
		
	}
	
	public void addValue(int value, int index) {
		Node current = this.head;
		int currentIndex = 0;
		
		for(current.getValue(); current != null; current =  current.getNode()) {
			if(index == currentIndex) {
				
				current.setValue(value);
			}
			currentIndex++;
		}
	
		
	}
	
	public int getSize() {
		return this.size;
	}
	
	
	public int getValue(int index) {
		Node current = this.head;
		for(int i =0; i< this.getSize(); i++) {
			
			if(i==index) {
				return current.getValue();
			}
			
			current = current.getNode();
		}
		
		throw new RuntimeException("invalid");
	}
	
	public void remove(int index) {
		Node currentNode = this.head;
		
		for (int i = 0; i < this.getSize(); i++) {
			if(i == index-1) {
				
				currentNode.setNode(currentNode.getNode().getNode());
			}else {
				
				currentNode = currentNode.getNode();
			}
		}
		
		this.size--;
	}
	
	
	private class Node{
		
	private Node next;
	private int value;
		
	public Node(int value) {
		this.value = value;
	}
	
	
	
	public int getValue() {
		
		return value;
	}
	
	public void setValue(int value) {
		
		this.value = value;
	}
	
	
	public Node getNode() {
		return this.next;
	}
	
	public void setNode(Node node) {
			this.next = node;
	}
	
	
	
	}
}
