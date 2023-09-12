package algoritmos;

public class Principal {

	public static void main(String[] args) {
	linkeList novo = new linkeList();
	
	novo.addValue(10);
	novo.addValue(20);
	novo.addValue(30);
	novo.addValue(40);
	
	novo.remove(2);
	for (int i = 0; i < novo.getSize(); i++) {
		
	System.out.println(novo.getValue(i));
	}
	
	
	}

}
