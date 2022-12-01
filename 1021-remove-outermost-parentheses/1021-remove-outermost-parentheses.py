class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        final_answer = []
        counter=0
        for val in s:
            stack.append(val)
            if val=='(':
                counter+=1
            elif val==')':
                counter-=1
            if counter==0:
                final_answer+=stack[1:-1]
                stack=[]
        
        return "".join(final_answer)