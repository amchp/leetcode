class Solution {
public:
    //Got lazy on this one and copied the top function of the internet after that knowing the first one of the number the problem becomes trivial
    unsigned int highestOneBit(unsigned int i) {
        i |= (i >>  1);
        i |= (i >>  2);
        i |= (i >>  4);
        i |= (i >>  8);
        i |= (i >> 16);
        return i - (i >> 1);
    }
    int bitwiseComplement(int n) {
        if(n == 0)return 1;
        int ans = n ^ (highestOneBit(((unsigned int)n) << 1) - 1);
        return  ans;
    }
};