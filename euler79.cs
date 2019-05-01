using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace ProjectEuler79
{
    public static class Passcode
    {

        const string filepath = @"C:\Users\Documents\Codes\Project-Euler\euler79.txt";

        public static List<string> read_data_from_file()
        {
            List<string> lines = new List<string>();
            using (StreamReader reader = new StreamReader(filepath))
            {
                string line;
                while ((line=reader.ReadLine()) != null)
                {
                    lines.Add(line);
                }

                return lines;

            }
        }
    }
                  	
	
	class Programe
	{
        Stopwatch clock = Stopwatch.StartNew();

        public static Dictionary<char, List<int>> char_dict = new Dictionary<char, List<int>>();
        public static List<string> text_file = Passcode.read_data_from_file();
        public static Dictionary<char,double> avg_pos = new Dictionary<char, double>();
        static int counter;
        static int total=0;
        

        private static void make_char_pos_dict(int i,int j)
        {
            char each_char = text_file[i].ToCharArray()[j];

            if (char_dict.ContainsKey(each_char))
            {
                List<int> pos_list = char_dict[each_char];
                pos_list.Add(j);
            }
            else
            {
                List<int> list = new List<int>();
                list.Add(j);
                char_dict.Add(each_char, list);
            }
        }

		public static void Main(String[] args)
		{
             
            //Console.WriteLine((text_file[5].ToCharArray()).Length);
            for (int i = 0; i < text_file.Count; i++)
            {
                for (int j=0; j<(text_file[i].ToCharArray()).Length; j++)
                {
                    Programe.make_char_pos_dict(i, j);
                }
                
            }
            
            foreach (KeyValuePair<char, List<int>> iter in char_dict)
            {
                //Console.WriteLine(iter.Key);
                counter = 0;
                total = 0;

                foreach (int each in iter.Value)
                {
                    //Console.Write(each);
                    total += each;
                    counter++;
                }

                try
                {
                    double final_avg = (double)(total) / (double)(counter);
                    avg_pos.Add(iter.Key, final_avg);
                    Console.Write('\n');
                }
                catch(ArithmeticException e)
                {
                    Console.WriteLine("You need to reconsider you programe: ('\n')",e);
                }
                
            }

            Console.Write('\n');

            var orderedDict = from entry in avg_pos orderby entry.Value ascending select entry;

            foreach (KeyValuePair<char, double> iter_again in orderedDict)
            {
                Console.Write(iter_again.Key);
            }

            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);

            Console.ReadKey();
        }

	} 
}