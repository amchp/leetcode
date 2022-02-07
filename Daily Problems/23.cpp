/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    //This was an interesting try to find the quickest way to join sorted link list
    //What I did was a data structure aproach to try to reduce waiting time
    struct CompareNode{
        bool operator()(ListNode* a, ListNode* b){
            return a->val > b->val;
        }
    };
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, CompareNode> q;
        for(int i = 0; i < lists.size(); ++i){
            if(lists[i])q.push(lists[i]);
        }
        if(q.empty())return nullptr;
        ListNode* head =  q.top();
        q.pop();
        ListNode* cur = head;
        if(cur->next)q.push(cur->next);
        while(!q.empty()){
            ListNode* n = q.top();
            q.pop();
            cur->next = n;
            cur = n;
            if(n->next)q.push(n->next);
        }
        return head;
    }
};