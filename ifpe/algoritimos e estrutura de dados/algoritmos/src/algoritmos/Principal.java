package algoritmos;

import java.util.*;

public class Principal {

	public static void main(String[] args) {
		/*
		 * ListCircle novo = new ListCircle(); Scanner leitor = new Scanner(System.in);
		 * int teste;
		 * 
		 * novo.add(10); novo.add(20); novo.add(30); novo.add(40); novo.add(50);
		 * novo.add(60);
		 * 
		 * novo.swap(1, 2);
		 * 
		 * for(int i =0; i < novo.getSize(); i++) {
		 * 
		 * 
		 * System.out.println(novo.getValue(i)); }
		 */
	
/*	Pilhas novo = new Pilhas();
	
	novo.push(10);
	novo.push(20);
	novo.push(30);
	novo.pop();
	
	System.out.print(novo.peek());
	
	
	
	
	}*/
		
/*
 * Queue nova = new Queue();
 * 
 * nova.offer(10); nova.offer(20); nova.offer(30); nova.offer(40);
 * 
 * System.out.print(nova.poll()); System.out.print(nova.poll());
 * System.out.print(nova.poll());
 */
//
//		StackArray nova  = new StackArray();
//		
//		nova.push(10);
//		nova.push(20);
//		nova.push(30);
//		nova.push(40);
//		nova.push(50);
//		nova.push(60);
//	
//		
//	nova.reverse();
//		
//			for(int i=0;  i < nova.getSize(); i++) {
//				
//				System.out.print(nova.array[i].getValue());
//			}
//			
//			
//		Deck deck = new Deck();
//		deck.addFirst(10);
//		deck.addFirst(20);
//		deck.addFirst(30);
//		deck.addFirst(40);
//		
//		deck.removeFirst();
//		deck.removeLast();
//		System.out.print(deck.getFirst()+" " +deck.getLast());
		
	
//		Pilhas s = new Pilhas();
//		s.push("i");
//		s.push("s");
//		String ch1 = s.pop(); s.pop();
//		s.push(" d");
//		String ch2 = s.peek();
//		
//		
//		System.out.print(ch2 +" " + ch1);
//		
		
//		Queue teste = new Queue();
//		
//		teste.offer("Hello");
//		teste.offer("Bye");
//		System.out.println(teste.peek());
//		teste.poll();
//		teste.offer("Welcome");
//		if (teste.getSize() > 0) {
//		System.out.println(teste.poll() + ", new size is " + teste.getSize());
//		
//
//}		

		BinaryTree bst = new BinarySearchTree();
		bst.add(10);
		bst.add(5);
		bst.add(3);
		bst.add(8);
		bst.add(17);
		bst.add(13);
		bst.inOrderTraversal();
		bst.remove(3);
		System.out.println(" ");
		bst.inOrderTraversal();
		
	}
}























