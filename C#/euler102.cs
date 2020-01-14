using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;

namespace ProjectEuler
{
    interface IVectorFeature
    {
        int CrossProduct(Vector vec1, Vector vec2);
    }

    public struct Vector : IVectorFeature
    {
        private int x;
        private int y;

        public int X
        {
            get { return this.x; }
            set
            {
                if (value > 0 || value < 0)
                {
                    this.x = value;
                }
            }
        }

        public int Y
        {
            get { return this.y; }
            set
            {
                if (value > 0 || value < 0)
                {
                    this.y = value;
                }
            }
        }

        public Vector(int x, int y)
        {
            this.x = x;
            this.y = y;
        }

        public int CrossProduct(Vector V1, Vector V2)
        {
            return V1.x * V2.y - V1.y * V2.x;
        }
    }


    class euler104
    {
        
        public static void readTextFromURL(string filepath)
        {
            try
            {
                WebClient web_client = new WebClient();
                string filehandle = web_client.DownloadString(filepath);
                processFile(filehandle);
            }
            catch (WebException web_except)
            {
                Console.WriteLine(web_except.Message);
            }
           
        }

        private static void processFile(string filehandle)
        {
            List<int[]> cord_list = new List<int[]>();
            string[] lines = filehandle.Split('\n');
            for (int i = 0; i < lines.Length-1; i++)
            {
                int[] inside_arr = lines[i].Split(',').Select(x => int.TryParse(x, out int n) ? n : 0).ToArray();
                cord_list.Add(inside_arr);
            }
            checkOrigin(cord_list);
        }

        private static void checkOrigin(List<int[]> cord_list)
        {
            int mainCounter = 0;
            Vector vect = new Vector();
            foreach (int[] arr in cord_list)
            {
                IEnumerable<int> vec1 = arr.Take(2).ToList();
                Vector vector1 = new Vector(vec1.ElementAt(0), vec1.ElementAt(1));
                IEnumerable<int> vec2 = arr.Skip(2).Take(2).ToList();
                Vector vector2 = new Vector(vec2.ElementAt(0), vec2.ElementAt(1));
                IEnumerable<int> vec3 = arr.Skip(4).Take(2).ToList();
                Vector vector3 = new Vector(vec3.ElementAt(0), vec3.ElementAt(1));

                if ((vect.CrossProduct(vector1, vector2) > 0 && vect.CrossProduct(vector1, vector3) < 0) || (vect.CrossProduct(vector1, vector2) < 0 && vect.CrossProduct(vector1, vector3) > 0))
                {
                    if ((vect.CrossProduct(vector2, vector1) > 0 && vect.CrossProduct(vector2, vector3) < 0) || (vect.CrossProduct(vector2, vector1) < 0 && vect.CrossProduct(vector2, vector3) > 0))
                    {
                        if ((vect.CrossProduct(vector3, vector1) > 0 && vect.CrossProduct(vector3, vector2) < 0) || (vect.CrossProduct(vector3, vector1) < 0 && vect.CrossProduct(vector3, vector2) > 0))
                        {
                            mainCounter++;
                        }
                    }
                }
            }
            Console.WriteLine(mainCounter);
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
