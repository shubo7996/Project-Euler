using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Numerics;

namespace ProjectEuler
{
    class euler119
    {
        public static void Main()
        {
            List<BigInteger> power_list = new List<BigInteger>();
            BigInteger val;
            BigInteger sum_;
            for (int x=9; x < 100; x++)
            {
                val = 1;
                for (int _ = 2; _ < x / 2; _++)
                {
                    val *= x;
                    sum_ = val.ToString().Sum(c => c - '0');
                    if (sum_ == x)
                    {
                        power_list.Add(val);
                    }
                }
                if (power_list.Count == 50)
                {
                    break;
                }
            }
            Console.WriteLine(power_list[28]);                           
            Console.ReadKey();
        }
    }
}
