#include <bits/stdc++.h>
#include <complex>
using namespace std;
const double pi = 3.14159265358979323846;

void fft(complex<long double> *x, int n, bool inv=false) {
  for (int i = 0, j = 0; i < n; i++) {
    if (i < j) swap(x[i], x[j]);
    int m = n>>1;
    while (1 <= m && m <= j) j -= m, m >>= 1;
    j += m;
  }
  for (int mx = 1; mx < n; mx <<= 1) {
    complex<long double> wp, w = 1;
    if (inv) wp = exp(complex<long double>(0, pi / mx));
    else wp = exp(complex<long double>(0, -pi / mx));

    for (int m = 0; m < mx; m++, w *= wp) {
      for (int i = m; i < n; i += mx << 1) {
        complex<long double> t = x[i + mx] * w;
        x[i + mx] = x[i] - t;
        x[i] += t; }
    }
  }
  if (inv) for(int i = 0; i < n; i++) x[i] /= complex<long double>(n);
}

vector<int> input(int n) {
  map<char, int> map_dir;
  map_dir['n'] = 0;
  map_dir['w'] = 1;
  map_dir['e'] = 2;
  map_dir['s'] = 3;

  vector<int> te(n, 0);
  for(int i = 0; i < n; i++) {
    char s; cin >> s;
    if (s == '?') continue;

    int k; cin >> k;
    te[i] = k * 4 + map_dir[s];
  }
  return te;
}
int F[600000], G[600000];
bool H[600000];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, m;
  cin >> n >> m;
  for (int i = 0; i < n - m + 1; i++) H[i] = true;
  vector<int> a = input(n), b = input(m);

  int size = 2 * n+1;
  while (size & (size-1)) size++;
  complex<long double> *A = new complex<long double>[size], *B = new complex<long double>[size];

  vector<int> bits = {0,1,2,3,4};
  for(auto bit: bits) {
    for(int i = 0; i < size; i++) A[i] = 0, B[i] = 0;
    for(int i = 0; i < n; i++) A[n-i-1] = (a[i]==0)? 0 : (a[i] & (1 << bit)? 1 : -1);
    for(int i = 0; i < m; i++) B[i] = (b[i]==0)? 0 : (b[i] & (1 << bit)? 1 : -1);
    fft(A, size);
    fft(B, size);
    for(int i = 0; i < size; i++) A[i] *= B[i];
    fft(A, size, true);
    for(int i = 0; i < n - m + 1; i++) F[i] = int(round(real(A[n-1-i])));

    for(int i = 0; i < size; i++) A[i] = 0, B[i] = 0;
    for(int i = 0; i < n; i++) A[n-i-1] = (a[i] == 0)? 0 : 1;
    for(int i = 0; i < m; i++) B[i] = (b[i] == 0)? 0 : 1;
    fft(A, size);
    fft(B, size);
    for(int i = 0; i < size; i++) A[i] *= B[i];
    fft(A, size, true);
    for(int i = 0; i < n - m + 1; i++) G[i] = int(round(real(A[n-1-i])));

    for(int i = 0; i < n - m + 1; i++) H[i] = H[i] && F[i] == G[i];
  }

  int res = 0;
  for(int i = 0; i < n - m + 1; i++) if (H[i]) res++;
  cout << res;
}

main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m; cin >> n >> m;
    for (int i = 0; i < n - m + 1; i++) H[i] = true;
    vector<int> a = input(n)
}