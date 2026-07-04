class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
        {return false;}

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};
// time : O(nlogn)
// space: O(n)/ O(1) depen=ding on sorting algo