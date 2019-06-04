using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class euler62
    {
        //private static char[] sortString(string str)
        //{
        //    char[] characters = str.ToCharArray();
        //    Array.Sort(characters);
        //    return characters;
        //}

        public static void Main(string[] args)
        {
            Dictionary<int, string> cubes = new Dictionary<int, string>();
            Dictionary<string, int> counts = new Dictionary<string, int>();
            int i = 0;
            string sorted_str;
            var result=0;
 
            while (i<8500)
            {
                string cube_str = Convert.ToString(Math.Pow(i,3));
                sorted_str = String.Concat(cube_str.OrderBy(c => c));
                cubes.Add(i, sorted_str);


                //result = Convert.ToInt32((from d in counts
                //            where d.Value == 5
                //            select d.Key).FirstOrDefault());

                i++;
            }

            foreach (string value in cubes.Values.ToList())
            {
                if (counts.ContainsKey(value))
                    counts[value]++;
                else
                    counts[value] = 1;
            }
            
            foreach (KeyValuePair<string,int> key_val in counts)
            {
                if (key_val.Value == 5)
                {
                    //Console.WriteLine(key_val.Key);
                    result=cubes.Values.ToList().IndexOf(key_val.Key);
                    Console.WriteLine(Math.Pow(result,3));
                    break;
                }
            }

            //Console.WriteLine(result ^ 3);       
            Console.ReadKey();
        }
    }
}

