using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Numerics.BigInteger

namespace ProjectEuler{
	public static class Fibonacci{
		public static Dictionary<int,BigInteger> calc_fib(int limit_){
			Dictionary<int,BigInteger> mem=new Dictionary<int,BigInteger>();
			for (int i=1;i<(limit_+1);i++){
				if (i<=2){
					try{
						mem.Add(i,1);
					}catch(Exception e){
						Console.WriteLine(e.Message);
					}
				}else{
					mem[x]=mem[x-1]+mem[x-2];
				}
			}
			return mem;
		}
		public static BigInteger extract(Dictionary<int,BigInteger> mem_){
			var mem_val=mem_.Values.ToList();
			BigInteger sum_=0;
			foreach(BigInteger val in mem_val){
				if (val<=4000000 && val%2==0){
					sum_+=val;
				}
			}
			return sum_;
		}
	}
	public class Programe{
		Stopwatch clock = Stopwatch.StartNew();
		Dictionary<int,BigInteger> fib_= Fibonacci.calc_fib(100);
		BigInteger extract_=Fibonacci.extract(fib_);
		Console.WriteLine(extract_);
		Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
	}
}