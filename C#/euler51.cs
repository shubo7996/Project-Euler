using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace ProjectEuler{

    class euler51{

        const int limit=1_000_000;
        private int[] fillarray(int[] primelist){
            for (int i=0;i<=limit+1;i++){
                primelist[i]=true;
            }
            return primelist;
        }

        public static List<int> generatePrime(){            
            int[] primeList= new int[limit+1];
            euler51.fillarray(primeList);
            List<int> primes=new List<int>();
            int p=2;
            while(p*p<=limit){
                if (primeList[p]==true){
                    int i=p*2;
                    while(i<=limit){
                        primeList[i]=false;
                        i+=p;
                    }
                }
                p+=1;
            }

            for (int i=2;i<limit;i++){
                if(primelist[i]==true){
                    
                }
            }

       } 
    }

}
