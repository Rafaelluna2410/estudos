package algoritmos;

public class BinarySearchTree implements BinaryTree {

	
	private Node root;
	
	public void add(int value) {
		
		
		this.root= internalAdd(value, this.root);
		
	}
	
	private Node internalAdd(int value, Node node) {
		if (node == null) {
			 return new Node(value);
		} else if (value < node.getValue()) {
			node.setLeft(internalAdd(value, node.getLeft()));
		} else if (value > node.getValue()) {
			node.setRight(internalAdd(value, node.getRight()));
		}
		
		return node;
	}
	


	public boolean contains(int element) {
	
		return false;
	}

	public void remove() {

		
	}

	
	public void preOrderTraversal() {

		preOrderInternal(this.root);
	}
	
	private void preOrderInternal(Node node) {
		if(node !=null) {
		System.out.print(node.getValue()+ " ");
		preOrderInternal(node.getLeft());
		preOrderInternal(node.getRight());
		
		}
	}
	
	public void inOrderTraversal() {
		
		inOrderInternal(this.root);
		
	}
	
	private void inOrderInternal(Node node) {
		
		if(node !=null) {
		inOrderInternal(node.getLeft());
		System.out.print(node.getValue() + " ");
		inOrderInternal(node.getRight());
		}
	}

	
	public void postOrderTraversal() {
		postOrderInternal(this.root);
	
	}
	
	private void postOrderInternal(Node node) {
		if(node !=null) {
		postOrderInternal(node.getLeft());
		postOrderInternal(node.getRight());
		System.out.print(node.getValue() + " ");
		}
	}
	
	
	private class Node{
		
		private Node left;
		private Node right;
		private int value;
		
		public Node(int value) {
			this.value = value;
		}

		public Node getLeft() {
			return left;
		}

		public void setLeft(Node left) {
			this.left = left;
		}

		public Node getRight() {
			return right;
		}

		public void setRight(Node right) {
			this.right = right;
		}

		public int getValue() {
			return value;
		}

		public void setValue(int value) {
			this.value = value;
		}
		
			
	}

}
