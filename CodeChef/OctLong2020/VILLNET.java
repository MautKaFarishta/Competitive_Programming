/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner sc=new Scanner(System.in);
	    // your code goes here
	    try{
	        int t = sc.nextInt();
	        while(t-->0){
	            long x1=sc.nextLong();
	            long y1=sc.nextLong();
	            long x2=sc.nextLong();
	            long y2=sc.nextLong();
	            
	            HashMap<String,Boolean>map=new HashMap<>();
	            
	            if(x1>-10&&x2>-10&&x1<10&&x2<10&&y1>0&&y2>0&&y1<10&&y2<10){
	                System.out.println(solve1(x1,y1,x2,y2,0,map));
	            }else{
	                System.out.println(solve(x1,y1,x2,y2,0,map));
	            }
	            
	        }
	    }catch(Exception e){
	        return;
	    }
	}
	static int mod=(int)1e9+7;
	static int solve(long x1,long y1,long fx,long fy,int counts,HashMap<String,Boolean> map){
	    if (counts>6){
	        return Integer.MAX_VALUE;
	    }
	    if (x1==fx && y1==fy){
	        return counts;
	    }
	    if (map.containsKey(x1 + "" + y1))
	      if (map.get(x1+""+y1)==true){
	          return Integer.MAX_VALUE;
	      }
	    map.put(x1 + "" + y1,true);
	    int d1 =solve(x1+2*y1,y1,fx,fy,counts+1,map);
	    int d2 =solve(x1-2*y1,y1,fx,fy,counts+1,map);
	    int d3=Integer.MAX_VALUE,d4=Integer.MAX_VALUE;
	    if (2* x1 +y1>0){
	        d3=solve(x1,y1+2*x1,fx,fy,counts+1,map);
	    }
	    else if (2* x1 +y1<0){
	        d3=solve(-x1,-y1-2*x1,fx,fy,counts+1,map);
	    }
	    if (-2 * x1 +y1 >0)
	        d4 =solve(x1,y1-2*x1,fx,fy,counts+1,map);
	    else if (-2 * x1 +y1 <0)
	        d4 =solve(-x1,-y1+2*x1,fx,fy,counts+1,map);
	    map.put(x1 + "" + y1,!map.get(x1 + "" + y1));
	    
	    return Math.min(d1,Math.min(d2,Math.min(d3,d4)));
	}
	static int solve1(long x1 ,long y1 ,long fx ,long fy , int counts ,HashMap<String,Boolean> map){
	    if ((x1>=10) || (x1<=-10) || (y1<=0) || (y1>=10)){
	        return Integer.MAX_VALUE;
	    }
	    if (x1==fx&&y1==fy){
	        return counts;
	    }
	    if (map.containsKey(x1+""+y1))
	        if (map.get(x1 + "" + y1)==true){
	            return Integer.MAX_VALUE;
	        }
	    map.put(x1+""+y1,true);
	    int d1=solve1(x1+2*y1,y1,fx,fy,counts+1,map);
	    int d2=solve1(x1-2*y1,y1,fx,fy,counts+1,map);
	    int d3 = Integer.MAX_VALUE,d4 = Integer.MAX_VALUE;
	    if (2*x1+y1>0){
	        d3=solve1(x1,y1+2*x1,fx,fy,counts+1,map);
	    }
	    else if (2*x1+y1<0){
	        d3=solve1(-x1,-y1-2*x1,fx,fy,counts+1,map);
	    }
	    if (-2*x1+y1>0){
	        d4=solve1(x1,y1-2*x1,fx,fy,counts+1,map);
	    }
	    else if (-2*x1+y1<0){
	        d4=solve1(-x1,-y1+2*x1,fx,fy,counts+1,map);
	    }
	    map.put(x1+ "" + y1,!map.get(x1+""+y1));
	    
	    return Math.min(d1,Math.min(d2,Math.min(d3,d4)));
	}
 }
// // Java program to illustrate 
// // Java.util.HashMap 
  
// import java.util.HashMap; 
  
// public class GFG { 
//     public static void main(String[] args) 
//     { 
//         // Create an empty hash map 
//         HashMap<String, Integer> map 
//             = new HashMap<>(); 
  
//         // Add elements to the map 
//         map.put("vishal", 10); 
//         map.put("sachin", 30); 
//         map.put("vaibhav", 20); 
  
//         // Print size and content 
//         System.out.println("Size of map is:- "
//                            + map.size()); 
//         System.out.println(map); 
  
//         // Check if a key is present and if 
//         // present, print value 
//         if (map.containsKey("vishal")) { 
//             Integer a = map.get("vishal"); 
//             System.out.println("value for key"
//                                + " \"vishal\" is:- "
//                                + a); 
//         } 
// Java program to illustrate 
// Java.util.HashMap 
  
// import java.util.HashMap; 
// import java.util.Map; 
  
// public class GFG { 
//     public static void main(String[] args) 
//     { 
//         HashMap<String, Integer> map = new HashMap<>(); 
  
//         map.put("vishal", 10); 
//         map.put("sachin", 30); 
//         map.put("vaibhav", 20); 
  
//         for (Map.Entry<String, Integer> e : map.entrySet()) 
//             System.out.println(e.getKey() + " " + e.getValue()); 
//     } 
// } 
// import java.util.HashMap;
// import java.util.Map;
// import java.util.Iterator;
// import java.util.Set;
// public class Details {

//    public static void main(String args[]) {

//       /* This is how to declare HashMap */
//       HashMap<Integer, String> hmap = new HashMap<Integer, String>();

//       /*Adding elements to HashMap*/
//       hmap.put(12, "Chaitanya");
//       hmap.put(2, "Rahul");
//       hmap.put(7, "Singh");
//       hmap.put(49, "Ajeet");
//       hmap.put(3, "Anuj");

//       /* Display content using Iterator*/
//       Set set = hmap.entrySet();
//       Iterator iterator = set.iterator();
//       while(iterator.hasNext()) {
//          Map.Entry mentry = (Map.Entry)iterator.next();
//          System.out.print("key is: "+ mentry.getKey() + " & Value is: ");
//          System.out.println(mentry.getValue());
//       }

//       /* Get values based on key*/
//       String var= hmap.get(2);
//       System.out.println("Value at index 2 is: "+var);

//       /* Remove values based on key*/
//       hmap.remove(3);
//       System.out.println("Map key and values after removal:");
//       Set set2 = hmap.entrySet();
//       Iterator iterator2 = set2.iterator();
//       while(iterator2.hasNext()) {
//           Map.Entry mentry2 = (Map.Entry)iterator2.next();
//           System.out.print("Key is: "+mentry2.getKey() + " & Value is: ");
//           System.out.println(mentry2.getValue());
//        }

//    }
// }
