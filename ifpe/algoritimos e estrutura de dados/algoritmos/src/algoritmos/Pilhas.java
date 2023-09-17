package algoritmos;

public class Pilhas implements Stack{
	
	private Node top;
	private int size;

	
	@Override
	public void push(String element) {
		
		if(this.top == null) {
			Node node = new Node(element);
			this.top = node;
			
		}else {
			Node newNode =new Node(element);
			newNode.setDown(this.top);
			this.top = newNode;
			
			
		}
		this.size++;
		
	}
	
	@Override
	public String peek() {
		if(this.top ==null) {
			
		throw new RuntimeException("Empty");
			
			
		}else {
			
			
		return this.top.getValue();	
		}
		
		
		
	
	}
	
	@Override
	public String pop() {
		if(this.top ==null) {
			throw new RuntimeException("Empty");
		}else {
			
		Node oldNode = this.top;
		this.top = this.top.getDown();
		this.size--;
		
			return oldNode.getValue();
			
		}
		
		
		
	}

	@Override
	public int getSize() {
		// TODO Auto-generated method stub
		return this.size;
	}
	
	
	private class Node{
		
	
		private String value;
		private Node down;
		
		public Node(String value) {
			this.value = value;
			
		}
		
		public Node getDown() {
			return down;
		}
		
		public void setDown(Node down) {
			this.down = down;
		}
		
		public String getValue() {
			return value;
		}
		
		public void setValue(String value) {
			this.value = value;
		}
		
				
	}

}
