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
            List<IEnumerable<int>> cord_list = new List<IEnumerable<int>>();
            string[] lines = filehandle.Split(new[] { Environment.NewLine }, StringSplitOptions.None);
            IEnumerable<int> inside_arr = new int[lines.Length];
            for (int i = 0; i < lines.Length; i++)
            {
                inside_arr = lines[i].Split(',').Select(x => Convert.ToInt32(x));
                Console.WriteLine(inside_arr);
                cord_list.Add(inside_arr);
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
