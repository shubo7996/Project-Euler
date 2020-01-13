using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Windows;

namespace ProjectEuler
{
    interface ICrossProd
    {
        int getCrossProduct(Vector V1, Vector V2);
    }


    public struct Vector: ICrossProd
    {
        public int x;
        public int y;

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

        //public Vector(int x, int y)
        //{
        //    this.x = x;
        //    this.y = y;
        //}

        public int getCrossProduct(Vector V1, Vector V2)
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
            for (int i = 0; i < lines.Count(); i++)
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
                var vec1 = arr.Take(2).ToList();
                Vector vector1 = new Vector();
                vector1.x = vec1[0];vector1.y = vec1[1];

                var vec2 = arr.Skip(2).Take(2).ToList();
                Vector vector2 = new Vector();
                vector2.x = vec2[0];vector2.y = vec2[1];

                var vec3 = arr.Skip(4).Take(2).ToList();
                Vector vector3 = new Vector();
                vector3.x = vec3[0];vector3.y = vec3[1];

                if ((vect.getCrossProduct(vector1, vector2) > 0 && vect.getCrossProduct(vector1, vector3) < 0) || (vect.getCrossProduct(vector1, vector2) < 0 && vect.getCrossProduct(vector1, vector3) > 0))
                {
                    if ((vect.getCrossProduct(vector2, vector1) > 0 && vect.getCrossProduct(vector2, vector3) < 0) || (vect.getCrossProduct(vector2, vector1) < 0 && vect.getCrossProduct(vector2, vector3) > 0))
                    {
                        if ((vect.getCrossProduct(vector3, vector1) > 0 && vect.getCrossProduct(vector3, vector2) < 0) || (vect.getCrossProduct(vector3, vector1) < 0 && vect.getCrossProduct(vector3, vector2) > 0))
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
