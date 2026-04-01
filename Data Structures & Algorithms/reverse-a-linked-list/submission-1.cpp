class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        //mark cur,next pointers and temp
        ListNode* cur = nullptr; //cur is a pointer to a type ListNode
        ListNode* nxt = head;
        while(nxt){
            ListNode* temp = nxt->next;
            nxt->next = cur;
            cur = nxt;
            nxt = temp;
        }
        return cur;
    }
};