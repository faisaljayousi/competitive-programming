class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.length() != t.length())
        {
            return false;
        }

        unordered_map<char, int> hashmap;

        for (auto c : s)
        {
            hashmap[c]++;
        };

        for (auto c : t)
        {
            hashmap[c]--;
            if (hashmap[c] < 0)
            {
                return false;
            }
        };

        return true;
    };
};
