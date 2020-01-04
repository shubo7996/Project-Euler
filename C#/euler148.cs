using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

namespace ProjectEuler
{
    class euler148
    {
        //Analytical formula(Calculates Upto 10^3 Rows)

        //private static int pascalEachRow(int n)
        //{
        //    BigInteger[] row = new BigInteger[n + 1];
        //    row[0] = row[n] = 1;

        //    for (int i = 0; i < n >> 1; i++)
        //    {
        //        BigInteger l = (row[i] * (n - i)) / (i + 1);
        //        row[i + 1] = row[n - i - 1] = l;
        //    }

        //    IEnumerable<BigInteger> div_list = from number in row where number % 7 != 0 select number;
        //    return div_list.Count();
        //}

        //Lucas's Theorem

        //Basic Idea is to convert a row(which is base 10), to the base p (prime)[7 in this case],
        //add 1 to each of the digits and finally multiply each of the digits
        //For Eg: Lets Take 18th Row and prime base is 7 here.
        //18(base-10)-->24(base-7)-->35-->15
        //This prooves that in the 18th row, there are 15 elements which are not divisible by 7

        private static void inc_m(int[] m, int index)
        {
            m[0] += 1;
            int i = 0;
            while (m[i] == index)
            {
                m[i] = 0;
                i++;
                m[i] += 1;
            }
        }

        private static int get_t(int[] m, int size)
        {
            int t = 1;
            for (int i = 0; i < size; i++)
            {
                t = t * (m[i] + 1);
            }

            return t;
        }

        public static void Main()
        {
            var watch = new System.Diagnostics.Stopwatch();
            watch.Start();

            //int mainCounter = 0;
            int limit = 1000000000;
            int base_index = 7;

            int size = (int)Math.Ceiling(Math.Log(limit) / Math.Log(base_index));
            Console.WriteLine(size);
            int[] m = new int[size];

            for (int i = 0; i < size; i++)
            {
                m[i] = 0;
            }

            BigInteger result = 0;

            for (int i = 0; i < limit; i++)
            {
                result += get_t(m, size);
                Console.WriteLine("Start");
                inc_m(m, base_index);
            }


            //for (int x = 0; x < 1000000000; x++)
            //{
            //    mainCounter += pascalEachRow(x);
            //}

            watch.Stop();

            Console.WriteLine(result);
            Console.WriteLine($"Time Elapsed: {watch.ElapsedMilliseconds} ms");

            Console.ReadKey();
        }
    }
}
