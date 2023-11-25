package algoritmos;


public class HashTables {
	
	
	private HashTableEntry[] table;
	private int size;
	
	public HashTables(){
		this.table = new HashTableEntry[10];
		this.size = 0;	
		
	}
	
	public String get(String key) {
		
		int hashCode = Math.abs(key.hashCode());
		int index = hashCode % this.table.length;
		
		HashTableEntry currentEntry = this.table[index];
		
		while(currentEntry != null) {
			 if(currentEntry.key.equals(key)) {
				 return currentEntry.value;
			 }
			 index++;
			 if(index >= table.length) {
				 index=0;
			 }
			 
			 currentEntry = this.table[index];
			 
		}
		
		throw new RuntimeException("fail");
	}
	
	public void add(String key, String value) {
		int hashCode =Math.abs(key.hashCode());
		int index = hashCode % this.table.length;
		System.out.println("Key " + key + "Index: "+index );
		
		HashTableEntry currentEntry = this.table[index];
		while(currentEntry != null) {
			index++;
			if(index> this.table.length) {
				index=0;
			}
			currentEntry = this.table[index];
		}
		this.table[index]= new HashTableEntry(key, value);
		this.size++;
	}
	
	private class HashTableEntry{
		String key;
		String value;
		
	public HashTableEntry(String key, String value) {
			this.key = key;
			this.value = value;	
			
		}
	
	}
}
