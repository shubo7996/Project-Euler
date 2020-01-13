using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;

namespace ProjectEuler
{
    class euler104
    {
        public static void readTextFromURL(string filepath)
        {
            WebClient web_client = new WebClient();
            string filehandle = web_client.DownloadString(filepath);
            processFile(filehandle);
        }

        private static void processFile(string filehandle)
        {
            List<int[]> cord_list = new List<int[]>();
            string[] lines = filehandle.Split('\n');
            for (int i = 0; i < lines.Count(); i++)
            {
                int[] inside_arr = lines[i].Split(',').Select(x => int.TryParse(x, out int n) ? n : 0).ToArray();
                cord_list.Add(inside_arr);
            }
            checkOrigin(cord_list);
        }

        private static void checkOrigin(List<int[]> cord_list)
        {
           foreach (int[] arr in cord_list)
            {
                IEnumerable<int> A1 = arr.Take(2).ToArray();
                IEnumerable<int> B1 = arr.Skip(2).Take(2);
                IEnumerable<int> C1 = arr.Skip(4).Take(2);

                
           }
           
        }
    }

    class MainPrograme
    {
        public static void Main()
        {
            string filepath = "https://projecteuler.net/project/resources/p102_triangles.txt";
            euler104.readTextFromURL(filepath);
            Console.ReadKey();

        }
    }
}
