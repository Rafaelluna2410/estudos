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
		
		return internalContains(element, this.root);
	}
	
	public boolean internalContains(int element, Node node) {
		
		if(node !=null) {
		if(element == node.getValue()) {
			return true;
		}else if(element < node.getValue()) {			
			return internalContains(element, node.getLeft());
		}else{		
			return internalContains(element, node.getRight());		
		}
		}
		
		return false;
	}
	
	
	public void remove(int element) {

		this.root = internalRemove(element, this.root);
	}
	
	private Node internalRemove(int element, Node node) {
		if (node != null) {
			if (element == node.getValue()) {
				if (node.getLeft() == null && node.getRight() == null) {
					return null;
				} else if (node.getLeft() != null && node.getRight() != null) {
					Node teste = node.getLeft();
					while (teste.getRight() != null) {
						teste = teste.getRight();
					}
					node.setValue(teste.getValue());
					node.setLeft(internalRemove(node.getValue(), node.getLeft()));
					return node;
				} else {
					return node.getRight() == null ? node.getLeft() : node.getRight();
				}
			} else if (element < node.getValue()) {
				node.setLeft(internalRemove(element, node.getLeft()));
			} else {
				node.setRight(internalRemove(element, node.getRight()));
			}
		}
		
		return node;
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
