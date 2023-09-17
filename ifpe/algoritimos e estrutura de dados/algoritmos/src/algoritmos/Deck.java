package algoritmos;

public class Deck implements Deque {

	private Node top;
	private Node base;
	private int size;
	
	
	@Override
	public void addFirst(int element) {
		if(this.top ==null) {
			Node node = new Node(element);
			this.top = node;
			this.base = this.top;
			
		}else {
			Node node = new Node(element);
			node.setDown(this.top);
			this.top.setTop(node);
			this.top =node;
		}
		
		
		
		this.size++;
		
	}

	@Override
	public void addLast(int element) {
		if(this.base==null) {
			Node node = new Node(element);
			this.top = node;
			this.base = this.top;
			
		}else {
			Node node = new Node(element);
			node.setTop(this.base);
			this.base.setDown(node);
			this.base = node;
		}
		this.size++;
	}

	@Override
	public int removeFirst() {
		if(this.top == null) {
			throw new RuntimeException("empty");
			
		}else {
			
			this.top=  this.top.getDown();
			this.top.setTop(null);
			this.size--;
			return this.top.getValue();
			
			
			
		}
		
	}

	@Override
	public int removeLast() {
		if(this.base==null) {
			throw new RuntimeException("empty");
			
		}else {
			
			this.base = this.base.getTop();
			this.base.setDown(null);
			
			this.size--;
			return this.base.getValue();
		}
		
	
	}

	@Override
	public int getFirst() {
		// TODO Auto-generated method stub
		return this.top.getValue();
	}

	@Override
	public int getLast() {
		// TODO Auto-generated method stub
		return this.base.getValue();
	}

	@Override
	public int size() {
		
		return this.size;
	}

	
	private class Node{
		
		public Node getTop() {
			return top;
		}


		public void setTop(Node top) {
			this.top = top;
		}


		public Node getDown() {
			return down;
		}


		public void setDown(Node down) {
			this.down = down;
		}


		public int getValue() {
			return value;
		}


		public void setValue(int value) {
			this.value = value;
		}


		private Node top;
		private Node down;
		private int value;
		
		
		public Node(int element) {
			this.value = element;
			
		}
		
		
		
		
		
		
		
		
		
	}
	
	
	
}
