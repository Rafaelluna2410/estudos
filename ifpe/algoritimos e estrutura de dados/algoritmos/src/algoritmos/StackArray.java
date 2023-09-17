package algoritmos;

import java.util.ArrayList;

public class StackArray implements Stack {

	private int size = 0;
	public Node[] array = new Node[this.size];

	  @Override 
	  public void push(String element) {
	 
	 Node node = new Node(element); 
	 Node[] novo = new Node[this.size+1];
	  
	 for(int i=0; i< this.size; i++) {
	 
	  novo[i] = this.array[i];
	 
	  } 
	  novo[this.size] = node; 
	  this.size++; 
	  this.array = novo;
	  
	  
//	  Node[] reverse = new Node[this.size];
//		 
//	  for(int i =0; i<this.size; i++){
//	  
//	  reverse[i] = this.array[this.size -i-1];
//  
//	  } 
//	  this.array = reverse;
//	  
	
	 }
	  
	  
	  public void reverse() {
		  
		  Node[] reverse = new Node[this.size];			 
		  for(int i =0; i<this.size; i++){		  
		  reverse[i] = this.array[this.size -i-1];
	  
		  } 
		  this.array = reverse;
	  }
    

	@Override
	public String peek() {

		return array[0].getValue();
	}

	@Override
	public String pop() {
		if (array[0] == null) {
			throw new RuntimeException("Empty");

		} else {

			String oldValue = array[0].getValue();

			Node[] newArray = new Node[this.size - 1];
			for (int i = 0; i < this.size - 1; i++) {
				newArray[i] = array[i + 1];

			}

			this.size = array.length - 1;

			array = newArray;

			return oldValue;

		}

	}

	@Override
	public int getSize() {

		return this.size;
	}

	public class Node {

		private Node down;
		private String value;

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
