
#include<iostream>
#include<conio.h>
#define M 8
#define N 8
using namespace std;
  void flood(int out[][N], int x, int y, int xColor, int nColor)
{

    if (x < 0 || x >= M || y < 0 || y >= N)
        return;
    if (out[x][y] != xColor)
        return;
    if (out[x][y] == nColor)
        return;


    out[x][y] = nColor;

    flood(out, x+1, y, xColor, nColor);
    flood(out, x-1, y, xColor, nColor);
    flood(out, x, y+1, xColor, nColor);
    flood(out, x, y-1, xColor, nColor);
}

void findColor(int out[][N], int x, int y, int nColor)
{
    int xColor = out[x][y];
    flood(out, x, y, xColor, nColor);
}


int main()
{
    int out[M][N] =
                    {
                      {2, 0, 1, 1, 2, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 3, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 0, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                     };
    int x = 4, y = 4, nColor = 3;
    findColor(out, x, y, nColor);

    cout << "Updated output : \n";


    for (int i=0; i<M; i++)
    {
        for (int j=0; j<N; j++)
           cout << out[i][j] << " ";
        cout << endl;
    }
    return 0;
}
