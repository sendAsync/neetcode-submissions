class Solution {
    public double myPow(double x, int n) {
        if(n==0)return 1.0d;
        if(n<0)return 1/helper(x,n);
        return helper(x,n);
    }

    public double helper(double x, int n){
        if(n==0)return 1;
        if(n==1)return x;
        double ans = helper(x, n/2);
        if(n%2==0){
            return ans*ans;
        }else{
            return ans*ans*x;
        }
    }
}
