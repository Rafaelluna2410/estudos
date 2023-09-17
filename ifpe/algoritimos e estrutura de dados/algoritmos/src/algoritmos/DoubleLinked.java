package algoritmos;


public class DoubleLinked {
	
	
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
	
	
	public void addValue(int value, int index) {
		Node current = this.head;
		int indexCurrent = 0;
		
		for(current.getValue(); current != null; current = current.getNext()) {
			if(indexCurrent == index) {
				
				current.setValue(value);
				
			}
			indexCurrent++;
		}
			
		
	}
	
	
		public int getSize() {
			
			return this.size;
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
	
	public void remove(int index) {
		Node current = this.head;
		
		for(int i=0; i< this.getSize(); i++) {
			if(i == index-1) {
				current.setNext(current.getNext().getNext());
				current.getNext().setPrevios(current);
				
			}else {
				
				current = current.getNext();
			}
			
		}
		
		this.size--;
		
		
	}
	
	
	public float indexOf(int value) {
		
		Node current = this.head;
		
		for(int i=0; i< this.size; i++) {
			
			if(current.value ==value) {
				
				return 1;
			
			}
			
			current = current.getNext();
		}
		return -1;

		
	}
	
	
	
	
	private class Node{
		
		private int value;
		private Node next;
		private Node previos;
		
		public Node(int value){
			
			this.value = value;
		}
		
		
	public int getValue() {
		
		return this.value;
	}	
		
	public void setValue(int value) {
		this.value = value;
		
	}
	
	
	public Node getNext() {
		
		return this.next;
	}
	
	public void setNext(Node node) {
		
		this.next = node;
			
	}
	
	public void setPrevios( Node node) {
		
		this.previos = node;
		
	}
	
}

}
