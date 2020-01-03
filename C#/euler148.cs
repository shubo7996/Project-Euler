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
        private static int pascalEachRow(int n)
        {
            BigInteger[] row = new BigInteger[n + 1];
            row[0] = row[n] = 1;

            for (int i = 0; i < n >> 1; i++)
            {
                BigInteger l = (row[i] * (n - i)) / (i + 1);
                row[i + 1] = row[n - i - 1] = l;
            }

            IEnumerable<BigInteger> div_list = from number in row where number % 7 != 0 select number;
            return div_list.Count();
        }

        public static void Main()
        {
            var watch = new System.Diagnostics.Stopwatch();
            watch.Start();

            int mainCounter = 0;

            for (int x = 0; x < 1000000000; x++)
            {
                mainCounter += pascalEachRow(x);
            }

            watch.Stop();

            Console.WriteLine(mainCounter);
            Console.WriteLine($"Time Elapsed: {watch.ElapsedMilliseconds} ms");

            Console.ReadKey();
        }
    }
}