```
syms x y z
f = [2*x+z == 1, x+y+z == 0];
solve(f, [x,z])

% Ibland ges lösningen i fields. För att nå värdena:

syms B g S I
eq = [-B*I*S+g*I == 0, B*I*S-g*I == 0, S+I == 1];
solution = solve(eq, [S I]);
S = solution.S
I = solution.I
```