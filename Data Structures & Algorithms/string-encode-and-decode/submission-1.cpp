class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded;
        
        for(const string& s: strs){
            encoded += to_string(s.size())+"#"+s;
        }

        return encoded;

    }

    vector<string> decode(string s) {
        int i=0;
        vector<string> res;
        while (i<s.size()){
            
            int cur = i;
            while (s[cur] != '#'){ //"" and '' are treated differently in C++
                cur++;
            }
            int length = stoi(s.substr(i, cur - i)); //will get the number before #
            i = cur+1; //point i to be at the index after #
            cur = i+length; //this will point to the end of the word since i will be at the beginning and j at the end of the word
            res.push_back(s.substr(i, length)); //we now push the 
            i=cur;
        }
        return res;   
    }   
};
