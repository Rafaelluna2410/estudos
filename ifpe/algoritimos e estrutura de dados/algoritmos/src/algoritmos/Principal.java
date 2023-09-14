package algoritmos;

import java.util.*;

public class Principal {

	public static void main(String[] args) {
	listCircle novo = new listCircle();
	Scanner leitor = new Scanner(System.in);
	int teste;
	
	novo.add(10);
	novo.add(20);
	novo.add(30);
	novo.add(40);
	novo.add(50);
	novo.add(60);
	
	novo.swap(1, 2);
	
	for(int i =0; i < novo.getSize(); i++) {
		
		
		System.out.println(novo.getValue(i));
	}
	
	
	
	
	}

}
