import java.util.Scanner;
import java.lang.Math; 

public class Solution{
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args){
        int T=sc.nextInt();
        for(int t=0;t<T;t++){
            float radius=sc.nextFloat();
            float area=(float)Math.PI*(float)Math.pow(radius, 2);
            // System.out.print("Case "+t+": "+String.format("%.3f", area));
            System.out.print(String.format("Case %d: %.3f\n",t, area));
        }
	}
}