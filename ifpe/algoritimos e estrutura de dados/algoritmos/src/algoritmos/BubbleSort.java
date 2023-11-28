package algoritmos;

public class BubbleSort {
	
	private int[] array;
	
	public BubbleSort(int[]array) {
	boolean flag = true;
	while(flag) {
		
		flag = false;
		for (int i = 0; i < array.length-1; i++) {
			
			if(array[i] > array[i+1]) {
			int aux = array[i];
			array[i] = array[i + 1];
            array[i+1]= aux;
			flag = true;			
			}	
			}			
		}
	this.array = array;
	}		
	public int[] getArray(){
		
		return this.array;
	}
	public static void main(String [] args) {	
	int[] teste = {25,30,5,8,9,4,6,50,11,33};
	BubbleSort novo = new BubbleSort(teste);		
	for(int i : novo.getArray()) {
		System.out.println(i);	
				
		}	
	}
}


