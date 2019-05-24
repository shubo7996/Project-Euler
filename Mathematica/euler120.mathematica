/*
	**Mathematica Solution of PE120**
	Solution-@SubhamoyPaul
*/

f[limit_] := Sum[If[Mod[a, 2] == 0, Power[a, 2] - 2*a, Power[a, 2] - a], {a, 3, limit}]  
f[1000]