using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class euler125
    {
        private static bool check_pal(int num)
        {
            int temp=num;
            int rev = 0;
            if (num > 100000000)
            {
                return false;
            }
            while (temp > 0)
            {
                rev = rev * 10 + (temp % 10);
                temp = temp / 10;
            }
            if (rev == num)
            {
                return true;
            }
            return false;
        }

        public static void Main(string[] args)
        {
            var watch = new System.Diagnostics.Stopwatch();
            watch.Start();
            List<int> pal_list = new List<int>();
            long final_sum = 0;
            for (int outer = 1; outer <= Math.Sqrt(100000000); outer++)
            {
                int main = (outer * outer);
                for (int inner = outer + 1; inner <= Math.Sqrt(100000000); inner++)
                {
                    main += (inner * inner);
                    if ((check_pal(main)) && !pal_list.Contains(main))
                    {
                        final_sum += main;
                        pal_list.Add(main);
                    }
                }
            }
            watch.Stop();
            Console.WriteLine($"Required Result is: {final_sum}");
            Console.WriteLine($"Time Elapsed: {watch.ElapsedMilliseconds} ms");
            Console.ReadLine();
        }
        
    }
}
