using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
//using System.Threading.Tasks;
using System.IO;

namespace ProjectEuler
{
    class euler98
    {
        const string filepath = @"C:\Users\kiit1\Documents\Codes\Project-Euler\euler98.txt";
        int[] squares;
        public void Hashing()
        {
            int result = 0;
            
            List<int> squareList = new List<int>();

            for  (int i = 2; i <= 31700; i++)
            {
                squareList.Add(i * i);
            }

            squares = squareList.ToArray();

            Dictionary<string, List<string>> anagrams= new Dictionary<string, List<string>>();
            string[] words = File.ReadAllText(filepath).Replace("\"", "").Split(',');
            foreach (string name in words)
            {
                string key = new String(name.ToCharArray().OrderBy(i=>i).ToArray());
                if (!anagrams.ContainsKey(key))
                {
                    anagrams.Add(key, new List<string>());
                }

                anagrams[key].Add(name);
                
            }

            foreach (KeyValuePair<string, List<string>> anagram in anagrams)
            {
                if (anagram.Value.Count <= 1) continue;
                for (int i = 0; i < anagram.Value.Count; i++)
                {
                    
                    for (int j = i + 1; j < anagram.Value.Count; j++)
                    {


                        int pairvalue = SquareAanagram(anagram.Value[i], anagram.Value[j]);
                        if (pairvalue > result)
                        {
                            result = pairvalue;
                        }
                        Console.WriteLine("\n {0} and {1} gives {2}", anagram.Value[i], anagram.Value[j], pairvalue);
                    }
                }

            }

            Console.WriteLine("\n{0}",result);

            Console.ReadKey();
        }

        private int SquareAanagram(string word1, string word2)
        {
            int max = 0;
            char[] w1array = word1.ToCharArray();
            char[] w2array = word2.ToCharArray();

            for (int i = 0; i < squares.Length; i++)
            {
                int squareLength = squares[i].ToString().Length;
                if (squareLength < word1.Length) continue;
                if (squareLength > word1.Length) break;
                bool match = true;
                int square = squares[i];
                Dictionary<char, int> map = new Dictionary<char, int>();
                for (int j = w1array.Length - 1; j >= 0; j--)
                {
                    int digit = square % 10;
                    square /= 10;
                    if (map.ContainsKey(w1array[j]))
                    {
                        if (map[w1array[j]] == digit)
                        {
                            continue;
                        }
                        else
                        {
                            match = false;
                            break;
                        }
                    }
                    if (map.ContainsValue(digit))
                    {
                        match = false;
                        break;
                    }
                    map.Add(w1array[j], digit);
                }
                if (!match) continue;
                int w2value = 0;
                if (map[w2array[0]] == 0)
                {
                    match = false;
                }
                else
                {
                    for (int j = 0; j < w2array.Length; j++)
                    {
                        w2value = w2value * 10 + map[w2array[j]];
                    }
                }
                if (!match) continue;
                if (Array.BinarySearch(squares, w2value) > -1)
                {
                    int maxpair = Math.Max(w2value, squares[i]);
                    max = Math.Max(max, maxpair);
                }
            }
            return max;
        }

    }

    class Programe
    {
        public static void Main(string[] args)
        {
            euler98 euler = new euler98();
            euler.Hashing();
        }
    }
}
