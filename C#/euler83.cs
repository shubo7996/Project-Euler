using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace ProjectEuler
{
    class euler83
    {
        const string filepath = @"C:\Users\kiit1\Documents\Codes\Project-Euler\euler83.txt";
        const int ROWS = 80;
        const int COLS = 80;
        static readonly int[] direction_rows= { +1, -1, 0, 0};
        static readonly int[] direction_cols = { 0, 0, +1, -1 };

        private static int[,] readFile(string filepath)
        {
            int[,] adj_matrix = new int[ROWS,COLS];
            int row_ = 0, col_ = 0;
            using (StreamReader reader = File.OpenText(filepath))
            {
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    string[] row = line.Split(',');
                    foreach (string col in row)
                    {
                        adj_matrix[row_, col_] = int.Parse(col);
                        col_++;
                    }
                    row_++;
                    col_ = 0;
                }
            }

            return adj_matrix;
        }

        private static int solve(int[,] adjMatrix)
        {
            Tuple<int,int> current_tup = new Tuple<int,int>(0, 0);
            Dictionary<Tuple<int, int>, int> permanent = new Dictionary<Tuple<int, int>, int>();

            permanent.Add(current_tup,weight(current_tup));

            Dictionary<Tuple<int, int>, int> temporary = new Dictionary<Tuple<int, int>, int>();
            int total_nodes = ROWS * COLS;

            while ((permanent.Count)< total_nodes)
            {
                List<Tuple<int, int>> neighbours = find_neighbours(current_tup);
                foreach (Tuple<int,int> node in neighbours)
                {
                    
                    if (!permanent.ContainsKey(node))
                    {
                        if (temporary.ContainsKey(node))
                        {
                            if (temporary[node] > permanent[current_tup] + weight(node))
                            {
                                temporary[node] = permanent[current_tup] + weight(node);
                            }
                        }
                        else
                        {
                            try
                            {
                                temporary.Add(node, permanent[current_tup] + weight(node));
                            }
                            catch (Exception e)
                            {
                                Console.WriteLine(e.Message);
                            }                            
                        }
                    }                    
                }

                int min_weight = temporary.Values.Min();
                List<Tuple<int, int>> min_nodes = new List<Tuple<int, int>>();
                foreach (KeyValuePair<Tuple<int,int>,int> key_val in temporary)
                {
                    if (key_val.Value == min_weight)
                    {
                        min_nodes.Add(key_val.Key);
                    }
                }

                Tuple<int, int> min_singular_node = min_nodes[0];
                permanent[min_singular_node] = min_weight;
                temporary.Remove(min_singular_node);
                current_tup = min_singular_node;

            }
            return permanent[new Tuple<int,int>(ROWS-1,COLS-1)];
        }

        private static List<Tuple<int,int>> find_neighbours(Tuple<int,int> tup)
        {
            var indices = tup;
            int r = indices.Item1;
            int c = indices.Item2;
            List<Tuple<int, int>> moves = new List<Tuple<int, int>>();
            for (int x = 0; x < 4; x++)
            {
                int rr = r + direction_rows[x];
                int cc = c + direction_cols[x];

                if (rr<0 || cc < 0)
                {
                    continue;
                }
                if (rr>=ROWS || cc >= COLS)
                {
                    continue;
                }
                moves.Add(Tuple.Create(rr, cc));
            }
            return moves;
        }

        private static int weight(Tuple<int, int> tup)
        {
            int row = tup.Item1;
            int col = tup.Item2;

            int[,] matrix = readFile(filepath);
            return matrix[row,col];
        }


        public static void Main(string[] args)
        {            
            int[,] adj_mat = readFile(filepath);
            int result = solve(adj_mat);
            Console.WriteLine(result);
            Console.ReadKey();
        }
    }
}
