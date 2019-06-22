using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class Vertex
    {
        public string name;
        public int status;
        public int predecessor;
        public int length;

        public Vertex(string name)
        {
            this.name = name;
        }
    }

    class UndirectedGraph
    {
        public readonly int MAX_VERTICES = 40;

        int n;
        int e;
        int[,] adj;
        Vertex[] vertexList;

        private readonly int TEMPORARY = 1;
        private readonly int PERMANENT = 2;
        private readonly int NIL = -1;
        private readonly int INFINITY = 99999;

        public UndirectedGraph()
        {
            adj = new int[MAX_VERTICES, MAX_VERTICES];
            vertexList = new Vertex[MAX_VERTICES];
        }

        public int Vertices()
        {
            return n;
        }

        public void PrimsAlgorithm()
        {
            int c, v;

            int edgesInTree = 0;
            int wtTree = 0;

            for (v = 0; v < n; v++)
            {
                vertexList[v].status = TEMPORARY;
                vertexList[v].length = INFINITY;
                vertexList[v].predecessor = NIL;
            }

            int root = 0;
            vertexList[root].length = 0;

            while (true)
            {
                c = TempVertexMinL();
                if (c == NIL)
                {
                    if (edgesInTree == n - 1)
                    {
                        Console.WriteLine("Weight of the Minimal Spanning Tree is" + wtTree);
                    }
                    else
                        throw new InvalidOperationException
                            ("Graph is not Connected, Spanning Tree not possible");
                }
                vertexList[c].status = PERMANENT;

                if (c != root)
                {
                    edgesInTree++;
                    Console.WriteLine("(" + vertexList[c].predecessor + "," + c + ")");
                    wtTree = wtTree + adj[vertexList[c].predecessor, c];
                }

                for (v = 0; v < n; v++)
                {
                    if (IsAdjacent(c,v) && vertexList[v].status == TEMPORARY)
                    {
                        if (adj[c,v] < vertexList[v].length)
                        {
                            vertexList[v].length = adj[c, v];
                            vertexList[v].predecessor = c;
                        }
                    }
 
                }
            }
        }

        private int TempVertexMinL()
        {
            int min = INFINITY;
            int x = NIL;

            for (int v = 0; v < n; v++)
            {
                if (vertexList[v].status==TEMPORARY && vertexList[v].length < min)
                {
                    min = vertexList[v].length;
                    x = v;
                }
            }
            return x;
        }

    }

    class euler107
    {
        private Array[,] readFile(string filepath)
        {

        }

        public static void Main(string[] args)
        {

        }
    }
}
