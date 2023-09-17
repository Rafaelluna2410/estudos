package algoritmos;

public class Queue implements filas{

	private Node tail;
	private Node head;
	private int size;
	
	
	@Override
	public void offer(String element) {
		if(this.tail ==null) {
			Node node  = new Node(element);
			this.tail = node;
			this.head = this.tail;
			
		}else{
			Node node  =  new Node(element);
			this.tail.setNext(node);
			this.tail = node;
		
		}
		
		this.size++;
	}

	@Override
	public String peek() {
		
		return this.head.getValue();
	}

	@Override
	public String poll() {
		if(this.head == null) {
			
			throw new RuntimeException("Empty");
		}else {
			Node oldNode = this.head;
			this.head = this.head.getNext();
			
			this.size--;
			return oldNode.getValue();
			
			
		}
		
	}

	@Override
	public int getSize() {
		
		return this.size;
	}
	
	
	
	private class Node{
		
		private Node next;
		private String value;
		
		public Node(String value) {
			this.value = value;
			
		}

		public Node getNext() {
			return next;
		}

		public void setNext(Node next) {
			this.next = next;
		}

		public String getValue() {
			return value;
		}

		public void setValue(String value) {
			this.value = value;
		}
	
		
	}
	
}
