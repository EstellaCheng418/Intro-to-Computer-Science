package locklear.MAIN;

import java.io.IOException;
import java.util.Arrays;

import lockear.ASSEMBLER.MemoryBuilder;
import locklear.ENUMS.*;
import locklear.MEMORY.*;


public class Gene {

	public static void main(String[] args) throws InterruptedException {
		//Testing Suite
		MemoryBuilder MB = new MemoryBuilder("Gene1");
		MB.buildMemory();
		MemoryBank mBank = new MemoryBank("Bank_1",MB);
		//Task 1 Display Memory
		System.out.println("***TASK 1***");
		mBank.display();
		//Task 2 Flush Memory
		System.out.println("***TASK 2***");
		mBank.flush();
		//Task 3 Dump Memory
		System.out.println("***TASK 3***");
		MemoryBuilder MB2 = new MemoryBuilder("Gene2");
		MB2.buildMemory();
		MemoryBank mBank2 = new MemoryBank("Bank_2",MB2);
		Memory[] m = mBank2.dump();
		System.out.println("Contains " + m.length + " Memory Objects");
		//Task 4 Replicate Memory
		System.out.println("***TASK 4***");
		mBank2.replicate();		
		//Task 5 Reorder Memory
		System.out.println("***TASK 5***");
		mBank2.display();
		mBank2.reorder(Flags.STATUS);
		System.out.println();
		mBank2.display();
		//Task 6 Display Sector
		System.out.println("***TASK 6***");
		mBank2.displaySector(Sector.Alpha);
		//Task 7 Return Memory
		System.out.println("***TASK 7***");
		mBank2.returnMemory("Mloc_0");			
		//Task 8 Swap Memory
		System.out.println("***TASK 8***");
		mBank2.display();
		mBank2.swapMemory("Mloc_1", "Mloc_7");
		System.out.println();
		mBank2.display();
		//Task 9 Swap Sectors
		System.out.println("***TASK 9***");		
		Memory[] m9 = mBank2.getSector(Sector.Alpha);
		System.out.println(Arrays.toString(m9));
		//Task 10 Insert Memory
		System.out.println("***TASK 10***");
		mBank.clear();
		mBank.display();
		mBank.insertMemory(new Memory("abc_1234",
				"10110_22",Status.Intact));
		mBank.display();
		System.out.println();
		MemoryBuilder MB3 = new MemoryBuilder("Gene3");
		MB3.buildMemory();
		MemoryBank mBank_3 = new MemoryBank("Bank_3",MB3);	
		mBank_3.insertMemory(new Memory("abc_1234",
				"10110_22",Status.Intact));		
		//Task 11 Insert Cache
		System.out.println("***TASK 11***");
		MemoryBank mbEmpty = new MemoryBank();
		mbEmpty.display();
		mbEmpty.setBankID("Bank_2");
		Memory[] mb = {new Memory("abc_1234","10110_22",Status.Intact),
				new Memory("bbc_2234","10110_22",Status.Corrupted),
				new Memory("abc_3234","10110_22",Status.Intact)};
		mbEmpty.insertCache(mb);
		mbEmpty.display();
		//Task 12 Remove Memory
		System.out.println("***TASK 12***");
		mBank2.updateMemory("Mloc_3", "10110_22");
		//Task 13 Validate Memory
		System.out.println("***TASK 13***");
		String[] addr = {"Mloc_1","Mloc_5"};
		mBank2.validateMemory(addr);
		//Task 14 Persist Memory
		System.out.println("***TASK 14***");
		try {
			mBank2.persistMemory("Mem_Locker");
		} catch (IOException e) {
			System.out.println("Method Failure");
			e.printStackTrace();
		}
		
		//Task 15 Constitute Memory
		System.out.println("***TASK 15***");
		
		try {
			mBank2.constituteMemory("Mem_Locker");
		} catch (IOException e) {
			System.out.println("Method Failure");
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			System.out.println("System Failure");
			e.printStackTrace();
		}
		
		//Task 16 Compare Memory Banks
		System.out.println("***TASK 16***");
		MemoryBuilder MB4 = new MemoryBuilder("Gene4");
		MB4.buildMemory();
		MemoryBank mBank_4 = new MemoryBank("Bank_4",MB4);
		mBank_4.compareBanks(mBank_3);
		System.out.println();
		mBank_4.compareBanks(mBank_4);
		//Task 17 Repair Memory
		System.out.println("***TASK 17***");
		mBank_4.repairMemory();
	}

}
