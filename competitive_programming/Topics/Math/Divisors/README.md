# To know the Divisors of number n
### We loop from 1 till sqrt(n) or while i * i <= n

```cpp
  
  int n;
  cin>>n;

  for (int i=1; i * i <= n; i++) {
    if (n % i == 0) {
      if (n / i != i) {
        cout<<i<<endl;
      }
    }
  } 

```